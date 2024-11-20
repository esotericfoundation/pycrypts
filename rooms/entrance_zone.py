from rooms.room import Room
from tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall


class EntranceZone(Room):
    def __init__(self, game: "Game"):
        border_left = Wall(game.top_left, game.bottom_left + (40, 0), game)
        border_right_1 = Wall(game.top_right + (-40, 0), game.top_right + (0, 240), game)
        border_right_2 = Wall(game.top_right + (-40, 480), game.bottom_right, game)
        border_top_1 = Wall(game.top_left, game.top_left + (160, 40), game)
        border_top_2 = Wall(game.top_left + (400, 0), game.top_right + (0, 40), game)
        border_bottom = Wall(game.bottom_left + (0, -40), game.bottom_right, game)

        spawn_1 = (game.top_right + (-200, 240))
        spawn_2 = (game.bottom_right + (-200, -320))

        wall_1 = Wall([400, 500], [1250, 550], game)
        wall_2 = Wall([1000, 200], [1050, 500], game)
        wall_3 = Wall([775, 25], [825, 325], game)
        wall_4 = Wall([550, 200], [600, 500], game)

        entrance_door = Door(border_right_1.bottom_right - (border_right_1.get_width(), 0), border_right_2.top_left + (border_right_2.get_width(), 0), None, game)
        exit_door = Door(border_top_1.top_left + (border_top_1.get_width(), 0), border_top_2.bottom_right - (border_top_2.get_width(), 0), None, game)

        super().__init__([border_left, border_right_1, border_right_2, border_top_1, border_top_2, border_bottom, wall_1, wall_2, wall_3, wall_4], [entrance_door, exit_door], spawn_1, spawn_2, game, 0.5)
        pass

    def spawn_monsters(self):
        skeleton_1 = Skeleton((404, 410), 64, self.game)
        skeleton_2 = Skeleton((314, 402), 64, self.game)
        skeleton_3 = Skeleton((173, 405), 64, self.game)
        skeleton_4 = Skeleton((423, 271), 64, self.game)
        skeleton_5 = Skeleton((308, 266), 64, self.game)
        skeleton_6 = Skeleton((171, 269), 64, self.game)
        skeleton_7 = Skeleton((409, 178), 64, self.game)
        skeleton_8 = Skeleton((261, 175), 64, self.game)
        skeleton_9 = Skeleton((147, 167), 64, self.game)

        self.monsters.extend((skeleton_1, skeleton_2, skeleton_3, skeleton_4, skeleton_5, skeleton_6, skeleton_7, skeleton_8, skeleton_9))

