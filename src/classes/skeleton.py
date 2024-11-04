from src.classes.monster import Monster
from src.classes.fireball import Fireball

class Skeleton(Monster):

    def __init__(self, screen, position, size):
        super().__init__(screen, position, "skeleton", size)

    def attack_entity(self, entity):
        Fireball(entity, self.screen, self.position, 32)
