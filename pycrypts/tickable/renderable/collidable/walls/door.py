from typing import TYPE_CHECKING

import pygame
from pygame import Rect, Vector2

from .wall import Wall
from ..collidable import Collidable

if TYPE_CHECKING:
    from .....game import PyCrypts
    from .....rooms.room import Room


class Door(Wall):
    def __init__(self, top_left: [int, int], bottom_right: tuple[int, int], destination: "Room", spawn: Vector2 | None, game: "PyCrypts", room: "Room"):
        self.destination = destination
        self.spawn = spawn
        self.game = game

        super().__init__(top_left, bottom_right, game, room)

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        in_door = False
        for living in self.room.get_living_entities():
            if self.is_in_door(living):
                in_door = True
                break

        if in_door:
            transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
            transparent_surface.fill((140, 65, 5, 224))
            self.game.screen.blit(transparent_surface, self.top_left)
        else:
            pygame.draw.rect(self.game.screen, (140, 65, 5), Rect(self.top_left, (width, height)))

    def on_players_enter(self):
        if self.destination is None:
            return

        players = self.game.players

        for player in players:
            self.game.logger.info(f"Sending {player} to {self.destination} at {self.spawn}")

            player.position = Vector2(self.spawn) + (player.size, player.size) # Clone the vector.
            player.set_scale(self.destination.scale)
            player.room = self.destination

        self.destination.load()

    def tick(self):
        super().tick()

        players = self.game.players

        if len(players) == 0:
            return

        for player in players:
            if not self.is_in_door(player):
                return

        self.on_players_enter()

    def is_colliding(self, other: Collidable) -> bool:
        return False

    def is_in_door(self, other: Collidable) -> bool:
        return super().is_colliding(other)
