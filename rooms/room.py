from rooms.wall import Wall


class Room:
    def __init__(self, walls: list[Wall]):
        self.walls = walls
        pass

    def load(self):
        for wall in self.walls:
            wall.load()

    def unload(self):
        for wall in self.walls:
            wall.unload()
