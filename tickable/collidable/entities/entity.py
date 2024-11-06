import pygame
from pygame import Vector2

from game import Game
from tickable.collidable.collidable import Collidable


class Entity(Collidable):
    entities: list["Entity"] = []

    def __init__(self, position: tuple[int, int], character: str, size: int):
        super().__init__()
        self.position = Vector2(position)

        image = pygame.image.load("./assets/images/entities/" + character + ".png").convert_alpha()
        self.image = pygame.transform.scale(image, (size, size))

        self.size = size

        Entity.entities.append(self)

    def render(self):
        Game.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

    def move(self):
        pass

    def move_without_collision(self, distance_travelled: Vector2):
        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 0.15

            self.position += distance_travelled

            for entity in Collidable.collidables:
                if entity == self:
                    continue

                if self.is_colliding(entity) or entity.is_colliding(self):
                    self.position -= distance_travelled
                    break

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        return self.position.distance_to(location) < (self.size / 2)

    def is_colliding(self, entity: Collidable) -> bool:
        if isinstance(entity, Entity):
            return self.position.distance_to(entity.position) < (self.size / 2 + entity.size / 2)
        return False # Collisions with things other than entities will be managed by those classes themselves.

    def remove(self):
        super().remove()

        if self in Entity.entities:
            Entity.entities.remove(self)
