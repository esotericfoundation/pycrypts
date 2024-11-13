import pygame
from pygame import Vector2

from game import Game
from tickable.collidable.collidable import Collidable
from tickable.collidable.entities import entity
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

        print(f"Top-left: {self.top_left}, Bottom-right: {self.bottom_right}, Width: {width}, Height: {height}")

        # for point in Wall.points:
            # pygame.draw.line(Game.screen, (255, 255, 255), point[0], point[1], 3)

        pygame.draw.rect(Game.screen, (115, 115, 115), ((Game.center - (50, 50)).x, (Game.center - (50, 50)).y, 100, 100))
        pass

    def is_colliding(self, other: Collidable) -> bool:
        if isinstance(other, Entity):
            if other.no_clip:
                return False

            points = other.get_points()

            for point in points:
                if self.contains_point(point + (other.get_radius(), other.get_radius())):
                    return True
        return False

    def contains_point(self, point: tuple[int, int] | Vector2) -> bool:
        point = Vector2(point)
        return self.top_left.x <= point.x <= self.bottom_right.x and self.top_left.y <= point.y <= self.bottom_right.y

