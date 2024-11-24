from rooms.room import Room
from tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall


class EntranceZone(Room):
    def __init__(self, game: "Game"):
        border_left = Wall(game.top_left, game.bottom_left + (40, 0), game)
        border_right_1 = Wall(game.top_right + (-40, 0), game.top_right + (0, 240), game)
        border_right_2 = Wall(game.top_right + (-40, 480), game.bottom_right, game)
        border_top = Wall(game.top_left, game.top_right + (0, 40), game)
        border_bottom = Wall(game.bottom_left + (0, -40), game.bottom_right, game)

        spawn_1 = (game.top_right + (-100, 240))
        spawn_2 = (game.bottom_right + (-100, -320))

        wall_1 = Wall([200, 500], [1250, 550], game)
        wall_2 = Wall([1050, 200], [1100, 500], game)
        wall_3 = Wall([850, 25], [900, 325], game)
        wall_4 = Wall([650, 200], [700, 500], game)

        wall_5 = Wall([200, 40], [250, 550], game)

        entrance_door = Door(border_right_1.bottom_right - (border_right_1.get_width(), 0), border_right_2.top_left + (border_right_2.get_width(), 0), None, game)

        super().__init__([border_left, border_right_1, border_right_2, border_top, border_bottom, wall_1, wall_2, wall_3, wall_4, wall_5], [entrance_door], spawn_1, spawn_2, game, 0.5)
        pass

    def spawn_monsters(self):
        skeleton_1 = Skeleton((600, 400), 64, self.game)
        skeleton_2 = Skeleton((500, 400), 64, self.game)
        skeleton_3 = Skeleton((400, 400), 64, self.game)
        skeleton_4 = Skeleton((600, 300), 64, self.game)
        skeleton_5 = Skeleton((500, 300), 64, self.game)
        skeleton_6 = Skeleton((400, 300), 64, self.game)
        skeleton_7 = Skeleton((600, 200), 64, self.game)
        skeleton_8 = Skeleton((500, 200), 64, self.game)
        skeleton_9 = Skeleton((400, 200), 64, self.game)

        self.monsters.extend((skeleton_1, skeleton_2, skeleton_3, skeleton_4, skeleton_5, skeleton_6, skeleton_7, skeleton_8, skeleton_9))

