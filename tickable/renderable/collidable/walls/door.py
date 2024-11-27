import pygame
from pygame import Rect, Vector2

from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.living.players.player import get_players
from tickable.renderable.collidable.walls.wall import Wall


class Door(Wall):
    def __init__(self, top_left: [int, int], bottom_right: tuple[int, int], destination: "Room", spawns: (Vector2, Vector2), game: "Game"):
        self.destination = destination
        self.__spawns = spawns
        self.game = game

        super().__init__(top_left, bottom_right, game)

    def get_spawns(self):
        return self.__spawns

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        pygame.draw.rect(self.game.screen, (140, 65, 5), Rect(self.top_left, (width, height)))
        pass

    def on_players_enter(self):
        if self.destination is not None:
            players = get_players()
            i = 0

            for player in players:
                i += 1
                if i == 1:
                    player.position = Vector2(self.get_spawns()[0])
                else:
                    player.position = Vector2(self.get_spawns()[1])

                player.set_scale(self.destination.entity_scale)

            self.game.current_room.unload()
            self.destination.load()

    def tick(self):
        super().tick()

        all_players_ready = True

        players = get_players()

        if len(players) == 0:
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