import enum

import pygame
from pygame import Vector2
from classes.entity import Entity

MovementKeys = enum.Enum("MovementKeys", ["ARROW", "WASD"])

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player = Entity(screen, Vector2(screen.get_width() / 2, screen.get_height() / 2), "pro", 64)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.tick()

    pygame.display.flip()

pygame.quit()
