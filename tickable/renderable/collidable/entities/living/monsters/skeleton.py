import pygame

from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.fireball import Fireball
from tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from tickable.renderable.collidable.entities.living.monsters.monster import Monster


class Skeleton(Monster):

    def __init__(self, position: tuple[int, int], size: int, game: "Game"):
        super().__init__(position, "skeleton", size, 250, game)

    def attack_entity(self, entity: LivingEntity):
        Fireball((entity.position.x, entity.position.y), (self.position.x, self.position.y), 32, self.game)

    def is_colliding(self, entity: Entity) -> bool:
        if isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)

    def damage(self, damage):
        super().damage(damage)

        print("Skeleton taking damage!")

        sound = pygame.mixer.Sound('assets/sounds/skeleton_damage.mp3')
        sound.set_volume(0.125)
        pygame.mixer.Sound.play(sound)
