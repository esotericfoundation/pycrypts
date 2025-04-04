from pygame import Vector2

from pycrypts.game import PyCrypts
from pycrypts.rooms.room import Room
from ..entity import Entity


class Projectile(Entity):

    def __init__(self, game: "PyCrypts", room: "Room", position: tuple[int, int] | Vector2, character: str, size: int, direction: Vector2):
        super().__init__(game, room, position, character, size)

        self.direction = direction

    def tick(self):
        super().tick()

        self.position += self.direction * self.game.dt
