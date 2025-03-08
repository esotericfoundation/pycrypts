import math

import pygame

from typing import TYPE_CHECKING
from pycrypt.tickable.renderable.collidable.collidable import Collidable
from pycrypt.tickable.renderable.collidable.entities.entity import Entity
from pycrypt.tickable.renderable.collidable.entities.projectiles.fireball import Fireball
from pycrypt.tickable.renderable.collidable.entities.living.living_entity import LivingEntity

if TYPE_CHECKING:
    from pycrypt.game import PyCrypt


class Arrow(Fireball):
    def __init__(self, target: tuple[int, int], position: tuple[int, int], size: int, game: "PyCrypt"):
        super().__init__(target, position, size, game, 2, "arrow")

        angle = math.atan2(self.target.y - self.position.y, self.target.x - self.position.x)
        self.image = pygame.transform.rotate(self.image, -math.degrees(angle) - 45)
        self.hit = False

    def is_colliding(self, entity: Collidable) -> bool:
        if self.hit:
            return False

        if isinstance(entity, Entity) and entity.no_clip:
            return False

        from pycrypt.tickable.renderable.collidable.entities.living.players.player import Player
        if isinstance(entity, Player):
            return False

        if isinstance(entity, Arrow):
            return False

        is_colliding = Entity.is_colliding(self, entity)

        if is_colliding:
            if isinstance(entity, Fireball):
                if not entity.strong:
                    entity.unload()
                return False

            self.hit = True
            self.unload()

            if isinstance(entity, LivingEntity):
                entity.damage(10)
                return False
            return True

        return False
