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
        self.game.logger.debug(f"Loading tickable {type(self).__name__}")
        self.game.tickables.append(self)

    def unload(self):
        self.game.logger.debug(f"Unloading tickable {type(self).__name__}")
        if self in self.game.tickables:
            self.game.logger.debug(f"Successfully unloaded tickable {type(self).__name__}")
            self.game.tickables.remove(self)
        else:
            self.game.logger.debug(f"Failed to unload tickable {type(self).__name__}")
