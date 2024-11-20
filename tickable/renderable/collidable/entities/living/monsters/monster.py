import random

from tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from tickable.renderable.collidable.entities.living.players.player import get_players

class Monster(LivingEntity):
    attack_interval = 0.5

    def __init__(self, position: tuple[int, int], monster: str, size: int, health: int, game: "Game"):
        super().__init__(position, "monsters/" + monster, size, health, game)
        self.attack_timer = 0
        self.game = game

    def tick(self):
        super().tick()
        self.attack_timer += self.game.dt

        if self.attack_timer >= self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def attack(self):
        players = list(filter(self.sees_other, get_players()))
        player_count = len(players)

        if player_count == 0:
            return

        player = players[random.randint(0, player_count - 1)]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity: LivingEntity):
        pass
