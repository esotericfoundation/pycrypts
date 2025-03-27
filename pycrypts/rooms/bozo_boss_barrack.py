from typing import TYPE_CHECKING

from pygame import Vector2

from .room import Room
from ..tickable.renderable.collidable.walls.wall import Wall

if TYPE_CHECKING:
    from ..game import PyCrypts


class BozoBossBarrack(Room):
    def __init__(self, game: "PyCrypts"):
        spawn_1 = Vector2(150, game.height / 2 - 150)
        spawn_2 = Vector2(150, game.height / 2 + 150)

        super().__init__(spawn_1, spawn_2, game, 0.5)

    def create(self):
        super().create()

        top_border = Wall(self.game.top_left, self.game.top_right + (0, 50), self.game, self, True)
        bottom_border = Wall(self.game.bottom_left + (0, -50), self.game.bottom_right, self.game, self, True)

        Wall(top_border.get_bottom_left(), bottom_border.top_left + (50, 0), self.game, self, True)
        Wall(top_border.bottom_right + (-50, 0), bottom_border.get_top_right() + (-50, 0), self.game, self, True)
