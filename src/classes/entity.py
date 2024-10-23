import pygame

from src.enums.movement_keys import movement_keys


class Entity:

    def __init__(self, screen, position, character, size, movement_type):
        self.screen = screen

        self.position = position

        image = pygame.image.load("./assets/characters/" + character + ".png").convert_alpha()
        self.image = pygame.transform.scale(image, (size, size))

        self.size = size

        self.movement_type = movement_type

    def render(self):
        self.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

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

        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 0.15

            self.position += distance_travelled

    def is_inside_hitbox(self, location):
        return self.position.distance_to(location) < (self.size / 2)

    def is_colliding(self, entity):
        return self.position.distance_to(entity.position) < (self.size / 2 + entity.size / 2)
