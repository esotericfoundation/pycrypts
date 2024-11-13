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

        self.no_clip = False

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
            distance_travelled = distance_travelled.normalize() * 250 * Game.dt

            self.position += distance_travelled

            for collidable in Collidable.collidables:
                if collidable == self:
                    continue

                if self.is_colliding(collidable) or collidable.is_colliding(self):
                    self.position -= distance_travelled
                    break

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        return self.position.distance_to(location) < (self.size / 2)

    def is_colliding(self, entity: Collidable) -> bool:
        if self.no_clip:
            return False

        if isinstance(entity, Entity):
            return self.position.distance_to(entity.position) < (self.size / 2 + entity.size / 2)

        from tickable.collidable.walls.wall import Wall
        if isinstance(entity, Wall):
            return entity.is_colliding(self)
        return False

    def remove(self):
        super().remove()

        if self in Entity.entities:
            Entity.entities.remove(self)

    def get_radius(self):
        return self.size / 2.0

    def get_center(self):
        return self.position

    def get_top_left(self):
        return self.position - (self.get_radius(), self.get_radius())

    def get_bottom_right(self):
        return self.position + (self.get_radius(), self.get_radius())

    def get_top_right(self):
        return self.position - (-self.get_radius(), self.get_radius())

    def get_bottom_left(self):
        return self.position + (-self.get_radius(), self.get_radius())

    def get_points(self):
        return [self.get_top_left(), self.get_bottom_right(), self.get_top_right(), self.get_bottom_left()]
