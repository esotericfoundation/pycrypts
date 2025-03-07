from pycrypt.tickable.renderable.collidable.entities.living.monsters.ai.goal import Goal
from pycrypt.tickable.renderable.collidable.entities.living.players.player import get_players


class WalkToTargetGoal(Goal):
    def __init__(self, owner, priority, game, speed = 1):
        super().__init__(owner, priority, game)

        self.speed = speed
        self.cached_target = None

    def start(self):
        pass

    def tick(self):
        if self.owner.velocity.magnitude() > 0:
            return

        self.owner.move_towards(self.cached_target, self.speed)

    def end(self):
        self.cached_target = None
        pass

    def can_use(self) -> bool:
        return super().can_use() and len(self.get_nearby_targets_and_cache()) > 0

    def get_nearby_targets_and_cache(self):
        targets = list(sorted(list(filter(lambda p: self.owner.sees_other(p), get_players())), key=lambda p: self.owner.position.distance_squared_to(p.position)))

        if len(targets) > 0:
            self.cached_target = targets[0]

        return targets