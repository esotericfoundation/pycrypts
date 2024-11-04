import pygame

from entities.entity import Entity
from entities.fireball import Fireball
from entities.living.living_entity import LivingEntity
from entities.living.monsters.monster import Monster


class Skeleton(Monster):

    def __init__(self, position: tuple[int, int], size: int):
        super().__init__(position, "skeleton", size, 250)

    def attack_entity(self, entity: LivingEntity):
        Fireball((entity.position.x, entity.position.y), (self.position.x, self.position.y), 32)

    def is_colliding(self, entity: Entity) -> bool:
        if isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)

    def damage(self, damage):
        super().damage(damage)

        sound = pygame.mixer.Sound('assets/sounds/skeleton_damage.mp3')
        sound.set_volume(0.125)
        pygame.mixer.Sound.play(sound)
