from pygame import Vector2

from entities.entity import Entity
from entities.living.living_entity import LivingEntity

class Fireball(Entity):

    def __init__(self, target, screen, position, size):
        super().__init__(screen, position, "fireball", size)
        self.target = target

    def move(self):
        distance = Vector2(self.target) - self.position
        if distance.magnitude_squared() < 0.05:
            self.remove()
            return
        movement = distance.normalize() * 0.5
        self.move_without_collision(movement)

    def is_colliding(self, entity):
        from entities.living.monsters.skeleton import Skeleton
        if isinstance(entity, Skeleton) or isinstance(entity, Fireball):
            return False

        is_colliding = super().is_colliding(entity)

        if is_colliding:
            if isinstance(entity, LivingEntity):
                entity.damage(10)
                self.remove()
                return False

            return True

        return False
