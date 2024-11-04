from pygame import Vector2

from entities.entity import Entity

class Fireball(Entity):

    def __init__(self, target, screen, position, size):
        super().__init__(screen, position, "fireball", size)
        self.target = target

    def move(self):
        distance = Vector2(self.target) - self.position
        if distance.magnitude() < 0.5:
            self.remove()
            return
        movement = distance.normalize() * 0.5
        self.move_without_collision(movement)

    def is_colliding(self, entity):
        from entities.living.monsters.skeleton import Skeleton
        if isinstance(entity, Skeleton) or isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)
