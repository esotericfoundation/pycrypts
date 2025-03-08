from typing import TYPE_CHECKING

from pygame import Vector2

if TYPE_CHECKING:
    from ..game import PyCrypts


class Room:
    def __init__(self, spawn_1: Vector2, spawn_2: Vector2, game: "PyCrypts", entity_scale=1.0, movement_factor=1.0):
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
        print(f"Creating room {self}")
        self.created = True

    def load(self):
        print("Loading room")

        if not self.created:
            self.create()

        self.game.current_room = self

        print(f"Loading {len(self.walls)} walls")

        for wall in self.walls:
            wall.load()

        print(f"Loading {len(self.doors)} doors")

        for door in self.doors:
            door.load()

        print(f"Loading {len(self.monsters)} monsters")

        for monster in self.monsters:
            if monster.health <= 0:
                self.monsters.remove(monster)
                continue

            monster.load()
            monster.set_scale(self.entity_scale)

        print(f"Loading {len(self.other_entities)} other entities")

        for other_entity in self.other_entities:
            other_entity.load()
            other_entity.set_scale(self.entity_scale)

    def unload(self):
        print("Unloading room")

        print(f"Number of walls: {len(self.walls)}")

        for wall in self.walls:
            wall.unload()

        print(f"Number of doors: {len(self.doors)}")

        for door in self.doors:
            door.unload()

        print(f"Number of monsters: {len(self.monsters)}")

        for monster in self.monsters:
            monster.unload()

        print(f"Number of other entities: {len(self.other_entities)}")

        for other_entity in self.other_entities:
            other_entity.unload()

        print("Done unloading room")

        # self.other_entities.clear()

    def spawn_monsters(self):
        pass
