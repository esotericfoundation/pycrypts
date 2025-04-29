from typing import TYPE_CHECKING

from pygame import Vector2

from .room import Room
from ..tickable.renderable.collidable.entities.candle import Candle
from ..tickable.renderable.collidable.entities.living.monsters.zombie import Zombie
from ..tickable.renderable.collidable.entities.shield import Shield
from ..tickable.renderable.collidable.walls.brittle_wall import BrittleWall
from ..tickable.renderable.collidable.walls.door import Door
from ..tickable.renderable.collidable.entities.living.monsters.bozo import Bozo
from ..tickable.renderable.collidable.walls.wall import Wall

if TYPE_CHECKING:
    from ..game import PyCrypts


class BozoBossBarrack(Room):
    def __init__(self, game: "PyCrypts"):
        spawn = Vector2(60, game.height / 2)

        self.brittle_wall: BrittleWall | None = None

        super().__init__(game, spawn, 0.5)

    def create(self):
        super().create()

        bozo = Bozo(self.game, self, self.game.center)

        top_border = Wall(self.game.top_left, self.game.top_right + (0, 40), self.game, self, True)
        bottom_border = Wall(self.game.bottom_left + (0, -40), self.game.bottom_right, self.game, self, True)
        Wall(self.game.top_right + (-40, 0), self.game.bottom_right, self.game, self, True)

        bozo_boss_barracks_barricade = Door((0, 280), (40, 440), self.game.entrance_zone, Vector2(1150, 580), self.game, self, None, lambda: bozo.health > 0 and self.brittle_wall is not None and self.brittle_wall.is_broken())

        Wall(bozo_boss_barracks_barricade.top_left - (40, 0), bozo_boss_barracks_barricade.get_bottom_left(), self.game, self, True)

        Wall(top_border.get_bottom_left(), bozo_boss_barracks_barricade.get_top_right(), self.game, self, True)
        Wall(bozo_boss_barracks_barricade.get_bottom_left(), bottom_border.top_left + (40, 0), self.game, self, True)

        Wall(top_border.bottom_right + (-40, 0), bottom_border.get_top_right(), self.game, self, True)

        top_left_corner_block = Wall((40, 40), (80, 80), self.game, self, True)
        next_top_corner = Wall(top_left_corner_block.top_left + (320, 0), top_left_corner_block.bottom_right + (320, 0), self.game, self, True)

        Candle(self.game, self, top_left_corner_block.bottom_right + (0, -40))
        Candle(self.game, self, next_top_corner.bottom_right + (-80 + 8, -40))

        big_top_stub_right = Wall(top_left_corner_block.top_left + (440, 0), top_left_corner_block.bottom_right + (440, 0), self.game, self, True)
        top_right_corner_block = Wall(top_left_corner_block.top_left + (1160, 0), top_left_corner_block.bottom_right + (1160, 0), self.game, self, True)

        # Pillars
        Wall(big_top_stub_right.bottom_right + (80, 120), big_top_stub_right.bottom_right + (120, 160), self.game, self)
        Wall(top_right_corner_block.get_bottom_left() + (-120, 120), top_right_corner_block.get_bottom_left() + (-80, 160), self.game, self)

        Candle(self.game, self, big_top_stub_right.bottom_right + (0, -40))
        Candle(self.game, self, top_right_corner_block.get_bottom_left() + (-40 + 8, -40))

        bottom_left_corner_block = Wall((40, 640), (80, 680), self.game, self, True)
        next_bottom_corner = Wall(bottom_left_corner_block.top_left + (320, 0), bottom_left_corner_block.bottom_right + (320, 0), self.game, self, True)

        Candle(self.game, self, bottom_left_corner_block.get_top_right() + (0, -0))
        Candle(self.game, self, next_bottom_corner.get_top_right() + (-80 + 8, -0))

        big_bottom_stub_right = Wall(bottom_left_corner_block.top_left + (440, 0), bottom_left_corner_block.bottom_right + (440, 0), self.game, self, True)
        bottom_right_corner_block = Wall(bottom_left_corner_block.top_left + (1160, 0), bottom_left_corner_block.bottom_right + (1160, 0), self.game, self, True)

        # Pillars
        Wall(big_bottom_stub_right.get_top_right() + (80, -160), big_bottom_stub_right.get_top_right() + (120, -120), self.game, self)
        Wall(bottom_right_corner_block.top_left + (-120, -160), bottom_right_corner_block.top_left + (-80, -120), self.game, self)

        Candle(self.game, self, big_bottom_stub_right.get_top_right() + (0, 0))
        Candle(self.game, self, bottom_right_corner_block.top_left + (-40 + 8, 0))

        stub_1 = Wall(next_top_corner.top_left + (40, 0), next_top_corner.bottom_right + (80, 40), self.game, self, True)
        stub_2 = Wall(next_bottom_corner.top_left + (40, -40), next_bottom_corner.bottom_right + (80, 0), self.game, self, True)

        # Middle Pillars
        Wall(big_top_stub_right.bottom_right + (240, 80), big_top_stub_right.bottom_right + (280, 120), self.game, self)
        Wall(top_right_corner_block.get_bottom_left() + (-280, 80), top_right_corner_block.get_bottom_left() + (-240, 120), self.game, self)

        Wall(big_bottom_stub_right.get_top_right() + (240, -120), big_bottom_stub_right.get_top_right() + (280, -80), self.game, self)
        Wall(bottom_right_corner_block.top_left + (-280, -120), bottom_right_corner_block.top_left + (-240, -80), self.game, self)

        guard_1 = Zombie(self.game, self, bozo_boss_barracks_barricade.top_left + (120, -80))
        guard_2 = Zombie(self.game, self, bozo_boss_barracks_barricade.bottom_right + (80, 80))

        Shield(guard_1, self.game, self)
        Shield(guard_2, self.game, self)

        self.brittle_wall = BrittleWall(stub_1.top_left + (0, 80), stub_2.bottom_right + (0, -80), [guard_1, guard_2], self.game, self)
