from tickable.collidable.entities.entity import Entity
from tickable.collidable.entities.living.players.player import Player
from tickable.collidable.walls.door import Door
from tickable.collidable.walls.wall import Wall

from game import Game


class Room:
    def __init__(self, walls: list[Wall], doors: list[Door], spawn_1: tuple[int, int], spawn_2: [int, int], entity_scale=1.0):
        self.walls = walls
        self.doors = doors
        self.monsters = []
        self.spawn_1 = spawn_1
        self.spawn_2 = spawn_2
        self.entity_scale = entity_scale
        pass

    def load(self):
        for wall in self.walls:
            wall.load()

        for door in self.doors:
            door.load()

        Player.players[0].position = self.spawn_1
        Player.players[1].position = self.spawn_2

        self.spawn_monsters()

        Game.current_room = self

    def unload(self):
        for wall in self.walls:
            wall.unload()

        for door in self.doors:
            door.unload()

        for monster in self.monsters:
            if monster in Entity.entities:
                monster.remove()

    def spawn_monsters(self):
        pass
