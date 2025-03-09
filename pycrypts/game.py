import os
import time

import pygame
from pygame import Vector2, Surface

from .enums.movement_keys import movement_keys
from .rooms.entrance_zone import EntranceZone
from .rooms.room import Room
from .rooms.surface_zone import SurfaceZone
from .tickable.renderable.collidable.collidable import Collidable
from .tickable.renderable.collidable.entities.entity import Entity
from .tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from .tickable.renderable.collidable.entities.living.players.player import Player
from .tickable.renderable.collidable.walls.wall import Wall
from .tickable.renderable.display.health_bar import HealthBar
from .tickable.renderable.renderable import Renderable
from .tickable.tickable import Tickable


class PyCrypts:
    def __init__(self, game: pygame):
        self.pygame: pygame = game

        self.screen: Surface | None = None
        self.debug = True

        self.clicked_positions: [Vector2, Vector2] = [None, None]

        self.past = time.time()
        self.dt = 0

        self.height = None
        self.width = None
        self.bottom_left = None
        self.bottom_right = None
        self.top_left = None
        self.top_right = None
        self.center = None

        self.current_room: Room | None = None
        self.entrance_zone: Room | None = None
        self.surface_zone: Room | None = None

        self.over = False

        self.tickables: list[Tickable] = []

        self.assets: dict[str, Surface] = {}
        self.sounds: dict[str, pygame.mixer.Sound] = {}

    def load_icon(self):
        self.pygame.display.set_caption(type(self).__name__)

        icon = self.pygame.image.load(f'assets/images/icons/{type(self).__name__.lower()}.png')
        self.pygame.display.set_icon(icon)

    def init(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.pygame.init()

        self.screen = self.pygame.display.set_mode((1280, 720))
        self.load_icon()

        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.bottom_left = Vector2(0, self.height)
        self.bottom_right = Vector2(self.width, self.height)
        self.top_left = Vector2(0, 0)
        self.top_right = Vector2(self.width, 0)
        self.center = Vector2(self.width / 2, self.height / 2)

        print("Instantiating rooms")
        self.current_room = self.surface_zone = SurfaceZone(self)
        self.entrance_zone = EntranceZone(self)

        rizzler = Player((0, 0), "rizzler", 64, movement_keys["WASD"], self.pygame.K_LSHIFT, self, self.current_room)
        player = Player((0, 0), "pro", 64, movement_keys["ARROW"], self.pygame.K_RSHIFT, self, self.current_room)

        HealthBar(rizzler, (self.screen.get_width() - 100 - 300, self.screen.get_height() - 140), 300, 40, self)
        HealthBar(player, (100, self.screen.get_height() - 140), 300, 40, self)

        print("Loading starting zone")
        self.surface_zone.load()

        players = self.get_players()
        i = 0

        for player in players:
            i += 1
            if i == 1:
                player.position = self.current_room.spawn_1
            else:
                player.position = self.current_room.spawn_2
            player.set_scale(self.current_room.entity_scale)

    def tick(self):
        if not self.over:
            present = time.time()
            self.dt = present - self.past
            self.past = present

        keys = self.pygame.key.get_pressed()

        if keys[self.pygame.K_ESCAPE]:
            return False

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                return False

        self.screen.fill((0, 0, 0))

        if self.over:
            font_1 = self.pygame.font.Font(None, 150)

            text_1 = font_1.render("Game Over!", True, (255, 0, 0))
            text_1_rect = text_1.get_rect(center=self.center)

            self.screen.blit(text_1, text_1_rect)

            font_2 = self.pygame.font.Font(None, 50)

            text_2 = font_2.render("Press ESC to exit", True, (200, 0, 0))
            text_2_rect = text_2.get_rect(center=(self.center.x, self.center.y + 100))

            self.screen.blit(text_2, text_2_rect)

        if not self.over:
            for tickable in self.tickables:
                if isinstance(tickable, Collidable):
                    if tickable.room != self.current_room:
                        continue

                tickable.tick()

        self.pygame.display.flip()
        return True

    def handle_debug_mouse_click(self):
        pos = self.pygame.mouse.get_pos()
        print(f'POSITION SELECTED: ({pos[0]}, {pos[1]})')

        print(f'skeleton = Skeleton(({pos[0]}, {pos[1]}), 32)')

        debug_pos_1 = self.clicked_positions[0]
        debug_pos_2 = self.clicked_positions[1]

        if debug_pos_1 is None:
            self.clicked_positions[0] = Vector2(pos)
            return

        if debug_pos_2 is None:
            self.clicked_positions[1] = pos
            debug_pos_2 = pos

        print(debug_pos_1)
        print(debug_pos_2)

        wall = Wall(debug_pos_1, debug_pos_2, self)
        print(wall.to_string())

        self.clicked_positions = [None, None]

    def get_asset(self, key: str) -> Surface:
        asset = self.assets.get(key)

        if asset is not None:
            return asset

        try:
            asset = self.pygame.image.load(key + ".png").convert_alpha()
        except FileNotFoundError:
            asset = self.pygame.image.load(key + ".svg").convert_alpha()

        self.assets[key] = asset

        return asset

    def get_sound(self, key: str) -> pygame.mixer.Sound:
        sound = self.sounds.get(key)

        if sound is not None:
            return sound

        sound = pygame.mixer.Sound(key + ".mp3")
        sound.set_volume(0.125)

        self.sounds[key] = sound

        return sound

    def get_renderables(self):
        return list(filter(lambda tickable: isinstance(tickable, Renderable), self.tickables))

    def get_collidables(self):
        return list(filter(lambda tickable: isinstance(tickable, Collidable), self.get_renderables()))

    def get_entities(self):
        return list(filter(lambda tickable: isinstance(tickable, Entity), self.get_collidables()))

    def get_living_entities(self):
        return list(filter(lambda tickable: isinstance(tickable, LivingEntity), self.get_entities()))

    def get_players(self):
        return list(filter(lambda tickable: isinstance(tickable, Player), self.get_living_entities()))

    def get_walls(self):
        return list(filter(lambda tickable: isinstance(tickable, Wall), self.get_collidables()))

    def end(self):
        self.over = True
        self.current_room = None

    def quit(self):
        self.pygame.quit()
