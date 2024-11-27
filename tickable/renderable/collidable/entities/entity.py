import pygame
from pygame import Vector2

from tickable.renderable.collidable.collidable import Collidable, get_collidables


def get_entities():
    return list(filter(lambda collidable: isinstance(collidable, Entity), get_collidables()))


class Entity(Collidable):
    def __init__(self, position: tuple[int, int] | Vector2, character: str, size: int, game: "Game"):
        super().__init__()

        self.position = Vector2(position)
        self.velocity = Vector2(0, 0)

        self.game = game

        self.image = pygame.image.load("./assets/images/entities/" + character + ".png").convert_alpha()
        self.base_image = self.image

        self.absolute_size = size
        self.size = size

        self.no_clip = False

        if game.current_room is not None:
            self.set_scale(game.current_room.entity_scale)

        self.base_image = self.image

    def render(self):
        self.game.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

    def move(self):
        self.move_without_collision(self.velocity)
        self.velocity *= 0.9

        if self.velocity.magnitude() < 0.1:
            self.velocity = Vector2(0, 0)

        pass

    def move_without_collision(self, distance_travelled: Vector2, speed_factor: float = 1):
        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 250 * speed_factor * self.game.dt

            self.position.x += distance_travelled.x
            collision_x = any(self.is_colliding(collidable) or collidable.is_colliding(self) for collidable in get_collidables() if collidable != self)
            if collision_x:
                self.position.x -= distance_travelled.x

            self.position.y += distance_travelled.y
            collision_y = any(self.is_colliding(collidable) or collidable.is_colliding(self) for collidable in get_collidables() if collidable != self)
            if collision_y:
                self.position.y -= distance_travelled.y

    def move_towards(self, entity: "Entity", speed_factor: float = 1):
        distance = entity.position - self.position
        self.move_without_collision(distance, speed_factor)

    def move_away_from(self, entity: "Entity", speed_factor: float = 1):
        distance = entity.position - self.position
        distance *= -1
        self.move_without_collision(distance, speed_factor)

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
        self.image = pygame.transform.scale(self.base_image, (self.size, self.size))

    def get_radius(self):
        return self.size / 2.0

    def get_center(self):
        return self.position

    def get_actual_center(self):
        return self.position + (self.size / 2, self.size / 2)

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
        distance = other.get_actual_center() - self.get_actual_center()
        direction = distance.normalize()

        current_position = self.get_actual_center() + direction
        while (current_position - self.get_actual_center()).magnitude() < distance.magnitude():
            for wall in self.game.current_room.walls:
                if wall.contains_point(current_position):
                    return False

            current_position += direction

        return True
