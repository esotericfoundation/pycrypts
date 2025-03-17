import argparse
import os
import time
import logging

import pygame
from pygame import Vector2, Surface

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
    def __init__(self, game: pygame, log: logging, arguments: list[str] = None):
        if arguments is None:
            arguments = []

        if arguments and (arguments[0].endswith("__main__.py") or arguments[0].endswith(type(self).__name__.lower())):
            arguments = arguments[1:]

        parser = argparse.ArgumentParser()
        parser.add_argument("-l", "--log-level", type=str, choices=[level for level in logging._nameToLevel.keys()], default="INFO", help="Set logging level")

        parsed = parser.parse_args(arguments)
        log_level = getattr(logging, parsed.log_level, logging.INFO)
        log.basicConfig(level=log_level)

        self.logger = logging.getLogger(type(self).__name__)

        self.pygame: pygame = game

        self.screen: Surface | None = None

        self.past = time.time()
        self.dt = 0

        self.tickables: list[Tickable] = []
        self.gui: list[Renderable] = []
        self.players: list[Player] = []

        self.current_room: Room | None = None
        self.entrance_zone: Room | None = None
        self.surface_zone: Room | None = None

        self.over = False

        self.assets: dict[str, Surface] = {}
        self.sounds: dict[str, pygame.mixer.Sound] = {}
        self.fonts: dict[tuple[str | None, int], pygame.font.Font] = {}

        self.height = None
        self.width = None
        self.bottom_left = None
        self.bottom_right = None
        self.top_left = None
        self.top_right = None
        self.center = None

        self.fog: Surface | None = None

    def init(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.logger.info(f"Initialising {self.pygame.__name__} v{self.pygame.ver}")
        self.pygame.init()

        self.logger.info("Creating screen")
        self.screen = self.pygame.display.set_mode((1280, 720))

        self.pygame.display.set_caption(type(self).__name__)

        self.pygame.display.set_icon(self.get_asset(f"assets/images/icons/{type(self).__name__.lower()}"))

        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.bottom_left = Vector2(0, self.height)
        self.bottom_right = Vector2(self.width, self.height)
        self.top_left = Vector2(0, 0)
        self.top_right = Vector2(self.width, 0)
        self.center = Vector2(self.width / 2, self.height / 2)

        self.fog = self.pygame.Surface((self.width, self.height), self.pygame.SRCALPHA)

        self.surface_zone = SurfaceZone(self)
        self.entrance_zone = EntranceZone(self)

        self.surface_zone.load()

        pro = Player((0, 0), "pro", 64, "ARROW", self.pygame.K_RSHIFT, self, self.current_room)
        rizzler = Player((0, 0), "rizzler", 64, "WASD", self.pygame.K_LSHIFT, self, self.current_room)

        HealthBar(pro, (self.screen.get_width() - 70 - 300, self.screen.get_height() - 60), 300, 40, self)
        HealthBar(rizzler, (70, self.screen.get_height() - 60), 300, 40, self)

        i = 0

        for player in self.players:
            i += 1
            if i == 1:
                player.position = self.current_room.spawn_1
            else:
                player.position = self.current_room.spawn_2
            player.set_scale(self.current_room.entity_scale)

    def render_fog(self):
        self.fog.fill((0, 0, 0, 255))
        m = 255 / float(200)

        for player in self.players:
            for i in range(200, 1, -1):
                self.pygame.draw.circle(self.fog, (0, 0, 0, i*m), player.get_int_pos(), i)

        self.screen.blit(self.fog, (0, 0))

    def is_debug(self):
        return self.logger.level <= logging.DEBUG

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

        self.screen.fill((45, 45, 45))

        if self.over:
            font_1 = self.get_font((None, 150))

            text_1 = font_1.render("Game Over!", True, (255, 0, 0))
            text_1_rect = text_1.get_rect(center=self.center)

            self.screen.blit(text_1, text_1_rect)

            font_2 = self.get_font((None, 50))

            text_2 = font_2.render("Press ESC to exit", True, (200, 0, 0))
            text_2_rect = text_2.get_rect(center=(self.center.x, self.center.y + 100))

            self.screen.blit(text_2, text_2_rect)

        if not self.over:
            for tickable in self.tickables:
                if isinstance(tickable, Collidable):
                    if tickable.room != self.current_room:
                        continue

                tickable.tick()
            for gui in self.gui:
                gui.render()

            self.render_fog()

        self.pygame.display.flip()
        return True

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

        sound = pygame.mixer.Sound("assets/sounds/" + key + ".mp3")
        sound.set_volume(0.125)

        self.sounds[key] = sound

        return sound

    def get_font(self, key: tuple[str | None, int]) -> pygame.font.Font:
        font = self.fonts.get(key)

        if font is not None:
            return font

        font = pygame.font.SysFont(key[0], key[1])
        self.fonts[key] = font

        return font

    def get_renderables(self):
        return list(filter(lambda tickable: isinstance(tickable, Renderable), self.tickables))

    def get_collidables(self):
        return list(filter(lambda tickable: isinstance(tickable, Collidable), self.get_renderables()))

    def get_entities(self):
        return list(filter(lambda tickable: isinstance(tickable, Entity), self.get_collidables()))

    def get_living_entities(self):
        return list(filter(lambda tickable: isinstance(tickable, LivingEntity), self.get_entities()))

    def get_walls(self):
        return list(filter(lambda tickable: isinstance(tickable, Wall), self.get_collidables()))

    def end(self):
        self.logger.info("Game over!")
        self.over = True
        self.current_room = None

    def quit(self):
        self.pygame.quit()
