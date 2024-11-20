from tickable.renderable.collidable.entities.entity import Entity


class LivingEntity(Entity):

    def __init__(self, position: tuple[int, int], character: str, size: int, health: int, game: "Game"):
        super().__init__(position, "living/" + character, size, game)

        self.health = health
        self.max_health = health

    def damage(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.unload()

    def attack(self):
        pass

    def attack_entity(self, entity: "LivingEntity"):
        pass
