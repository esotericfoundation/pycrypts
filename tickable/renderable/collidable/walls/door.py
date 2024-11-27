import pygame
from pygame import Rect

from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.living.players.player import get_players
from tickable.renderable.collidable.walls.wall import Wall


class Door(Wall):
    def __init__(self, top_left: [int, int], bottom_right: tuple[int, int], destination: "Room", game: "Game"):
        super().__init__(top_left, bottom_right, game)

        self.destination = destination
        self.game = game

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        pygame.draw.rect(self.game.screen, (140, 65, 5), Rect(self.top_left, (width, height)))
        pass

    def on_players_enter(self):
        if self.destination is not None:
            self.game.current_room.unload()
            self.destination.load()

    def tick(self):
        super().tick()

        all_players_ready = True

        players = get_players()

        if players.__sizeof__() == 0:
            return

        for player in players:
            if not self.is_in_door(player):
                all_players_ready = False

        if all_players_ready:
            self.on_players_enter()

    def is_colliding(self, other: Collidable) -> bool:
        return False

    def is_in_door(self, other: Collidable) -> bool:
        return super().is_colliding(other)
