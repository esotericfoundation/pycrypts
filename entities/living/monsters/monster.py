import random
from entities.living.living_entity import LivingEntity
from entities.living.players.player import Player

class Monster(LivingEntity):

    attack_interval = 500

    def __init__(self, screen, position, monster, size, health):
        super().__init__(screen, position, "monsters/" + monster, size, health)
        self.attack_timer = 0

    def tick(self):
        super().tick()
        self.attack_timer += 1

        if self.attack_timer == self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def attack(self):
        player = Player.players[random.randint(0, len(Player.players) - 1)]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity):
        pass
