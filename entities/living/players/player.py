import pygame
from pygame import Vector2

from entities.entity import Entity
from entities.living.living_entity import LivingEntity
from enums.movement_keys import movement_keys

class Player(LivingEntity):

    players = []

    def __init__(self, screen, position, character, size, movement_type):
        super().__init__(screen, position, "players/" + character, size, 100)

        self.movement_type = movement_type

        Player.players.append(self)

    def tick(self):
        super().tick()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.attack()

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

    def remove(self):
        super().remove()
        Player.players.remove(self)

    def attack(self):
        attackable_entities = []

        for entity in Entity.entities:
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

            if Vector2(closest_entity.position).distance_squared_to(self.position) < Vector2(entity.position).distance_squared_to(self.position):
                closest_entity = entity

        self.attack_entity(closest_entity)

    def attack_entity(self, entity):
        entity.damage(10)
