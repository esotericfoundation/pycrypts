from tickable.renderable.collidable.entities.living.players.player import get_players, Player
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall
from tickable.tickable import Tickable


class Room:
    def __init__(self, tickables: list[Tickable], spawn_1: tuple[int, int], spawn_2: [int, int], game: "Game", entity_scale=1.0):
        self.tickables = tickables
        self.entity_scale = entity_scale

        self.spawn_1 = spawn_1
        self.spawn_2 = spawn_2

        self.game = game
        pass

    def load(self):
        self.game.current_room = self

        for tickable in self.tickables:
            tickable.load()

        self.spawn_monsters()

    def unload(self):
        for tickable in self.tickables:
            if not isinstance(tickable, Player):
                print(f"Unloading tickable {tickable}")
                tickable.unload()

    def add_tickable(self, tickable):
        self.tickables.append(tickable)

        if isinstance(tickable, Player):
            players = get_players()
            if tickable == players[0]:
                tickable.position = self.spawn_1
            elif tickable == players[1]:
                tickable.position = self.spawn_2

    def remove_tickable(self, tickable):
        if tickable in self.tickables:
            self.tickables.remove(tickable)

    def spawn_monsters(self):
        pass

    def get_walls(self):
        return list(filter(lambda tickable: isinstance(tickable, Wall), self.tickables))

    def get_doors(self):
        return list(filter(lambda wall: isinstance(wall, Door), self.get_walls()))
