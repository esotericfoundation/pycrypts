from entities.fireball import Fireball
from entities.living.monsters.monster import Monster


class Skeleton(Monster):

    def __init__(self, screen, position, size):
        super().__init__(screen, position, "skeleton", size)

    def attack_entity(self, entity):
        Fireball((entity.position.x, entity.position.y), self.screen, (self.position.x, self.position.y), 32)

    def is_colliding(self, entity):
        if isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)
