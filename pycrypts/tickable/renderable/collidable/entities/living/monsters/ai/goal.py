from typing import TYPE_CHECKING

from ..monster import Monster

if TYPE_CHECKING:
    from ........game import PyCrypts


class Goal:
    def __init__(self, owner: Monster, priority: int, game: "PyCrypts"):
        self.owner = owner
        self.priority = priority
        self.game = game

    def start(self):
        pass

    def tick(self):
        pass

    def end(self):
        pass

    def can_use(self) -> bool:
        return True
