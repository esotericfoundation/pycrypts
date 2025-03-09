from typing import TYPE_CHECKING

from ..renderable import Renderable

if TYPE_CHECKING:
    from ....game import PyCrypts
    from ....rooms.room import Room


class Collidable(Renderable):

    def __init__(self, game: "PyCrypts", room: "Room"):
        super().__init__(game)
        self.room = room

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass
