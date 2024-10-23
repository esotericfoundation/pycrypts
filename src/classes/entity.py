import pygame

class Entity:

    screen = None

    position = None

    image = None

    def __init__(self, screen, position, character, size):
        self.screen = screen

        self.position = position

        image = pygame.image.load("./assets/characters/" + character + ".png").convert()
        self.image = pygame.transform.scale(image, (size, size))

    def render(self):
        self.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

    def move(self):
        keys = pygame.key.get_pressed()

        distance_travelled = pygame.Vector2()

        if keys[pygame.K_w]:
            distance_travelled.y -= 1
        if keys[pygame.K_s]:
            distance_travelled.y += 1
        if keys[pygame.K_a]:
            distance_travelled.x -= 1
        if keys[pygame.K_d]:
            distance_travelled.x += 1

        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 0.15

            self.position += distance_travelled
