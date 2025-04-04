from pygame import Vector2

from pycrypts.game import PyCrypts
from pycrypts.rooms.room import Room
from ..entity import Entity


class Projectile(Entity):

    def __init__(self, position: tuple[int, int] | Vector2, character: str, size: int, game: "PyCrypts", room: "Room", direction: Vector2):
        super().__init__(position, character, size, game, room)

        self.direction = direction

    def tick(self):
        super().tick()

        self.position += self.direction * self.game.dt
