from typing import TYPE_CHECKING

from pygame import Vector2

from pycrypts.rooms.room import Room
from ..entity import Entity
from ...collidable import Collidable

if TYPE_CHECKING:
    from pycrypts.game import PyCrypts


class Projectile(Entity):

    def __init__(self, game: "PyCrypts", room: "Room", shooter: Entity, position: tuple[int, int] | Vector2, character: str, size: int, direction: Vector2, speed: float):
        super().__init__(game, room, position, character, size)

        self.direction = direction
        self.shooter = shooter
        self.speed = speed

    def tick(self):
        super().tick()

        if self.shooter.seen:
            return

        from ..living.players.player import Player
        threshold = Player.render_distance_squared * self.room.scale * self.room.scale

        for player in self.game.players:
            distance_squared = player.position.distance_squared_to(self.position)

            if distance_squared < threshold:
                self.shooter.seen = True
                self.game.logger.debug(f"Player {player} saw monster {self.shooter} for the first time!")
                break

    def move(self):
        self.move_without_collision(self.direction, self.speed)

    def is_colliding(self, entity: Collidable) -> bool:
        colliding = super().is_colliding(entity)

        if not colliding:
            return False

        self.on_hit(entity)
        return True

    def on_hit(self, collidable: Collidable):
        self.unload()
