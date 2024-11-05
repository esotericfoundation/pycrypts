import pygame

from game import Game
from tickable.tickable import Tickable


class Text(Tickable):
    def __init__(self, text, color, size = 20):
        super().__init__()

        self.text = text
        self.color = color

        self.font = pygame.font.SysFont('Arial', size)

    def tick(self):
        self.render()
        pass

    def render(self):
        img = self.font.render(self.text, True, self.color)
        Game.screen.blit(img, (500,500))
        pass
