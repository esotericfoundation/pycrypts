import pygame
from pygame import Vector2

from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.living.living_entity import LivingEntity


class SawTrap(Entity):
    def __init__(self, start: Vector2, end: Vector2, size: int, game: "Game"):
        super().__init__(start, "saw_trap", size, game)
        self.start = start
        self.end = end
        self.moving_to_end = True

        self.rotation = 0
        self.rotation_speed = 0.1

    def tick(self):
        super().tick()

        # self.rotation += self.rotation_speed * self.game.dt
        # self.image = pygame.transform.rotate(self.image, self.rotation)

        if self.moving_to_end:
            self.move_towards_location(self.end, 1)
            if self.position.distance_squared_to(self.end) < 25:
                print("Reached end")
                self.moving_to_end = False
        else:
            self.move_towards_location(self.start, 1)
            if self.position.distance_squared_to(self.start) < 25:
                print("Reached start")
                self.moving_to_end = True

    def is_colliding(self, entity: Collidable) -> bool:
        is_colliding = super().is_colliding(entity)

        if is_colliding and isinstance(entity, LivingEntity):
            entity.damage(1)

        return is_colliding
