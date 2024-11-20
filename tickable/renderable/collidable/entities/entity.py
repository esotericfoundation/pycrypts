import pygame
from pygame import Vector2

from tickable.renderable.collidable.collidable import Collidable, get_collidables


def get_entities():
    return filter(lambda collidable: isinstance(collidable, Entity), get_collidables())


class Entity(Collidable):
    def __init__(self, position: tuple[int, int] | Vector2, character: str, size: int, game: "Game"):
        super().__init__()
        self.position = Vector2(position)

        self.game = game

        self.image = pygame.image.load("./assets/images/entities/" + character + ".png").convert_alpha()

        self.absolute_size = size
        self.size = size

        self.no_clip = False

        if game.current_room is not None:
            self.set_scale(game.current_room.entity_scale)

    def render(self):
        self.game.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

    def move(self):
        pass

    def move_without_collision(self, distance_travelled: Vector2):
        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 250 * self.game.dt

            self.position += distance_travelled

            for collidable in get_collidables():
                if collidable == self:
                    continue

                if self.is_colliding(collidable) or collidable.is_colliding(self):
                    self.position -= distance_travelled
                    break

    def is_colliding(self, entity: Collidable) -> bool:
        if self.no_clip:
            return False

        if isinstance(entity, Entity):
            return self.position.distance_to(entity.position) < (self.size / 2 + entity.size / 2)

        from tickable.renderable.collidable.walls.wall import Wall
        if isinstance(entity, Wall):
            return entity.is_colliding(self)
        return False

    def set_scale(self, scale: float):
        self.size = self.absolute_size * scale
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

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

    def sees_other(self, other: "Entity") -> bool:
        distance = other.position - self.position
        direction = distance.normalize() * 1

        current_position = self.position + direction
        while current_position.x < other.position.x:
            for wall in self.game.current_room.walls:
                if wall.contains_point(current_position):
                    return False

            current_position += direction

        return True
