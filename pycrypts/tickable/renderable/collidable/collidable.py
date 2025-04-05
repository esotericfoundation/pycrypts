from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....rooms.room import Room


class Collidable:

    def __init__(self, room: "Room"):
        self.room = room
        self.no_clip = False
        self.very_clip = False

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass

    def __str__(self) -> str:
        return f"{type(self).__name__} in room {self.room}"
