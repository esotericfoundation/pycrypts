from typing import TYPE_CHECKING

from pygame import Vector2

from .room import Room
from ..tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from ..tickable.renderable.collidable.entities.living.monsters.specter import Specter
from ..tickable.renderable.collidable.entities.living.monsters.zombie import Zombie
from ..tickable.renderable.collidable.entities.traps.saw_trap import SawTrap
from ..tickable.renderable.collidable.walls.brittle_wall import BrittleWall
from ..tickable.renderable.collidable.walls.door import Door
from ..tickable.renderable.collidable.walls.wall import Wall

if TYPE_CHECKING:
    from ..game import PyCrypts


class EntranceZone(Room):
    entity_scale = 0.5
    movement_factor = 0.65

    def __init__(self, game: "PyCrypts"):
        spawn_1 = Vector2(game.top_right + (-100, 240))
        spawn_2 = Vector2(game.bottom_right + (-100, -320))

        self.monsters_to_defeat = []

        super().__init__(spawn_1, spawn_2, game, EntranceZone.entity_scale, EntranceZone.movement_factor)

    def create(self):
        super().create()

        skeleton_1 = Skeleton((525, 375), 64, self.game, self)
        skeleton_2 = Skeleton((450, 375), 64, self.game, self)
        skeleton_3 = Skeleton((375, 375), 64, self.game, self)
        skeleton_4 = Skeleton((525, 275), 64, self.game, self)
        skeleton_5 = Skeleton((450, 275), 64, self.game, self)
        skeleton_6 = Skeleton((375, 275), 64, self.game, self)
        skeleton_7 = Skeleton((525, 175), 64, self.game, self)
        skeleton_8 = Skeleton((450, 175), 64, self.game, self)
        skeleton_9 = Skeleton((375, 175), 64, self.game, self)

        self.monsters_to_defeat.extend([skeleton_1, skeleton_2, skeleton_3, skeleton_4, skeleton_5, skeleton_6, skeleton_7, skeleton_8, skeleton_9])

        Zombie((900, 400), 64, self.game, self)
        Zombie((1000, 400), 64, self.game, self)

        Specter((200, 600), 64, self.game, self)

        SawTrap(Vector2(325, 450 + 32), Vector2(325, self.game.height - 95), 64, self.game, self)

        Wall(self.game.top_left, self.game.bottom_left + (50, 0), self.game, self, True)
        border_right_1 = Wall(self.game.top_right + (-50, 0), self.game.top_right + (0, 240), self.game, self, True)
        border_right_2 = Wall(self.game.top_right + (-50, 480), self.game.bottom_right, self.game, self, True)
        Wall(border_right_1.bottom_right, border_right_2.top_left + (100, 0), self.game, self, True)
        Wall(self.game.top_left, self.game.top_right + (0, 50), self.game, self, True)
        Wall(self.game.bottom_left + (0, -50), self.game.bottom_right, self.game, self, True)

        Wall((650, 500), (1250, 550), self.game, self)
        Wall((1050, 200), (1100, 500), self.game, self)
        Wall((850, 25), (900, 325), self.game, self)
        wall_4 = Wall((650, 200), (700, 500), self.game, self)
        wall_5 = BrittleWall([300, 125], [350, 375], self.monsters_to_defeat, self.game, self)
        Wall(wall_5.bottom_right + (-50, 50), wall_4.bottom_right + (0, -25), self.game, self)
        Wall(wall_5.top_left + (0, -75), wall_5.bottom_right + (0, -250), self.game, self)
        Wall(wall_5.top_left + (0, 250), wall_5.bottom_right + (0, 50), self.game, self)

        Door(
            self.game.top_right + (-50, 240),
            self.game.top_right + (0, 480),
            self.game.surface_zone,
            (Vector2(150, 150), Vector2(250, 150)),
            self.game, self)
