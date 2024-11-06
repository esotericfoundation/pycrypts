import pygame
from pygame import Vector2

from game import Game
from tickable.tickable import Tickable


class Wall(Tickable):
    def __init__(self, top_right: tuple[int, int], bottom_left: tuple[int, int]):
        super().__init__()
        self.unload() # Not all walls should be ticked every frame.
        self.top_right = Vector2(top_right)
        self.bottom_left = Vector2(bottom_left)

    def tick(self):
        self.render()

    def load(self):
        Tickable.tickables.append(self)

    def unload(self):
        Tickable.tickables.remove(self)

    def render(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y

        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_right.x - width, self.bottom_left.y + height, width, height))
        pass
