from typing import TYPE_CHECKING

from .ai.goals.blast_bozos_balls import BlastBozosBallsGoal
from .......rooms.room import Room
from .monster import Monster

if TYPE_CHECKING:
    from .......game import PyCrypts


class Bozo(Monster):

    def __init__(self, position: tuple[int, int], game: "PyCrypts", room: "Room"):
        super().__init__(game, room, position, "bozo", 70, 600)

    def register_goals(self):
        self.goals.append(BlastBozosBallsGoal(self, 1, self.game))
