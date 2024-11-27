import random

import pygame
from pygame import Vector2

from tickable.renderable.collidable.entities.living.monsters.ai.goals.random_wander import RandomWanderGoal
from tickable.renderable.collidable.entities.living.monsters.ai.goals.walk_to_target import WalkToTargetGoal
from tickable.renderable.collidable.entities.living.monsters.monster import Monster


class Zombie(Monster):
        wander_cooldown = 2.0
        wander_duration = 1.5
        randomness = 0.35

        def __init__(self, position: tuple[int, int], size: int, game: "Game"):
            super().__init__(position, "zombie", size, 80, game)

            self.wander_direction = Vector2(0, 0)
            self.wander_time = 0
            self.idle_time = 0
            self.wandering = False

        def register_goals(self):
            self.goals.append(RandomWanderGoal(
                self, 1, self.game, 0.35, Zombie.wander_duration, Zombie.wander_cooldown, Zombie.randomness))
            self.goals.append(WalkToTargetGoal(
                self, 0, self.game, 0.65))

        def attack_entity(self, entity: "LivingEntity"):
            if self.position.distance_squared_to(entity.position) < 10000:
                entity.damage(20)
                entity.velocity += (entity.position - self.position).normalize() * 8

        def damage(self, damage):
            super().damage(damage)

            if not self.is_alive():
                return

            sound = pygame.mixer.Sound('assets/sounds/zombie_damage.mp3')
            sound.set_volume(0.125)
            pygame.mixer.Sound.play(sound)

        def die(self):
            super().die()

            sound = pygame.mixer.Sound('assets/sounds/zombie_death.mp3')
            sound.set_volume(0.125)
            pygame.mixer.Sound.play(sound)