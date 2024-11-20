class Tickable:

    tickables: list["Tickable"] = []

    def __init__(self, game: "Game"):
        self.game = game
        self.load()

    def tick(self):
        pass

    def load(self):
        Tickable.tickables.append(self)
        self.game.current_room.add_tickable(self)

    def unload(self):
        print(f"Unloading entity {self}")
        Tickable.tickables.remove(self)
        self.game.current_room.remove_tickable(self)
