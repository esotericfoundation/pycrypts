from tickable.collidable.entities.entity import Entity


class LivingEntity(Entity):

    def __init__(self, position: tuple[int, int], character: str, size: int, health: int):
        super().__init__(position, "living/" + character, size)

        self.health = health
        self.max_health = health

    def damage(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.remove()

    def attack(self):
        pass

    def attack_entity(self, entity: "LivingEntity"):
        pass
