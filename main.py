import pygame, time

from rooms.tutorial import Tutorial
from tickable.tickable import Tickable
from tickable.collidable.entities.living.players.player import Player
from enums.movement_keys import movement_keys
from game import Game
from tickable.health_bar import HealthBar

running = True

def tick():
    present = time.time()
    Game.dt = present - Game.past
    Game.past = present

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    Game.screen.fill((0, 0, 0))

    for tickable in Tickable.tickables:
        tickable.tick()

    pygame.display.flip()

    return True


tutorial = Tutorial()

rizzler = Player(tutorial.spawn_1, "rizzler", 64, movement_keys["WASD"], pygame.K_LSHIFT)
player = Player(tutorial.spawn_2, "pro", 64, movement_keys["ARROW"], pygame.K_RSHIFT)

rizzler_health_bar = HealthBar(rizzler, Game.screen.get_width() - 100 - 300, Game.screen.get_height() - 140, 300, 40)
player_health_bar = HealthBar(player, 100, Game.screen.get_height() - 140, 300, 40)

tutorial.load()

while tick():
    pass

pygame.quit()
