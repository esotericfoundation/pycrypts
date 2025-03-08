from typing import TYPE_CHECKING

from pycrypt.tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from pycrypt.tickable.renderable.collidable.entities.living.players.player import get_players

if TYPE_CHECKING:
    from pycrypt import PyCrypt

class Monster(LivingEntity):
    attack_interval = 1.0

    def __init__(self, position: tuple[int, int], monster: str, size: int, health: int, game: "PyCrypt"):
        super().__init__(position, "monsters/" + monster, size, health, game)
        self.attack_timer = 0
        self.game = game
        self.goals = []
        self.last_ticked_goal = None

        self.register_goals()

    def register_goals(self):
        pass

    def tick(self):
        super().tick()
        self.ai_tick()

        self.attack_timer += self.game.dt

        if self.attack_timer >= self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def ai_tick(self):
        usable_goals = list(filter(lambda g: g.can_use(), self.goals))
        if len(usable_goals) == 0:
            return

        highest_priority = list(sorted(usable_goals, key=lambda g: g.priority))[0]

        if highest_priority != self.last_ticked_goal:
            if self.last_ticked_goal is not None:
                self.last_ticked_goal.end()
            highest_priority.start()

        highest_priority.tick()
        self.last_ticked_goal = highest_priority

    def attack(self):
        players = list(filter(lambda p: self.sees_other(p), get_players()))
        player_count = len(players)

        if player_count == 0:
            return

        player = list(sorted(players, key=lambda p: self.position.distance_squared_to(p.position)))[0]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity: LivingEntity):
        pass
