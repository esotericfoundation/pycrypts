import pygame

from src.classes.entity import Entity
from src.enums.movement_keys import movement_keys

class Player(Entity):

    players = []

    def __init__(self, screen, position, character, size, movement_type):
        super().__init__(screen, position, "characters/" + character, size)

        self.movement_type = movement_type

        Player.players.append(self)

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
