import pygame

class Entity:

    screen = None

    position = None

    image = None

    def __init__(self, screen, position, character, size):
        self.screen = screen

        self.position = position

        image = pygame.image.load("./assets/characters/" + character + ".png").convert()
        self.image = pygame.transform.scale(image, size)

    def render(self):
        self.screen.blit(self.image, self.position)
