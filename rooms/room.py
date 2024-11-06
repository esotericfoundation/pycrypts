class Room:
    def __init__(self, walls):
        self.walls = walls
        pass

    def load(self):
        for wall in self.walls:
            wall.load()

    def unload(self):
        for wall in self.walls:
            wall.unload()
