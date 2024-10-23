import pygame

class Entity:

    position = None

    image = None

    def __init__(self, position, character, size):
        self.position = position

        image = pygame.image.load("./assets/characters/" + character + ".png").convert()
        self.image = pygame.transform.scale(image, size)
