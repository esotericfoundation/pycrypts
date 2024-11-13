import random

from tickable.collidable.entities.living.living_entity import LivingEntity
from tickable.collidable.entities.living.players.player import Player
from game import Game
from util.filter import filter_list


class Monster(LivingEntity):
    attack_interval = 0.5

    def __init__(self, position: tuple[int, int], monster: str, size: int, health: int):
        super().__init__(position, "monsters/" + monster, size, health)
        self.attack_timer = 0

    def tick(self):
        super().tick()
        self.attack_timer += Game.dt

        if self.attack_timer >= self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def attack(self):
        if len(Player.players) == 0:
            return

        player_list = filter_list(Player.players, self.sees_other)
        player_count = len(player_list)

        if player_count == 0:
            return

        player = player_list[random.randint(0, player_count - 1)]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity: LivingEntity):
        pass
