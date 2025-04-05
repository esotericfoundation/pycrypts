import math
import random
from typing import TYPE_CHECKING

from .....bozos_ball import BozosBall
from ..goal import Goal
from ...monster import Monster

if TYPE_CHECKING:
    from .........game import PyCrypts


class BlastBozosBallsGoal(Goal):
    def __init__(self, owner: Monster, priority: int, game: "PyCrypts"):
        super().__init__(owner, priority, game)

    def tick(self):
        random_angle = math.radians(random.randrange(0, 360))

        ball = BozosBall(self.game, self.owner.room, self.owner.position)
