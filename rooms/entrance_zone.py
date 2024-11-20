from game import Game
from rooms.room import Room
from tickable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.collidable.walls.door import Door
from tickable.collidable.walls.wall import Wall


class EntranceZone(Room):

    def __init__(self):
        border_left = Wall(Game.top_left, Game.bottom_left + (40, 0))
        border_right_1 = Wall(Game.top_right + (-40, 0), Game.top_right + (0, 240))
        border_right_2 = Wall(Game.top_right + (-40, 480), Game.bottom_right)
        border_top_1 = Wall(Game.top_left, Game.top_left + (160, 40))
        border_top_2 = Wall(Game.top_left + (400, 0), Game.top_right + (0, 40))
        border_bottom = Wall(Game.bottom_left + (0, -40), Game.bottom_right)

        spawn_1 = (Game.top_right + (-200, 240))
        spawn_2 = (Game.bottom_right + (-200, -320))

        wall_1 = Wall([400, 500], [1250, 550])
        wall_2 = Wall([1000, 200], [1050, 500])
        wall_3 = Wall([775, 25], [825, 325])
        wall_4 = Wall([550, 200], [600, 500])

        entrance_door = Door(border_right_1.bottom_right - (border_right_1.get_width(), 0), border_right_2.top_left + (border_right_2.get_width(), 0), None)
        exit_door = Door(border_top_1.top_left + (border_top_1.get_width(), 0), border_top_2.bottom_right - (border_top_2.get_width(), 0), None)

        super().__init__([border_left, border_right_1, border_right_2, border_top_1, border_top_2, border_bottom, wall_1, wall_2, wall_3, wall_4], [entrance_door, exit_door], spawn_1, spawn_2, 0.5)
        pass

    def spawn_monsters(self):
        skeleton_1 = Skeleton((404, 410), 32)
        skeleton_2 = Skeleton((314, 402), 32)
        skeleton_3 = Skeleton((173, 405), 32)
        skeleton_4 = Skeleton((423, 271), 32)
        skeleton_5 = Skeleton((308, 266), 32)
        skeleton_6 = Skeleton((171, 269), 32)
        skeleton_7 = Skeleton((409, 178), 32)
        skeleton_8 = Skeleton((261, 175), 32)
        skeleton_9 = Skeleton((147, 167), 32)

        self.monsters.extend((skeleton_1, skeleton_2, skeleton_3, skeleton_4, skeleton_5, skeleton_6, skeleton_7, skeleton_8, skeleton_9))

