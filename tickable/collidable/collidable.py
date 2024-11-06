from tickable.tickable import Tickable


class Collidable(Tickable):

    collidables: list["Collidable"] = []

    def __init__(self):
        super().__init__()
        Collidable.collidables.append(self)

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass

    def remove(self):
        super().remove()

        Collidable.collidables.remove(self)
