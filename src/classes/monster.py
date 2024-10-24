from src.classes.entity import Entity


class Monster(Entity):

    def __init__(self, screen, position, monster, size):
        super().__init__(screen, position, "monsters/" + monster, size)
