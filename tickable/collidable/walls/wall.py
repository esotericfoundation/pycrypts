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

        # for point in Wall.points:
            # pygame.draw.line(Game.screen, (255, 255, 255), point[0], point[1], 3)

        pygame.draw.rect(Game.screen, (115, 115, 115), (self.top_left.x, self.top_left.y, width, height))
        pass

    def get_borders(self):
        a_1, b_1, c_1 = 0, 1, self.top_left.y
        a_2, b_2, c_2 = 1, 0, self.bottom_right.x
        a_3, b_3, c_3 = 0, 1, self.bottom_right.y
        a_4, b_4, c_4 = 1, 0, self.top_left.x

        return (a_1, b_1, c_1), (a_2, b_2, c_2), (a_3, b_3, c_3), (a_4, b_4, c_4)

    def is_on_wall_border(self, point: tuple[int, int]) -> bool:
        point = Vector2(point)

        is_on_wall_1 = point.y == self.top_left.y and self.top_left.x <= point.x <= self.bottom_right.x
        is_on_wall_2 = point.x == self.bottom_right.x and self.top_left.y <= point.y <= self.bottom_right.y
        is_on_wall_3 = point.y == self.bottom_right.y and self.top_left.x <= point.x <= self.bottom_right.x
        is_on_wall_4 = point.x == self.top_left.x and self.top_left.y <= point.y <= self.bottom_right.y

        return is_on_wall_1 or is_on_wall_2 or is_on_wall_3 or is_on_wall_4

    def is_colliding(self, other: Collidable) -> bool:
        # If the other collidable is an Entity, use axis-aligned bounding box (AABB) collision detection
        if isinstance(other, Entity):
            if other.no_clip:
                return False

            other_top_left = Vector2(other.get_top_left())
            other_bottom_right = Vector2(other.get_bottom_right())

            # Check for overlap using AABB (Axis-Aligned Bounding Box) detection
            if (self.top_left.x < other_bottom_right.x and
                    self.bottom_right.x > other_top_left.x and
                    self.top_left.y < other_bottom_right.y and
                    self.bottom_right.y > other_top_left.y):
                return True

        # If the other collidable is a Fireball, treat it as a circle and use manual line-circle intersection checks
        elif isinstance(other, Fireball):
            fireball_center = other.get_center()
            fireball_radius = other.get_radius()

            # Define the four borders of the wall as line segments
            borders = [
                (self.top_left, Vector2(self.bottom_right.x, self.top_left.y)),  # Top border
                (Vector2(self.bottom_right.x, self.top_left.y), self.bottom_right),  # Right border
                (self.bottom_right, Vector2(self.top_left.x, self.bottom_right.y)),  # Bottom border
                (Vector2(self.top_left.x, self.bottom_right.y), self.top_left)  # Left border
            ]

            for start, end in borders:
                # Calculate the closest point on the line segment to the circle center
                line_vec = end - start
                point_vec = fireball_center - start
                line_len_sq = line_vec.length_squared()  # Square of the line length

                # Project point_vec onto line_vec, but clamp between 0 and line_len_sq
                t = max(0, min(1, point_vec.dot(line_vec) / line_len_sq))
                closest_point = start + t * line_vec  # Closest point on the line segment

                # Calculate distance from closest point to the circle center
                distance_sq = (fireball_center - closest_point).length_squared()

                # If the distance is less than or equal to the radius squared, there's a collision
                if distance_sq <= fireball_radius ** 2:
                    return True

        # No collision detected
        return False
