import random

from tickable.collidable.entities.living.living_entity import LivingEntity
from tickable.collidable.entities.living.players.player import Player


class Monster(LivingEntity):
    attack_interval = 500

    def __init__(self, position: tuple[int, int], monster: str, size: int, health: int):
        super().__init__(position, "monsters/" + monster, size, health)
        self.attack_timer = 0

    def tick(self):
        super().tick()
        self.attack_timer += 1

        if self.attack_timer == self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def attack(self):
        player_count = len(Player.players)

        if player_count == 0:
            return

        player = Player.players[random.randint(0, player_count - 1)]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity: LivingEntity):
        pass
