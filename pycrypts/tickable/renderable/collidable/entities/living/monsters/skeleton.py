from typing import TYPE_CHECKING

import pygame

from .ai.goals.back_off_from_target import BackOffFromTargetGoal
from .ai.goals.random_wander import RandomWanderGoal
from .ai.goals.walk_to_target import WalkToTargetGoal
from .monster import Monster
from ..living_entity import LivingEntity
from ...entity import Entity
from ...projectiles.fireball import Fireball

if TYPE_CHECKING:
    from .......game import PyCrypts
    from .......rooms.room import Room


class Skeleton(Monster):
    wander_duration = 1.5
    wander_cooldown = 1.0
    randomness = 0.35

    def __init__(self, position: tuple[int, int], size: int, game: "PyCrypts", room: "Room"):
        super().__init__(position, "skeleton", size, 50, game, room)

    def register_goals(self):
        self.goals.append(RandomWanderGoal(self, 2, self.game, 0.35, Skeleton.wander_duration, Skeleton.wander_cooldown, Skeleton.randomness))
        self.goals.append(WalkToTargetGoal(self, 1, self.game, 0.6))
        self.goals.append(BackOffFromTargetGoal(self, 0, self.game, 0.7, 200))

    def attack_entity(self, entity: LivingEntity):
        Fireball(entity.get_center(), (self.position.x, self.position.y), 32, self.game, self.room, 1.2)

    def is_colliding(self, entity: Entity) -> bool:
        if isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)

    def damage(self, damage):
        super().damage(damage)

        if not self.is_alive():
            return

        sound = self.game.get_sound("assets/sounds/skeleton_damage")
        pygame.mixer.Sound.play(sound)

    def die(self):
        super().die()

        sound = self.game.get_sound("assets/sounds/skeleton_death")
        pygame.mixer.Sound.play(sound)
