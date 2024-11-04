import pygame
from entities.entity import Entity

class LivingEntity(Entity):

    def __init__(self, screen, position, character, size, health):
        super().__init__(screen, position, "living/" + character, size)

        self.health = health
        self.max_health = health

    def damage(self, damage):
        self.health -= damage

        sound = pygame.mixer.Sound('assets/sounds/damage.mp3')
        sound.set_volume(0.125)
        pygame.mixer.Sound.play(sound)

        if self.health <= 0:
            self.remove()

    def attack(self):
        pass

    def attack_entity(self, entity):
        pass
