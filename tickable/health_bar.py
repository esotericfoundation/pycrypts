import pygame
from pygame import Vector2

from game import Game

from tickable.entities.living.living_entity import LivingEntity
from tickable.tickable import Tickable


class HealthBar(Tickable):

    def __init__(self, entity: LivingEntity, top_left_x: int, top_left_y: int, width: int, height: int):
        super().__init__()
        self.entity = entity

        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def tick(self):
        self.render()

    def render(self):
        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_left_x - 5, self.top_left_y - 5, self.width + 10, self.height + 10))
        pygame.draw.rect(Game.screen, (200, 20, 20), (self.top_left_x, self.top_left_y, self.width * (self.entity.health / self.entity.max_health), self.height))
