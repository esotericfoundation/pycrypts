import pygame

from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.living.monsters.monster import Monster


class Zombie(Monster):
        def __init__(self, position: tuple[int, int], size: int, game: "Game"):
            super().__init__(position, "zombie", size, 100, game)

        def attack_entity(self, entity: "LivingEntity"):
            if self.position.distance_squared_to(entity.position) < 2500:
                entity.damage(20)

        def is_colliding(self, entity: Entity) -> bool:
            return super().is_colliding(entity)

        def damage(self, damage):
            super().damage(damage)

            print("Zombie taking damage!")

            sound = pygame.mixer.Sound('assets/sounds/zombie_damage.mp3')
            sound.set_volume(0.125)
            pygame.mixer.Sound.play(sound)