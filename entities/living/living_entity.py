from entities.entity import Entity


class LivingEntity(Entity):
    def __init__(self, screen, position, character, size):
        super().__init__(screen, position, "living/" + character, size)
