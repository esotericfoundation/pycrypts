from typing import TYPE_CHECKING

from pygame import Vector2

from .entity import Entity
from ..collidable import Collidable
from .....rooms.room import Room

if TYPE_CHECKING:
    from .....game import PyCrypts


class BozosBall(Entity):
    def __init__(self, game: "PyCrypts", room: "Room", position: tuple[int, int] | Vector2, color: str = "red", size: int = 48):
        super().__init__(position, f"bozos_ball_{color}", size, game, room)

    def is_colliding(self, entity: Collidable) -> bool:
        from .living.monsters.bozo import Bozo
        if isinstance(entity, Bozo):
            return False

        return super().is_colliding(entity)
