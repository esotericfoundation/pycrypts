import pygame
from pygame import Rect

from game import Game
from tickable.collidable.collidable import Collidable
from tickable.collidable.entities.living.players.player import Player
from tickable.collidable.walls.wall import Wall


class Door(Wall):
    def __init__(self, top_left: [int, int], bottom_right: tuple[int, int], destination: "Room"):
        super().__init__(top_left, bottom_right)

        self.players_in_door = []
        self.destination = destination

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        pygame.draw.rect(Game.screen, (140, 65, 5), Rect(self.top_left, (width, height)))
        pass

    def on_player_enter(self, player: Player):
        self.players_in_door.append(player)

        if len(self.players_in_door) == 2:
            Game.current_room.unload()
            self.destination.load()

    def on_player_leave(self, player: Player):
        self.players_in_door.remove(player)

    def tick(self):
        super().tick()

        for player in Player.players:
            points = player.get_points()

            for point in points:
                if self.contains_point(point + (player.get_radius(), player.get_radius())):
                    self.on_player_enter(player)
                else:
                    self.on_player_leave(player)

    def is_colliding(self, other: Collidable) -> bool:
        return False
