import time

import pygame
from pygame import Vector2

from enums.movement_keys import movement_keys
from rooms.surface_zone import SurfaceZone
from tickable.renderable.collidable.entities.living.players.player import Player
from tickable.renderable.collidable.walls.wall import Wall
from tickable.renderable.display.health_bar import HealthBar
from tickable.tickable import Tickable

pygame.init()


def load_icon(window_name: str, icon_name: str):
    pygame.display.set_caption(window_name)

    icon = pygame.image.load(f'assets/{icon_name}.png')
    pygame.display.set_icon(icon)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        load_icon("Dungeon Crawler", "big-skeleton-face")

        self.debug = True

        self.clicked_positions: [Vector2, Vector2] = [None, None]

        self.past = time.time()
        self.dt = 0

        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.bottom_left = Vector2(0, self.height)
        self.bottom_right = Vector2(self.width, self.height)
        self.top_left = Vector2(0, 0)
        self.top_right = Vector2(self.width, 0)
        self.center = Vector2(self.width / 2, self.height / 2)

        self.current_room = None

    def init(self):
        rizzler = Player((0, 0), "rizzler", 64, movement_keys["WASD"], pygame.K_LSHIFT, self)
        player = Player((0, 0), "pro", 64, movement_keys["ARROW"], pygame.K_RSHIFT, self)

        HealthBar(rizzler, (self.screen.get_width() - 100 - 300, self.screen.get_height() - 140), 300, 40, self)
        HealthBar(player, (100, self.screen.get_height() - 140), 300, 40, self)

        surface_zone = SurfaceZone(self)
        surface_zone.load()

    def tick(self):
        present = time.time()
        self.dt = present - self.past
        self.past = present

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if self.debug and event.type == pygame.MOUSEBUTTONUP:
                self.handle_debug_mouse_click()

        self.screen.fill((0, 0, 0))

        for tickable in Tickable.tickables:
            tickable.tick()

        pygame.display.flip()
        return True

    def handle_debug_mouse_click(self):
        print("DEBUG MOUSE CLICK!")

        pos = pygame.mouse.get_pos()
        print(f'POSITION SELECTED: ({pos[0]}, {pos[1]})')

        print(f'skeleton = Skeleton(({pos[0]}, {pos[1]}), 32)')

        debug_pos_1 = self.clicked_positions[0]
        debug_pos_2 = self.clicked_positions[1]

        if debug_pos_1 is None:
            self.clicked_positions[0] = pos
            return

        if debug_pos_2 is None:
            self.clicked_positions[1] = pos
            debug_pos_2 = pos

        print(debug_pos_1)
        print(debug_pos_2)

        wall = Wall(debug_pos_1, debug_pos_2, self)
        print(wall.to_string())

        self.clicked_positions = [None, None]
