import pygame
from pygame import Vector2

from enums.movement_keys import movement_keys
from tickable.renderable.collidable.entities.entity import get_entities
from tickable.renderable.collidable.entities.living.living_entity import LivingEntity


def get_players():
    return filter(lambda entity: isinstance(entity, Player), get_entities())

class Player(LivingEntity):
    attack_cooldown = 1000
    attack_range = 14400

    def __init__(self, position: tuple[int, int], character: str, size: int, movement_type: int, attack_key: int, game: "Game"):
        super().__init__(position, "players/" + character, size, 100, game)

        self.movement_type = movement_type
        self.attack_key = attack_key

        self.time_since_last_attack = Player.attack_cooldown + 1

    def tick(self):
        super().tick()

        self.time_since_last_attack += 1

        keys = pygame.key.get_pressed()
        if keys[self.attack_key]:
            self.attack()

        if keys[pygame.K_LALT]:
            self.no_clip = not self.no_clip

    def move(self):
        keys = pygame.key.get_pressed()

        distance_travelled = pygame.Vector2()

        if keys[pygame.K_w if self.movement_type == movement_keys["WASD"] else pygame.K_UP]:
            distance_travelled.y -= 1
        if keys[pygame.K_s if self.movement_type == movement_keys["WASD"] else pygame.K_DOWN]:
            distance_travelled.y += 1
        if keys[pygame.K_a if self.movement_type == movement_keys["WASD"] else pygame.K_LEFT]:
            distance_travelled.x -= 1
        if keys[pygame.K_d if self.movement_type == movement_keys["WASD"] else pygame.K_RIGHT]:
            distance_travelled.x += 1

        self.move_without_collision(distance_travelled)

    def attack(self):
        if self.time_since_last_attack < Player.attack_cooldown:
            return

        attackable_entities = []

        for entity in get_entities():
            if not isinstance(entity, LivingEntity):
                continue

            if isinstance(entity, Player):
                continue

            attackable_entities.append(entity)

        if len(attackable_entities) == 0:
            return

        closest_entity = None
        for entity in attackable_entities:
            if closest_entity is None:
                closest_entity = entity
                continue

            if Vector2(closest_entity.position).distance_squared_to(
                    self.position) < entity.position.distance_squared_to(self.position):
                closest_entity = entity

        self.attack_entity(closest_entity)

    def sword_attack(self, entity: LivingEntity):
        pass

    def bow_attack(self, entity: LivingEntity):
        pass

    def attack_entity(self, entity: LivingEntity):
        if entity.position.distance_squared_to(self.position) < 14400:
            self.sword_attack(entity)
        else:
            self.bow_attack(entity)

        self.time_since_last_attack = 0

    def damage(self, damage: int):
        super().damage(damage)

        sound = pygame.mixer.Sound('assets/sounds/damage.mp3')
        sound.set_volume(0.125)
        pygame.mixer.Sound.play(sound)
