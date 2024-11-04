from src.classes.monster import Monster
from src.classes.fireball import Fireball

class Skeleton(Monster):

    def __init__(self, screen, position, size):
        super().__init__(screen, position, "skeleton", size)

    def attack_entity(self, entity):
        Fireball((entity.position.x, entity.position.y), self.screen, (self.position.x, self.position.y), 32)
