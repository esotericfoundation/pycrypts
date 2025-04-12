import random
from typing import TYPE_CHECKING

from pygame import Vector2

from .....bozos_ball import BozosBall
from ..goal import Goal
from ...monster import Monster

if TYPE_CHECKING:
    from .........game import PyCrypts


class BlastBozosBallsGoal(Goal):
    def __init__(self, owner: Monster, priority: int, game: "PyCrypts"):
        super().__init__(owner, priority, game)

    def can_use(self) -> bool:
        return True

    def tick(self):
        if random.random() > 0.05:
            return

        random_angle = random.randrange(0, 360)

        direction = Vector2(90, 90)
        direction = direction.rotate(random_angle)

        ball = BozosBall(self.game, self.owner.room, self.owner, self.owner.position, direction)
