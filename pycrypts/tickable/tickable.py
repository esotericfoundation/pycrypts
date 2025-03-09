from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import PyCrypts


class Tickable:
    def __init__(self, game: "PyCrypts"):
        self.game = game
        self.load()

    def tick(self):
        pass

    def load(self):
        self.game.tickables.append(self)

    def unload(self):
        print(f"Unloading tickable {self}")
        if self in self.game.tickables:
            print(f"Successfully unloaded tickable {self}")
            self.game.tickables.remove(self)
        else:
            print(f"Failed to unload tickable {self}")
