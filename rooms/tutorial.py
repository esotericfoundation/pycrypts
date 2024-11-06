from game import Game
from rooms.room import Room
from rooms.wall import Wall


class Tutorial(Room):
    def __init__(self):
        super().__init__([Wall(Game.top_left + (100, 0), Game.bottom_left)])
