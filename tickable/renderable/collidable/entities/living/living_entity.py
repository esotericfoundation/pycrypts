from tickable.renderable.collidable.entities.entity import Entity, get_entities


def get_living_entities():
    return list(filter(lambda entity: isinstance(entity, LivingEntity), get_entities()))


class LivingEntity(Entity):

    def __init__(self, position: tuple[int, int], character: str, size: int, health: int, game: "Game"):
        super().__init__(position, "living/" + character, size, game)

        self.health = health
        self.max_health = health

    def damage(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        self.unload()

    def attack(self):
        pass

    def attack_entity(self, entity: "LivingEntity"):
        pass

    def is_alive(self):
        return self.health > 0
