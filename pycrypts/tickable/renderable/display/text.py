from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from ..renderable import Renderable

if TYPE_CHECKING:
    from ....game import PyCrypts


class Text(Renderable):
    def __init__(self, text, location, color, game: "PyCrypts", size=20):
        super().__init__(game)

        self.text = text
        self.color = color

        self.location = Vector2(location)

        self.font = self.game.get_font(('Arial', size))

        self.game = game

    def render(self):
        img = self.font.render(self.text, True, self.color)
        self.game.screen.blit(img, self.location)

    def clear(self):
        img = self.font.render(self.text, True, self.color)
        rect = img.get_rect(topleft=self.location)
        pygame.draw.rect(self.game.screen, (0, 0, 0), rect)

    def unload(self):
        self.clear()
        super().unload()
