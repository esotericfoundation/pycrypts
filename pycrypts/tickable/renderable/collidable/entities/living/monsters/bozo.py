from typing import TYPE_CHECKING

from .ai.goals.blast_bozos_balls import BlastBozosBallsGoal
from ...bozos_ball import BozosBall
from ....collidable import Collidable
from .......rooms.room import Room
from .monster import Monster

if TYPE_CHECKING:
    from .......game import PyCrypts


class Bozo(Monster):

    def __init__(self, game: "PyCrypts", room: "Room", position: tuple[int, int]):
        super().__init__(game, room, position, "bozo", 70, 600)

    def register_goals(self):
        self.goals.append(BlastBozosBallsGoal(self, 1, self.game))

    def is_colliding(self, entity: Collidable) -> bool:
        if isinstance(entity, BozosBall):
            return False

        return super().is_colliding(entity)

    def die(self):
        super().die()

        self.game.won = True
