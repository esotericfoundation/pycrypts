from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.living.monsters.monster import Monster
from tickable.renderable.collidable.walls.wall import Wall


class BrittleWall(Wall):

    def __init__(self, top_left: (int, int), bottom_right: (int, int), monsters_to_defeat: list[Monster], game: "Game"):
        super().__init__(top_left, bottom_right, game)

        self.monsters_to_defeat = monsters_to_defeat
        self.broken = False

    def tick(self):
        self.broken = self.is_broken()
        if self.broken:
            return

        return super().tick()

    def is_colliding(self, other: Collidable) -> bool:
        if self.broken:
            return False

        return super().is_colliding(other)

    def is_broken(self):
        return all(map(lambda monster: not monster.is_alive(), self.monsters_to_defeat))
