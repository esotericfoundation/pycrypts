import pygame
from pygame import Vector2

from game import Game

from tickable.entities.living.living_entity import LivingEntity
from tickable.text import Text
from tickable.tickable import Tickable


class HealthBar(Tickable):

    def __init__(self, entity: LivingEntity, top_left_x: int, top_left_y: int, width: int, height: int):
        super().__init__()
        self.entity = entity

        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

        self.text = Text(str(entity.health), (top_left_x + 5, top_left_y) , (160, 0, 0), 35)

    def tick(self):
        self.render()

    def render(self):
        self.text.text = str(self.entity.health)

        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_left_x - 5, self.top_left_y - 5, self.width + 10, self.height + 10))
        pygame.draw.rect(Game.screen, (200, 50, 50), (self.top_left_x, self.top_left_y, self.width * (self.entity.health / self.entity.max_health), self.height))

        self.text.render()
