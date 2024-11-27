import pygame
from pygame import Vector2

from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.living.monsters.monster import Monster
from tickable.renderable.collidable.entities.living.players.player import get_players


class Zombie(Monster):
        def __init__(self, position: tuple[int, int], size: int, game: "Game"):
            super().__init__(position, "zombie", size, 80, game)

        def ai_tick(self):
            players = list(sorted(list(filter(lambda p: self.sees_other(p), get_players())), key=lambda p: self.position.distance_squared_to(p.position)))
            if len(players) > 0:
                player = players[0]
                self.move_towards(player, 0.5)
            else:

        def attack_entity(self, entity: "LivingEntity"):
            if self.position.distance_squared_to(entity.position) < 10000:
                entity.damage(20)

        def damage(self, damage):
            super().damage(damage)

            print("Zombie taking damage!")

            sound = pygame.mixer.Sound('assets/sounds/zombie_damage.mp3')
            sound.set_volume(0.125)
            pygame.mixer.Sound.play(sound)