import math
from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .text import Text
from ..collidable.entities.living.living_entity import LivingEntity
from ..renderable import Renderable

if TYPE_CHECKING:
    from ....game import PyCrypts


class HealthBar(Renderable):

    def __init__(self, entity: LivingEntity, top_left: (int, int) or Vector2, width: int, height: int, game: "PyCrypts"):
        super().__init__(game)
        self.entity = entity

        self.top_left = top_left
        self.width = width
        self.height = height

        self.game = game

        self.top_left = Vector2(top_left)

        self.text = Text(game, (self.top_left.x + 5, self.top_left.y), str(math.ceil(entity.health)), (160, 0, 0), 35)

    def load(self):
        super().load()
        self.game.gui.append(self)

    def render(self):
        self.text.text = str(math.ceil(self.entity.health))

        pygame.draw.rect(self.game.screen, (115, 115, 115), (self.top_left.x - 5, self.top_left.y - 5, self.width + 10, self.height + 10))
        pygame.draw.rect(self.game.screen, (200, 50, 50), (self.top_left.x, self.top_left.y, self.width * (self.entity.health / self.entity.max_health), self.height))

        self.text.render()

    def unload(self):
        super().unload()
        self.text.unload()
        self.game.gui.remove(self)
