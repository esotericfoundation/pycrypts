import pygame
from pygame import Vector2

from tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from tickable.renderable.display.text import Text
from tickable.renderable.renderable import Renderable


class HealthBar(Renderable):

    def __init__(self, entity: LivingEntity, top_left: (int, int) or Vector2, width: int, height: int, game: "Game"):
        super().__init__()
        self.entity = entity

        self.top_left = top_left
        self.width = width
        self.height = height

        self.game = game

        self.top_left = Vector2(top_left)

        self.text = Text(str(entity.health), (self.top_left.x + 5, self.top_left.y), (160, 0, 0), game, 35)

    def tick(self):
        self.render()

    def render(self):
        self.text.text = str(self.entity.health)

        pygame.draw.rect(self.game.screen, (115, 115, 115), (self.top_left.x - 5, self.top_left.y - 5, self.width + 10, self.height + 10))
        pygame.draw.rect(self.game.screen, (200, 50, 50), (self.top_left.x, self.top_left.y, self.width * (self.entity.health / self.entity.max_health), self.height))

        self.text.render()

    def unload(self):
        self.text.unload()
        super().unload()
