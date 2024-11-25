from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.entity import Entity


class Sword(Entity):

    def __init__(self, target, position, size, game):
        super().__init__(position, "sword", size, game)
        self.target = target
        self.time_left = 0.5

    def tick(self):
        super().tick()
        self.time_left -= self.game.dt

        if self.time_left <= 0:
            self.unload()

    def is_colliding(self, entity: Collidable) -> bool:
        return False

    def is_hitting(self, entity: Collidable) -> bool:
        return super().is_colliding(entity)
