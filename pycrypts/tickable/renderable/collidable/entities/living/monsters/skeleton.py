from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .ai.goals.back_off_from_target import BackOffFromTargetGoal
from .ai.goals.random_wander import RandomWanderGoal
from .ai.goals.walk_to_target import WalkToTargetGoal
from .monster import Monster
from ..living_entity import LivingEntity
from ..players.player import Player
from ...entity import Entity
from ...projectiles.fireball import Fireball
from ...traps.saw_trap import SawTrap

if TYPE_CHECKING:
    from .......game import PyCrypts
    from .......rooms.room import Room


class Skeleton(Monster):
    wander_duration = 1.5
    wander_cooldown = 1.0
    randomness = 0.35

    def __init__(self, position: tuple[int, int], size: int, game: "PyCrypts", room: "Room"):
        super().__init__(position, "skeleton", size, 50, game, room, game.get_sound("skeleton_damage"), game.get_sound("skeleton_death"))

    def register_goals(self):
        self.goals.append(RandomWanderGoal(self, 3, self.game, 0.35, Skeleton.wander_duration, Skeleton.wander_cooldown, Skeleton.randomness))
        self.goals.append(WalkToTargetGoal(self, 2, self.game, Player, self.game.players, 0.6))
        self.goals.append(BackOffFromTargetGoal(self, 1, self.game, Player, self.game.players, 0.7, 200))
        self.goals.append(BackOffFromTargetGoal(self, 0, self.game, SawTrap, self.game.tickables, 0.7, 100))

    def attack_entity(self, entity: LivingEntity):
        Fireball(entity.get_center(), Vector2(self.position.x, self.position.y), 32, self.game, self.room, 1.44)

    def is_colliding(self, entity: Entity) -> bool:
        if isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)
