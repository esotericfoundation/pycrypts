import math
from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .arrow import Arrow
from .fireball import Fireball
from ..entity import Entity
from ...collidable import Collidable

if TYPE_CHECKING:
    from ......game import PyCrypts
    from ......rooms.room import Room
    from ..living.monsters.monster import Monster


class Shield(Entity):
    def __init__(self, monster: "Monster", game: "PyCrypts", room: "Room"):
        super().__init__(game, room, monster.position, "shield", 64)

        self.monster = monster
        self.target = None
        self.no_clip = True
        self.block_sound = game.get_sound("shield_block")

    def tick(self):
        super().tick()

        if not self.monster.is_valid():
            self.unload()

        self.position = self.monster.position + (20, 20)

    def is_colliding(self, entity: Collidable) -> bool:
        if not isinstance(entity, Arrow) and not isinstance(entity, Fireball):
            return False

        if self.position.distance_squared_to(entity.position) < ((self.size / 2 + entity.size / 2) ** 2):
            entity.unload()
            pygame.mixer.Sound.play(self.block_sound)

        return False

    def is_hitting(self, entity: Collidable) -> bool:
        return super().is_colliding(entity)