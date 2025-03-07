from tickable.renderable.collidable.entities.living.monsters.ai.goals.walk_to_target import WalkToTargetGoal


class BackOffFromTargetGoal(WalkToTargetGoal):
    def __init__(self, owner, priority, game, speed = 1, distance_threshold = 100):
        super().__init__(owner, priority, game, speed)

        self.distance_threshold = distance_threshold
        self.is_backing_off = False

    def start(self):
        super().start()
        self.is_backing_off = True

    def tick(self):
        self.owner.move_away_from(self.cached_target, self.speed)

    def end(self):
        super().end()
        self.is_backing_off = False

    def can_use(self) -> bool:
        return super().can_use() and len(self.get_nearby_targets_and_cache()) > 0

    def get_nearby_targets_and_cache(self):
        targets = super().get_nearby_targets_and_cache()

        threshold_squared = self.distance_threshold * self.distance_threshold
        entity_scale_squared = self.game.current_room.entity_scale * self.game.current_room.entity_scale
        multiplier = 1

        if self.is_backing_off:
            multiplier = 1.8

        multiplier_squared = multiplier * multiplier

        nearby = list(filter(lambda p: self.owner.position.distance_squared_to(p.position) < threshold_squared * entity_scale_squared * multiplier_squared, targets))
        return nearby