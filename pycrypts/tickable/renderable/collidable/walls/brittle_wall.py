from typing import TYPE_CHECKING

import pygame

from .wall import Wall
from ..collidable import Collidable
from ..entities.living.monsters.monster import Monster

if TYPE_CHECKING:
    from .....game import PyCrypts


class BrittleWall(Wall):

    def __init__(self, top_left: (int, int), bottom_right: (int, int), monsters_to_defeat: list[Monster], game: "PyCrypts"):
        super().__init__(top_left, bottom_right, game)

        self.monsters_to_defeat = monsters_to_defeat
        self.broken = False

    def tick(self):
        if self.broken:
            return

        if self.is_broken():
            self.set_broken()

        return super().tick()

    def is_colliding(self, other: Collidable) -> bool:
        if self.broken:
            return False

        return super().is_colliding(other)

    def is_broken(self):
        return all(map(lambda monster: not monster.is_alive(), self.monsters_to_defeat))

    def set_broken(self):
        self.broken = True

        sound = pygame.mixer.Sound('assets/sounds/explosion.mp3')
        sound.set_volume(0.125)
        pygame.mixer.Sound.play(sound)
