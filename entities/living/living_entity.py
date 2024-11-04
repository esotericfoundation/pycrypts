from entities.entity import Entity


class LivingEntity(Entity):

    def __init__(self, position, character, size, health):
        super().__init__(position, "living/" + character, size)

        self.health = health
        self.max_health = health

    def damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.remove()

    def attack(self):
        pass

    def attack_entity(self, entity):
        pass
