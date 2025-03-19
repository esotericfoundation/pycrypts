from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from ..living_entity import LivingEntity
from ...projectiles.arrow import Arrow
from ...projectiles.sword import Sword
from ....collidable import Collidable

if TYPE_CHECKING:
    from .......game import PyCrypts
    from .......rooms.room import Room


class Player(LivingEntity):
    attack_cooldown = 0.75
    attack_range = 175
    regeneration_rate = 0.5

    def __init__(self, position: tuple[int, int], character: str, size: int, movement_type: str, attack_key: int, game: "PyCrypts", room: "Room"):
        super().__init__(position, "players/" + character, size, 100, game, room)

        self.movement_type = movement_type
        self.attack_key = attack_key

        self.time_since_last_attack = Player.attack_cooldown + 1
        self.time_since_last_regeneration = 0

        self.light_radius = 400

    def load(self):
        super().load()
        self.game.players.append(self)

    def unload(self):
        super().unload()
        if self in self.game.players:
            self.game.players.remove(self)

    def tick(self):
        super().tick()

        self.time_since_last_attack += self.game.dt
        self.time_since_last_regeneration += self.game.dt

        keys = pygame.key.get_pressed()
        if keys[self.attack_key]:
            self.attack()

        if self.time_since_last_regeneration >= Player.regeneration_rate:
            if self.health < self.max_health:
                self.health = min(self.health + 1, self.max_health)
                self.time_since_last_regeneration = 0

        if keys[pygame.K_LALT]:
            self.no_clip = not self.no_clip

    def render(self):
        super().render()
        self.render_light(self.light_radius)

    def move(self):
        super().move()

        keys = pygame.key.get_pressed()

        distance_travelled = pygame.Vector2()

        if keys[pygame.K_w if self.movement_type == "WASD" else pygame.K_UP]:
            distance_travelled.y -= 1
        if keys[pygame.K_s if self.movement_type == "WASD" else pygame.K_DOWN]:
            distance_travelled.y += 1
        if keys[pygame.K_a if self.movement_type == "WASD" else pygame.K_LEFT]:
            distance_travelled.x -= 1
        if keys[pygame.K_d if self.movement_type == "WASD" else pygame.K_RIGHT]:
            distance_travelled.x += 1

        if distance_travelled.magnitude_squared() == 0:
            return

        self.velocity += distance_travelled.normalize() * 250 * self.game.dt

        if self.velocity.magnitude_squared() == 0:
            return

        self.velocity = self.velocity.normalize() * min(self.velocity.magnitude(), 25)

    def attack(self):
        if self.time_since_last_attack < Player.attack_cooldown:
            return

        attackable_entities: list[LivingEntity] = list(filter(lambda e: not isinstance(e, Player) and self.sees_other(e), self.room.get_living_entities()))

        if len(attackable_entities) == 0:
            return

        closest_entity = min(attackable_entities, key=lambda e: e.position.distance_squared_to(self.position))

        self.attack_entity(closest_entity)

    def sword_attack(self, entity: LivingEntity):
        Sword(entity, self, self.get_center(), self.game, self.room)

    def bow_attack(self, entity: LivingEntity):
        Arrow(entity.get_center(), self.get_center(), 32, self.game, self.room)

    def attack_entity(self, entity: LivingEntity):
        if entity.position.distance_squared_to(self.position) < (Player.attack_range * Player.attack_range) * self.game.current_room.entity_scale * self.game.current_room.entity_scale:
            self.sword_attack(entity)
        else:
            self.bow_attack(entity)

        self.time_since_last_attack = 0

    def damage(self, damage: int):
        super().damage(damage)

        sound = self.game.get_sound("damage")
        pygame.mixer.Sound.play(sound)

    def die(self):
        super().die()

        if len(self.game.players) == 0:
            self.game.end()

    def is_colliding(self, entity: Collidable) -> bool:
        if isinstance(entity, Arrow):
            return False

        if isinstance(entity, Sword):
            return False

        return super().is_colliding(entity)
