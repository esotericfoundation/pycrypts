import pygame
from pygame import Vector2

from game import Game
from tickable.collidable.collidable import Collidable
from tickable.tickable import Tickable


class Wall(Collidable):
    def __init__(self, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        super().__init__()
        self.unload() # Not all walls should be ticked every frame.
        self.top_left = Vector2(top_left)
        self.bottom_right = Vector2(bottom_right)

    def get_center(self):
        return (self.top_left + self.bottom_right) / 2.0

    def get_width(self):
        return self.top_left.x - self.bottom_right.x

    def get_height(self):
        return self.bottom_right.y - self.top_left.y

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

    def get_borders(self):
        a_1, b_1, c_1 = 0, 1, self.top_left.y
        a_2, b_2, c_2 = 1, 0, self.bottom_right.x
        a_3, b_3, c_3 = 0, 1, self.bottom_right.y
        a_4, b_4, c_4 = 1, 0, self.top_left.x
        return (a_1, b_1, c_1), (a_2, b_2, c_2), (a_3, b_3, c_3), (a_4, b_4, c_4)

    def is_colliding(self, other: Collidable) -> bool:
        # (x - h)^2 + (y - k)^2 = r^2
        # ax + by = c
        pass
