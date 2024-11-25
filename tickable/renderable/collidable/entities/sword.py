from tickable.renderable.collidable.entities.entity import Entity


class Sword(Entity):

    def __init__(self, target, position, size, game):
        super().__init__(position, "sword", size, game)
        self.target = target
