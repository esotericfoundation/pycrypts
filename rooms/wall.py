import pygame
from pygame import Vector2

from game import Game
from tickable.tickable import Tickable


class Wall(Tickable):
    def __init__(self, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        super().__init__()
        self.unload() # Not all walls should be ticked every frame.
        self.top_left = Vector2(top_left)
        self.bottom_right = Vector2(bottom_right)

    def tick(self):
        self.render()

    def load(self):
        Tickable.tickables.append(self)

    def unload(self):
        Tickable.tickables.remove(self)

    def render(self):
        width = self.bottom_right.x - self.top_left.x
        height = self.bottom_right.y - self.top_left.y

        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_left.x, self.top_left.y, width, height))
        pass
