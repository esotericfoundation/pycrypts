from tickable.renderable.collidable.entities.entity import Entity


class Sword(Entity):

    def __init__(self, position, size, game):
        super().__init__(position, "sword", size, game)
