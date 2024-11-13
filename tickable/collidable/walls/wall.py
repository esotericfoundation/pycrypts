import pygame
from pygame import Vector2

from game import Game
from tickable.collidable.collidable import Collidable
from tickable.collidable.entities.entity import Entity
from tickable.collidable.entities.fireball import Fireball
from tickable.tickable import Tickable
from util.get_line_circle_intersection import get_line_circle_intersection


class Wall(Collidable):

    points: list[tuple[tuple[int, int], tuple[int, int]]] = []

    def __init__(self, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        super().__init__()
        self.unload() # Not all walls should be ticked every frame.
        self.top_left = Vector2(top_left)
        self.bottom_right = Vector2(bottom_right)

    def get_center(self):
        return (self.top_left + self.bottom_right) / 2.0

    def get_width(self):
        return self.bottom_right.x - self.top_left.x

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

        # for point in Wall.points:
            # pygame.draw.line(Game.screen, (255, 255, 255), point[0], point[1], 3)

        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_left.x, self.top_left.y, width, height))
        pass

def is_colliding(self, other: Collidable) -> bool:
    if isinstance(other, Entity):
        if other.no_clip:
            return False

        # Get the top-left and bottom-right points for AABB collision
        other_top_left = other.get_top_left()
        other_bottom_right = other.get_bottom_right()

        # AABB collision check
        if (self.top_left.x < other_bottom_right.x and
                self.bottom_right.x > other_top_left.x and
                self.top_left.y < other_bottom_right.y and
                self.bottom_right.y > other_top_left.y):
            return True
    return False

