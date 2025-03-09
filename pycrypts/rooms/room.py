from typing import TYPE_CHECKING

from pygame import Vector2

from ..tickable.renderable.collidable.collidable import Collidable
from ..tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from ..tickable.renderable.collidable.entities.living.players.player import Player
from ..tickable.renderable.collidable.walls.wall import Wall

if TYPE_CHECKING:
    from ..game import PyCrypts


class Room:
    def __init__(self, spawn_1: Vector2, spawn_2: Vector2, game: "PyCrypts", entity_scale=1.0, movement_factor=1.0):
        game.logger.info(f"Instantiating room {type(self).__name__}")

        self.spawn_1 = spawn_1
        self.spawn_2 = spawn_2
        self.entity_scale = entity_scale
        self.movement_factor = movement_factor
        self.game = game
        self.created = False

    def create(self):
        self.game.logger.info(f"Creating room {type(self).__name__} for the first time")
        self.created = True

    def load(self):
        self.game.logger.info(f"Loading room {type(self).__name__}")

        if not self.created:
            self.create()

        self.game.current_room = self

    def get_collidables(self):
        return list(filter(lambda collidable: collidable.room == self, self.game.get_collidables()))

    def get_walls(self):
        return list(filter(lambda collidable: isinstance(collidable, Wall), self.get_collidables()))

    def get_entities(self):
        return list(filter(lambda collidable: isinstance(collidable, Collidable), self.get_collidables()))

    def get_living_entities(self):
        return list(filter(lambda collidable: isinstance(collidable, LivingEntity), self.get_entities()))

    def get_players(self):
        return list(filter(lambda collidable: isinstance(collidable, Player), self.get_living_entities()))
