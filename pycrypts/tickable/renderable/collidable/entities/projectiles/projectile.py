from typing import TYPE_CHECKING

from pygame import Vector2

from pycrypts.rooms.room import Room
from ..entity import Entity
from ...collidable import Collidable

if TYPE_CHECKING:
    from pycrypts.game import PyCrypts


class Projectile(Entity):

    def __init__(self, game: "PyCrypts", room: "Room", position: tuple[int, int] | Vector2, character: str, size: int, direction: Vector2):
        super().__init__(game, room, position, character, size)

        self.direction = direction

    def move(self):
        self.move_without_collision(self.direction)

    def is_colliding(self, entity: Collidable) -> bool:
        colliding = super().is_colliding(entity)

        if not colliding:
            return False

        self.on_hit(entity)
        return True

    def on_hit(self, collidable: Collidable):
        self.unload()
