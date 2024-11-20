from rooms.entrance_zone import EntranceZone
from rooms.room import Room
from tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.renderable.collidable.walls.wall import Wall
from tickable.renderable.collidable.walls.door import Door

class Tutorial(Room):
    def __init__(self, game: "Game"):
        entrance_zone = EntranceZone(game)

        border_left = Wall(game.top_left, game.bottom_left + (80, 0), game)
        border_right_1 = Wall(game.top_right + (-80, 0), game.top_right + (0, 240), game)
        border_right_2 = Wall(game.top_right + (-80, 480), game.bottom_right, game)
        border_top_1 = Wall(game.top_left, game.top_left + (160, 80), game)
        border_top_2 = Wall(game.top_left + (400, 0), game.top_right + (0, 80), game)
        border_bottom = Wall(game.bottom_left + (0, -80), game.bottom_right, game)

        wall_1 = Wall(game.top_left + (480, 0), game.top_left + (560, 160), game)
        wall_2 = Wall(game.top_left + (480, 320), game.bottom_left + (560, 0), game)

        spawn_1 = (game.top_right + (-200, 240))
        spawn_2 = (game.bottom_right + (-200, -320))

        entrance_door = Door(border_right_1.bottom_right - (border_right_1.get_width(), 0), border_right_2.top_left + (border_right_2.get_width(), 0), None, game)
        exit_door = Door(border_top_1.top_left + (border_top_1.get_width(), 0), border_top_2.bottom_right - (border_top_2.get_width(), 0), entrance_zone, game)

        super().__init__([border_left, border_right_1, border_right_2, border_top_1, border_top_2, border_bottom, wall_1, wall_2, entrance_door, exit_door], spawn_1, spawn_2, game)

    def spawn_monsters(self):
        Skeleton(self.game.bottom_left + (160, -200), 64, self.game)
        Skeleton(self.game.bottom_left + (300, -200), 64, self.game)
