from typing import TYPE_CHECKING

from .......rooms.room import Room
from .monster import Monster

if TYPE_CHECKING:
    from .......game import PyCrypts


class Bozo(Monster):

    def __init__(self, position: tuple[int, int], game: "PyCrypts", room: "Room"):
        super().__init__(position, "bozo", 70, 600, game, room)
