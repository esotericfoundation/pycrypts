import pygame
from pygame import Rect

from game import Game
from tickable.collidable.collidable import Collidable
from tickable.collidable.entities.living.players.player import Player
from tickable.collidable.walls.wall import Wall


class Door(Wall):
    def __init__(self, top_left: [int, int], bottom_right: tuple[int, int], destination: "Room"):
        super().__init__(top_left, bottom_right)

        self.destination = destination

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        pygame.draw.rect(Game.screen, (140, 65, 5), Rect(self.top_left, (width, height)))
        pass

    def on_players_enter(self):
        print("Entering next room")
        if self.destination is not None:
            Game.current_room.unload()
            self.destination.load()

    def tick(self):
        super().tick()

        all_players_ready = True

        if len(Player.players) == 0:
            return

        for player in Player.players:
            if not self.is_in_door(player):
                all_players_ready = False

        if all_players_ready:
            self.on_players_enter()

    def is_in_door(self, player: Player) -> bool:
        return super().is_colliding(player)

    def is_colliding(self, other: Collidable) -> bool:
        return False
