from typing import TYPE_CHECKING

from pygame import Vector2

from .room import Room
from ..tickable.renderable.collidable.entities.living.monsters.zombie import Zombie
from ..tickable.renderable.collidable.walls.brittle_wall import BrittleWall
from ..tickable.renderable.collidable.walls.door import Door
from ..tickable.renderable.collidable.entities.living.monsters.bozo import Bozo
from ..tickable.renderable.collidable.walls.wall import Wall

if TYPE_CHECKING:
    from ..game import PyCrypts


class BozoBossBarrack(Room):
    def __init__(self, game: "PyCrypts"):
        spawn = Vector2(60, game.height / 2)

        super().__init__(game, spawn, 0.5)

    def create(self):
        super().create()

        top_border = Wall(self.game.top_left, self.game.top_right + (0, 40), self.game, self, True)
        bottom_border = Wall(self.game.bottom_left + (0, -40), self.game.bottom_right, self.game, self, True)
        Wall(self.game.top_right + (-40, 0), self.game.bottom_right, self.game, self, True)

        Wall(top_border.get_bottom_left(), bottom_border.top_left + (40, 0), self.game, self, True)
        Wall(top_border.bottom_right + (-40, 0), bottom_border.get_top_right() + (-50, 0), self.game, self, True)

        bozo_boss_barracks_barricade = Door((0, 280), (40, 440), self.game.entrance_zone, Vector2(80, 360), self.game, self)

        top_left_corner_block = Wall((40, 40), (80, 80), self.game, self, True)
        next_top_corner = Wall(top_left_corner_block.top_left + (320, 0), top_left_corner_block.bottom_right + (320, 0), self.game, self, True)
        Wall(top_left_corner_block.top_left + (440, 0), top_left_corner_block.bottom_right + (440, 0), self.game, self, True)
        Wall(top_left_corner_block.top_left + (1160, 0), top_left_corner_block.bottom_right + (1160, 0), self.game, self, True)
        bottom_left_corner_block = Wall((40, 640), (80, 680), self.game, self, True)
        next_bottom_corner = Wall(bottom_left_corner_block.top_left + (320, 0), bottom_left_corner_block.bottom_right + (320, 0), self.game, self, True)
        Wall(bottom_left_corner_block.top_left + (440, 0), bottom_left_corner_block.bottom_right + (440, 0), self.game, self, True)
        Wall(bottom_left_corner_block.top_left + (1160, 0), bottom_left_corner_block.bottom_right + (1160, 0), self.game, self, True)

        stub_1 = Wall(next_top_corner.top_left + (40, 0), next_top_corner.bottom_right + (80, 40), self.game, self, True)
        stub_2 = Wall(next_bottom_corner.top_left + (40, -40), next_bottom_corner.bottom_right + (80, 0), self.game, self, True)

        guard_1 = Zombie(self.game, self, bozo_boss_barracks_barricade.top_left + (120, -80), 64)
        guard_2 = Zombie(self.game, self, bozo_boss_barracks_barricade.bottom_right + (80, 80), 64)

        BrittleWall(stub_1.top_left + (0, 80), stub_2.bottom_right + (0, -80), [guard_1, guard_2], self.game, self)

        Bozo(self.game, self, self.game.center)
