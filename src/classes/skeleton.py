from src.classes.monster import Monster

class Skeleton(Monster):

    def __init__(self, screen, position, size):
        super().__init__(screen, position, "skeleton", size)

    def attack_entity(self, entity):
        print("Skeleton attacked entity")
