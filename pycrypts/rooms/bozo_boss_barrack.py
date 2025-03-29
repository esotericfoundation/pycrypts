from typing import TYPE_CHECKING

from pygame import Vector2

from .room import Room
from ..tickable.renderable.collidable.entities.living.monsters.zombie import Zombie
from ..tickable.renderable.collidable.walls.brittle_wall import BrittleWall
from ..tickable.renderable.collidable.walls.door import Door
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

        bozo_boss_barracks_barricade = Door((0, 280), (40, 440), self.game.entrance_zone, Vector2(80, 360), self.game, self)

        Wall((40, 40), (80, 80), self.game, self, True)
        Wall((440, 40), (480, 80), self.game, self, True)
        Wall((360, 40), (400, 80), self.game, self, True)
        Wall(self.game.top_right + (-80, 40), self.game.top_right + (-40, 80), self.game, self, True)
        Wall((40, 640), (80, 680), self.game, self, True)
        Wall((440, 640), (480, 680), self.game, self, True)
        Wall((360, 640), (400, 680), self.game, self, True)
        Wall(self.game.top_right + (-80, 640), self.game.top_right + (-40, 680), self.game, self, True)

        stub_1 = Wall((480, 40), (560, 120), self.game, self, True)
        stub_2 = Wall((480, 600), (560, 680), self.game, self, True)

        guard_1 = Zombie(bozo_boss_barracks_barricade.top_left + (120, -80), 64, self.game, self)
        guard_2 = Zombie(bozo_boss_barracks_barricade.bottom_right + (80, 80), 64, self.game, self)

        BrittleWall(stub_1.top_left + (0, 80), stub_2.bottom_right + (0, -80), [guard_1, guard_2], self.game, self)