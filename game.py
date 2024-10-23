import pygame
from pygame import Vector2

from src.classes.entity import Entity
from src.enums.movement_keys import movement_keys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = Entity(screen, Vector2(screen.get_width() / 2, screen.get_height() / 2), "pro", 64, movement_keys["ARROW"])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.tick()

    pygame.display.flip()

pygame.quit()
