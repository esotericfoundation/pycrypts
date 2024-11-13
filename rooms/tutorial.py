from game import Game
from rooms.room import Room
from tickable.collidable.walls.wall import Wall


class Tutorial(Room):
    def __init__(self):
        super().__init__([Wall(Game.center - (50, 50), Game.center + (50, 50))])
        # Width = 100
        # Height = 100
