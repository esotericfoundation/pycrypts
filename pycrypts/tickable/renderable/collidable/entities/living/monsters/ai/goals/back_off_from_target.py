from typing import TYPE_CHECKING

from pycrypts.tickable.renderable.collidable.entities.living.players.player import Player
from .walk_to_target import WalkToTargetGoal
from ...monster import Monster

if TYPE_CHECKING:
    from .........game import PyCrypts


class BackOffFromTargetGoal(WalkToTargetGoal):
    def __init__(self, owner: "Monster", priority: int, game: "PyCrypts", speed=1, distance_threshold=100):
        super().__init__(owner, priority, game, speed)

        self.distance_threshold = distance_threshold
        self.is_backing_off = False

        self.threshold_squared = self.distance_threshold * self.distance_threshold
        self.entity_scale_squared = self.game.current_room.entity_scale * self.game.current_room.entity_scale

    def start(self):
        super().start()
        self.is_backing_off = True

    def tick(self):
        self.owner.move_away_from(self.cached_target, self.speed)

    def end(self):
        super().end()
        self.is_backing_off = False

    def get_nearby_targets_and_cache(self) -> Player | None:
        super().get_nearby_targets_and_cache()

        if self.cached_target is None:
            return None

        multiplier_squared = 3.24 if self.is_backing_off else 1

        is_close_enough = self.owner.position.distance_squared_to(self.cached_target.position) < self.threshold_squared * self.entity_scale_squared * multiplier_squared

        if not is_close_enough:
            return None

        return self.cached_target
