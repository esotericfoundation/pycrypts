from game import Game
from rooms.room import Room
from tickable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.collidable.walls.wall import Wall


class Tutorial(Room):
    def __init__(self):
        border_left = Wall(Game.top_left, Game.bottom_left + (80, 0))
        border_right_1 = Wall(Game.top_right + (-80, 0), Game.top_right + (0, 240))
        border_right_2 = Wall(Game.top_right + (-80, 480), Game.bottom_right)
        border_top_1 = Wall(Game.top_left, Game.top_left + (160, 80))
        border_top_2 = Wall(Game.top_left + (400, 0), Game.top_right + (0, 80))
        border_bottom = Wall(Game.bottom_left + (0, -80), Game.bottom_right)

        wall_1 = Wall(Game.top_left + (480, 0), Game.top_left + (560, 160))
        wall_2 = Wall(Game.top_left + (480, 320), Game.bottom_left + (560, 0))

        spawn_1 = (Game.top_right + (-200, 240))
        spawn_2 = (Game.bottom_right + (-200, -320))

        super().__init__([border_left, border_right_1, border_right_2, border_top_1, border_top_2, border_bottom, wall_1, wall_2], spawn_1, spawn_2)

    def spawn_monsters(self):
        skeleton_1 = Skeleton(Game.bottom_left + (160, -200), 64)
        skeleton_2 = Skeleton(Game.bottom_left + (300, -200), 64)

        self.monsters.append(skeleton_1)
        self.monsters.append(skeleton_2)
