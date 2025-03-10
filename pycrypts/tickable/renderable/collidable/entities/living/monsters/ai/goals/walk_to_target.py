from typing import TYPE_CHECKING

from ..goal import Goal
from ...monster import Monster
from ....players.player import Player

if TYPE_CHECKING:
    from .........game import PyCrypts


class WalkToTargetGoal(Goal):
    def __init__(self, owner: Monster, priority: int, game: "PyCrypts", speed=1):
        super().__init__(owner, priority, game)

        self.speed = speed
        self.cached_target: Player | None = None

    def start(self):
        pass

    def tick(self):
        if self.owner.velocity.magnitude_squared() > 0:
            return

        self.owner.move_towards(self.cached_target, self.speed)

    def end(self):
        self.cached_target = None
        pass

    def can_use(self) -> bool:
        return super().can_use() and self.get_nearby_targets_and_cache() is not None

    def get_nearby_targets_and_cache(self) -> Player | None:
        players = list(filter(lambda p: self.owner.sees_other(p), self.game.players))

        if len(players) == 0:
            return None

        self.cached_target = min(players, key=lambda p: self.owner.position.distance_squared_to(p.position))
        return self.cached_target
