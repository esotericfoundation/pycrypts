import math

import pygame

from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.entity import Entity


class Sword(Entity):

    def __init__(self, target, position, game):
        super().__init__(position, "sword", 64, game)

        self.target = target
        self.time_left = 0.5

        target_angle = 360 - math.degrees((self.target.get_center() - self.position).as_polar()[1])
        self.image = pygame.transform.rotate(self.image, target_angle)

    def tick(self):
        super().tick()
        self.time_left -= self.game.dt

        if self.time_left <= 0:
            self.unload()

    def is_colliding(self, entity: Collidable) -> bool:
        return False

    def is_hitting(self, entity: Collidable) -> bool:
        return super().is_colliding(entity)
