from typing import TYPE_CHECKING

from ..renderable import Renderable

if TYPE_CHECKING:
    from ....game import PyCrypts
    from ....rooms.room import Room


class Collidable(Renderable):

    def __init__(self, game: "PyCrypts", room: "Room"):
        super().__init__(game)
        self.room = room
        self.no_clip = False
        self.very_clip = False

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass

    def __str__(self) -> str:
        return super().__str__() + f" in room {self.room}"
