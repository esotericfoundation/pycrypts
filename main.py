import pygame
from tickable.entities.living.monsters.skeleton import Skeleton
from tickable.tickable import Tickable
from tickable.entities.living.players.player import Player
from enums.movement_keys import movement_keys
from game import Game
from tickable.health_bar import HealthBar

running = True

def tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    Game.screen.fill((0, 0, 0))

    for tickable in Tickable.tickables:
        tickable.tick()

    pygame.display.flip()

    return True

player = Player(Game.center + (100, 0), "pro", 64, movement_keys["ARROW"], pygame.K_RSHIFT)
rizzler = Player(Game.center - (100, 0), "rizzler", 64, movement_keys["WASD"], pygame.K_LSHIFT)

player_health_bar = HealthBar(player, 100, Game.screen.get_height() - 140, 300, 40)
rizzler_health_bar = HealthBar(rizzler, Game.screen.get_width() - 100 - 300, Game.screen.get_height() - 140, 300, 40)

monster = Skeleton(Game.center - (0, 100), 64)

while tick():
    pass

pygame.quit()
