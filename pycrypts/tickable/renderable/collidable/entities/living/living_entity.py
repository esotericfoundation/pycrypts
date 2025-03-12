from typing import TYPE_CHECKING

from ..entity import Entity

if TYPE_CHECKING:
    from ......game import PyCrypts
    from ......rooms.room import Room



class LivingEntity(Entity):

    def __init__(self, position: tuple[int, int], character: str, size: int, health: float, game: "PyCrypts", room: "Room"):
        super().__init__(position, "living/" + character, size, game, room)

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
