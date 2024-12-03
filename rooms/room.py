from pygame import Vector2

from tickable.renderable.collidable.entities.living.players.player import get_players
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall


class Room:
    def __init__(self, spawn_1: Vector2, spawn_2: Vector2, game: "Game", entity_scale = 1.0, movement_factor = 1.0):
        self.walls = []
        self.doors = []
        self.monsters = []
        self.spawn_1 = spawn_1
        self.spawn_2 = spawn_2
        self.entity_scale = entity_scale
        self.movement_factor = movement_factor
        self.game = game
        self.other_entities = []
        self.created = False

    def create(self):
        self.created = True

    def load(self):
        if not self.created:
            self.create()
        self.game.current_room = self

        for wall in self.walls:
            wall.load()

        for door in self.doors:
            door.load()

        for monster in self.monsters:
            if monster.health <= 0:
                self.monsters.remove(monster)
                break

            monster.load()
            monster.set_scale(self.entity_scale)

    def unload(self):
        for wall in self.walls:
            wall.unload()

        for door in self.doors:
            door.unload()

        for monster in self.monsters:
            monster.unload()

        for other_entity in self.other_entities:
            other_entity.unload()

        # self.other_entities.clear()

    def spawn_monsters(self):
        pass
