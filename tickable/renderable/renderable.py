from tickable.tickable import Tickable


class Renderable(Tickable):

    def __init__(self, game: "Game"):
        super().__init__(game)

    def render(self):
        pass
