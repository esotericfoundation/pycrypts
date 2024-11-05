import pygame
from pygame import Vector2

from game import Game
from tickable.tickable import Tickable


class Text(Tickable):
    def __init__(self, text, location, color, size = 20):
        super().__init__()

        self.text = text
        self.color = color

        self.location = Vector2(location)

        self.font = pygame.font.SysFont('Arial', size)

    def tick(self):
        self.render()
        pass

    def render(self):
        img = self.font.render(self.text, True, self.color)
        Game.screen.blit(img, self.location)
        pass
