import pygame
from pygame import Vector2

from tickable.renderable.renderable import Renderable


class Text(Renderable):
    def __init__(self, text, location, color, game: "Game", size = 20):
        super().__init__()

        self.text = text
        self.color = color

        self.location = Vector2(location)

        self.font = pygame.font.SysFont('Arial', size)

        self.game = game

    def tick(self):
        self.render()
        pass

    def render(self):
        img = self.font.render(self.text, True, self.color)
        self.game.screen.blit(img, self.location)
        pass

    def clear(self):
        img = self.font.render(self.text, True, self.color)
        rect = img.get_rect(topleft=self.location)
        pygame.draw.rect(self.game.screen, (0, 0, 0), rect)
        pass

    def unload(self):
        self.clear()
        super().unload()
