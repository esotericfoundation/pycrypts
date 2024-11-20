from tickable.renderable.renderable import Renderable
from tickable.tickable import Tickable


def get_collidables():
    return filter(lambda tickable: isinstance(tickable, Collidable), Tickable.tickables)


class Collidable(Renderable):

    def __init__(self):
        super().__init__()

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass

