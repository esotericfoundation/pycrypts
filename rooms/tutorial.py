from game import Game
from rooms.room import Room
from tickable.collidable.walls.wall import Wall


class Tutorial(Room):
    def __init__(self):
        super().__init__([Wall(Game.top_left, Game.bottom_left + (50, 0))])
