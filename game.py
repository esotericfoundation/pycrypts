import pygame
from pygame import Vector2

pygame.init()

class Game:
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    pygame.display.set_caption("Dungeon Crawler")

    icon = pygame.image.load('assets/big-skeleton-face.png')
    pygame.display.set_icon(icon)

    height = screen.get_height()
    width = screen.get_width()

    center = Vector2(width / 2, height / 2)
