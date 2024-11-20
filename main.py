import pygame, time

from rooms.entrance_zone import EntranceZone
from rooms.tutorial import Tutorial
from tickable.collidable.walls.wall import Wall
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

        if Game.debug and event.type == pygame.MOUSEBUTTONUP:
            print("DEBUG MOUSE CLICK!")
            pos = pygame.mouse.get_pos()
            print(f'POSITION SELECTED: ({pos[0]}, {pos[1]})')
            print(f'skeleton = Skeleton(({pos[0]}, {pos[1]}), 32)')

            debug_pos_1 = Game.clicked_positions[0]
            debug_pos_2 = Game.clicked_positions[1]

            if debug_pos_1 is None:
                Game.clicked_positions[0] = pos
                continue

            if debug_pos_2 is None:
                Game.clicked_positions[1] = pos
                debug_pos_2 = pos

            print(debug_pos_1)
            print(debug_pos_2)

            wall = Wall(debug_pos_1, debug_pos_2)
            print(wall.to_string())

            Game.clicked_positions = [None, None]

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
