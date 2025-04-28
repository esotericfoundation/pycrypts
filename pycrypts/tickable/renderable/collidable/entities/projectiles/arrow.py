import math
from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .fireball import Fireball
from .projectile import Projectile
from ..bozos_ball import BozosBall
from ..entity import Entity
from ..living.living_entity import LivingEntity
from ...collidable import Collidable

if TYPE_CHECKING:
    from ......game import PyCrypts
    from ......rooms.room import Room


class Arrow(Projectile):
    def __init__(self, game: "PyCrypts", room: "Room", shooter: Entity, position: tuple[int, int] | Vector2, size: int, direction: Vector2, speed: float = 2.6):
        super().__init__(game, room, shooter, position, "arrow", size, direction, speed)

        angle = math.atan2(self.direction.y, self.direction.x)
        self.image = pygame.transform.rotate(self.image, -math.degrees(angle) - 45)

    def on_hit(self, collidable: Collidable):
        if isinstance(collidable, Fireball):
            if not collidable.strong:
                collidable.unload()
                return

        if isinstance(collidable, LivingEntity):
            collidable.damage(10)

        super().on_hit(collidable)
