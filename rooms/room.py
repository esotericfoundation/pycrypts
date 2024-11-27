from tickable.renderable.collidable.entities.living.players.player import get_players
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall


class Room:
    def __init__(self, spawn_1: tuple[int, int], spawn_2: [int, int], game: "Game", entity_scale = 1.0):
        self.walls = []
        self.doors = []
        self.monsters = []
        self.spawn_1 = spawn_1
        self.spawn_2 = spawn_2
        self.entity_scale = entity_scale
        self.game = game
        self.other_entities = []
        pass

    def create(self):
        pass

    def load(self):
        self.create()

        for wall in self.walls:
            wall.load()

        for door in self.doors:
            door.load()

        players = get_players()

        i = 0

        for player in players:
            i += 1
            if i == 1:
                player.position = self.spawn_1
            else:
                player.position = self.spawn_2
            player.set_scale(self.entity_scale)

        self.spawn_monsters()

        for monster in self.monsters:
            monster.set_scale(self.entity_scale)

        self.game.current_room = self

    def unload(self):
        for wall in self.walls:
            wall.unload()

        for door in self.doors:
            door.unload()

        for monster in self.monsters:
            monster.unload()

        for other_entity in self.other_entities:
            other_entity.unload()

    def spawn_monsters(self):
        pass
