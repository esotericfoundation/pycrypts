import pygame

from entities.entity import tick_all_entities
from entities.living.monsters.skeleton import Skeleton
from entities.living.players.player import Player
from enums.movement_keys import movement_keys
from game import Game

running = True

player = Player((Game.screen.get_width() / 2 + 100, Game.screen.get_height() / 2), "pro", 64, movement_keys["ARROW"], pygame.K_RSHIFT)
rizzler = Player((Game.screen.get_width() / 2 - 100, Game.screen.get_height() / 2), "rizzler", 64, movement_keys["WASD"], pygame.K_LSHIFT)

monster = Skeleton((Game.screen.get_width() / 2, Game.screen.get_height() / 2 - 100), 64)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Game.screen.fill((0, 0, 0))

    tick_all_entities()

    pygame.display.flip()

pygame.quit()
