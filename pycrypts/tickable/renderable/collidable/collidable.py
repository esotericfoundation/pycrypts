from typing import TYPE_CHECKING

from ..renderable import Renderable

if TYPE_CHECKING:
    from ....game import PyCrypts


class Collidable(Renderable):

    def __init__(self, game: "PyCrypts"):
        super().__init__(game)

    def is_inside_hitbox(self, location: tuple[int, int]) -> bool:
        pass

    def is_colliding(self, collidable: "Collidable") -> bool:
        pass
