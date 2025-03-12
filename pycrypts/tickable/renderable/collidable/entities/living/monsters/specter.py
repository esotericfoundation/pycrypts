from typing import TYPE_CHECKING

from pygame import Vector2

from .ai.goals.random_wander import RandomWanderGoal
from .ai.goals.walk_to_target import WalkToTargetGoal
from .monster import Monster
from ..living_entity import LivingEntity
from ...entity import Entity

if TYPE_CHECKING:
    from .......game import PyCrypts
    from .......rooms.room import Room


class Specter(Monster):

    def __init__(self, position: tuple[int, int], size: int, game: "PyCrypts", room: "Room"):
        super().__init__(position, "ghost", size, 80, game, room)

        self.wander_direction = Vector2(0, 0)
        self.wander_time = 0
        self.idle_time = 0
        self.wandering = False
        self.no_clip = True

    def register_goals(self):
        self.goals.append(RandomWanderGoal(self, 1, self.game, 0.35, 2.0, 1.5, 0.35))
        self.goals.append(WalkToTargetGoal(self, 0, self.game, 0.65))

    def attack_entity(self, entity: "LivingEntity"):
        if self.position.distance_squared_to(entity.position) < (10000 * self.game.current_room.entity_scale * self.game.current_room.entity_scale):
            entity.damage(15)
            entity.velocity += (entity.position - self.position).normalize() * 80

    def sees_other(self, other: "Entity") -> bool:
        return other.position.distance_squared_to(self.position) < 500 * 500
