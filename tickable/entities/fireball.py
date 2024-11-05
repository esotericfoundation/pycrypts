from pygame import Vector2

from tickable.entities.entity import Entity
from tickable.entities.living.living_entity import LivingEntity


class Fireball(Entity):

    def __init__(self, target: tuple[int, int], position: tuple[int, int], size: int):
        super().__init__(position, "fireball", size)
        self.target = Vector2(target)

    def move(self):
        distance = self.target - self.position
        if distance.magnitude_squared() < 0.05:
            self.remove()
            return
        movement = distance.normalize() * 0.5
        self.move_without_collision(movement)

    def is_colliding(self, entity: Entity) -> bool:
        from tickable.entities.living.monsters.skeleton import Skeleton
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
