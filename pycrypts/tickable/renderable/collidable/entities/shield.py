from typing import TYPE_CHECKING

import pygame

from .projectiles.projectile import Projectile
from .entity import Entity
from ..collidable import Collidable

if TYPE_CHECKING:
    from .....game import PyCrypts
    from .....rooms.room import Room
    from .living.monsters.monster import Monster


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

        self.position = self.monster.position + (self.monster.size * 2.0 / 5.0, self.monster.size * 2.0 / 5.0)

    def is_colliding(self, entity: Collidable) -> bool:
        if not isinstance(entity, Projectile):
            return False

        if isinstance(entity.shooter, type(self.monster)):
            return False

        if self.position.distance_squared_to(entity.position) < ((self.size / 2 + entity.size / 2) ** 2):
            entity.unload()
            pygame.mixer.Sound.play(self.block_sound)

        return False

    def is_hitting(self, entity: Collidable) -> bool:
        return super().is_colliding(entity)