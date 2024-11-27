import random

import pygame
from pygame import Vector2

from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.living.monsters.monster import Monster
from tickable.renderable.collidable.entities.living.players.player import get_players


class Zombie(Monster):
        wander_cooldown = 1.0
        wander_duration = 1.5

        def __init__(self, position: tuple[int, int], size: int, game: "Game"):
            super().__init__(position, "zombie", size, 80, game)

            self.wander_direction = Vector2(0, 0)
            self.wander_time = 0
            self.idle_time = 0
            self.wandering = False

        def ai_tick(self):
            players = list(sorted(list(filter(lambda p: self.sees_other(p), get_players())), key=lambda p: self.position.distance_squared_to(p.position)))

            if len(players) > 0:
                player = players[0]
                self.move_towards(player, 0.65)
                self.wandering = False
            else:
                if self.wandering:
                    self.move_without_collision(self.wander_direction, 0.35)
                    self.wander_time += self.game.dt

                    if self.wander_time >= Zombie.wander_duration:
                        self.wandering = False
                        self.wander_time = 0
                else:
                    self.idle_time += self.game.dt

                    if self.idle_time >= Zombie.wander_cooldown:
                        self.wander_direction = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
                        self.wandering = True
                        self.idle_time = 0

        def attack_entity(self, entity: "LivingEntity"):
            if self.position.distance_squared_to(entity.position) < 10000:
                entity.damage(20)

        def damage(self, damage):
            super().damage(damage)

            print("Zombie taking damage!")

            sound = pygame.mixer.Sound('assets/sounds/zombie_damage.mp3')
            sound.set_volume(0.125)
            pygame.mixer.Sound.play(sound)