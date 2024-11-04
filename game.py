import pygame

from entities.entity import tick_all_entities
from entities.living.monsters.skeleton import Skeleton
from entities.living.players.player import Player
from enums.movement_keys import movement_keys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = Player(screen, (screen.get_width() / 2 + 100, screen.get_height() / 2), "pro", 64, movement_keys["ARROW"], pygame.K_RSHIFT)
rizzler = Player(screen, (screen.get_width() / 2 - 100, screen.get_height() / 2), "rizzler", 64, movement_keys["WASD"], pygame.K_LSHIFT)

monster = Skeleton(screen, (screen.get_width() / 2, screen.get_height() / 2 - 100), 64)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    tick_all_entities()

    pygame.display.flip()

pygame.quit()
