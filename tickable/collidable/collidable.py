from tickable.tickable import Tickable


class Collidable(Tickable):

    collidables: list["Collidable"] = []

    def __init__(self):
        Collidable.collidables.append(self)
        super().__init__()

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, entity) -> bool:
        pass
