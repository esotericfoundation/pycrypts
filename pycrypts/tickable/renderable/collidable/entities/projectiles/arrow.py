import math
from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .fireball import Fireball
from ..entity import Entity
from ..living.living_entity import LivingEntity
from ...collidable import Collidable

if TYPE_CHECKING:
    from ......game import PyCrypts
    from ......rooms.room import Room


class Arrow(Fireball):
    def __init__(self, target: Vector2, position: Vector2, size: int, game: "PyCrypts", room: "Room"):
        super().__init__(target, position, size, game, room, 2, "arrow")

        angle = math.atan2(self.target.y - self.position.y, self.target.x - self.position.x)
        self.image = pygame.transform.rotate(self.image, -math.degrees(angle) - 45)
        self.hit = False

    def is_colliding(self, entity: Collidable) -> bool:
        if self.hit:
            return False

        if isinstance(entity, Entity) and entity.no_clip:
            return False

        from ..living.players.player import Player
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
