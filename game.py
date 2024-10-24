import pygame
from pygame import Vector2

from src.classes.monster import Monster
from src.classes.player import Player
from src.enums.movement_keys import movement_keys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = Player(screen, Vector2(screen.get_width() / 2 + 100, screen.get_height() / 2), "pro", 64, movement_keys["ARROW"])
rizzler = Player(screen, Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2), "rizzler", 64, movement_keys["WASD"])

monster = Monster(screen, Vector2(screen.get_width() / 2, screen.get_height() / 2 - 100), "skeleton", 64)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    rizzler.tick()
    player.tick()
    monster.tick()

    pygame.display.flip()

pygame.quit()
