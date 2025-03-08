import math
from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from pycrypt.tickable.renderable.collidable.collidable import Collidable
from pycrypt.tickable.renderable.collidable.entities.entity import Entity
from pycrypt.tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from pycrypt.tickable.renderable.collidable.entities.projectiles.arrow import Arrow
from pycrypt.tickable.renderable.collidable.entities.projectiles.fireball import Fireball

if TYPE_CHECKING:
    from pycrypt.game import PyCrypt
    from pycrypt.tickable.renderable.collidable.entities.living.players.player import Player


class Sword(Entity):

    def __init__(self, target, user: "Player", position: tuple[int, int] | Vector2, game: "PyCrypt"):
        super().__init__(position, "sword", 64, game)

        self.target = target
        self.user = user
        self.time_left = 0.5
        self.used = False

    def tick(self):
        super().tick()
        self.time_left -= self.game.dt

        if self.time_left <= 0:
            self.unload()

        offset = Vector2(self.target.position - self.user.position)

        y = offset.y
        offset.y = 0

        offset = offset.normalize() * (self.user.size / 2)
        offset.y = math.copysign(1, y) * (self.user.size / 4)

        if offset.x < 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
        else:
            self.image = self.base_image

        self.position = self.user.position + offset

        if self.is_hitting(self.target) and not self.used:
            if isinstance(self.target, Fireball):
                self.target.unload()
                return

            if isinstance(self.target, Arrow):
                self.target.unload()
                return

            if isinstance(self.target, LivingEntity):
                self.target.damage(12)
                self.target.velocity = (self.target.position - self.user.position).normalize() * 40
                self.used = True
                self.time_left = 0.2

    def is_colliding(self, entity: Collidable) -> bool:
        if super().is_colliding(entity):
            from pycrypt.tickable.renderable.collidable.entities.living.players.player import Player
            if isinstance(entity, Player):
                return False

            if isinstance(entity, Arrow):
                entity.unload()

            if isinstance(entity, Fireball):
                entity.unload()

            return True
        return False

    def is_hitting(self, entity: Collidable) -> bool:
        return super().is_colliding(entity)
