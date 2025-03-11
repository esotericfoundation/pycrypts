from typing import TYPE_CHECKING

import pygame
from pygame import Vector2

from .ai.goals.random_wander import RandomWanderGoal
from .ai.goals.strafe_to_target import StrafeToTargetGoal
from .monster import Monster

if TYPE_CHECKING:
    from .......game import PyCrypts
    from ..living_entity import LivingEntity
    from .......rooms.room import Room


class Zombie(Monster):
    wander_cooldown = 2.0
    wander_duration = 1.5
    randomness = 0.35

    def __init__(self, position: tuple[int, int], size: int, game: "PyCrypts", room: "Room"):
        super().__init__(position, "zombie", size, 80, game, room)

        self.wander_direction = Vector2(0, 0)
        self.wander_time = 0
        self.idle_time = 0
        self.wandering = False

    def register_goals(self):
        self.goals.append(RandomWanderGoal(self, 1, self.game, 0.35, Zombie.wander_duration, Zombie.wander_cooldown, Zombie.randomness))
        self.goals.append(StrafeToTargetGoal(self, 0, self.game, 0.65))

    def attack_entity(self, entity: "LivingEntity"):
        if self.position.distance_squared_to(entity.position) < (10000 * self.game.current_room.entity_scale * self.game.current_room.entity_scale):
            entity.damage(20)
            entity.velocity += (entity.position - self.position).normalize() * 40

    def damage(self, damage):
        super().damage(damage)

        sound = self.game.get_sound('zombie_damage')
        pygame.mixer.Sound.play(sound)

    def die(self):
        super().die()

        sound = self.game.get_sound('zombie_death')
        pygame.mixer.Sound.play(sound)
