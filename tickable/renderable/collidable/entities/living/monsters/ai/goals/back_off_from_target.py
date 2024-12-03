from tickable.renderable.collidable.entities.living.monsters.ai.goals.walk_to_target import WalkToTargetGoal


class BackOffFromTargetGoal(WalkToTargetGoal):
    def __init__(self, owner, priority, game, speed = 1, distance_threshold = 100):
        super().__init__(owner, priority, game, speed)

        self.distance_threshold = distance_threshold

    def tick(self):
        self.owner.move_away_from(self.cached_target, self.speed)

    def can_use(self) -> bool:
        return super().can_use() and len(self.get_nearby_targets_and_cache()) > 0

    def get_nearby_targets_and_cache(self):
        targets = super().get_nearby_targets_and_cache()
        nearby = list(filter(lambda p: self.owner.position.distance_squared_to(p.position) < self.distance_threshold * self.distance_threshold * self.game.current_room.entity_scale * self.game.current_room.entity_scale, targets))

        return nearby