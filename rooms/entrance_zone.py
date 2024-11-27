from pygame import Vector2

from rooms.room import Room
from tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.renderable.collidable.walls.brittle_wall import BrittleWall
from tickable.renderable.collidable.walls.door import Door
from tickable.renderable.collidable.walls.wall import Wall


class EntranceZone(Room):
    entity_scale = 0.5

    def __init__(self, game: "Game"):
        spawn_1 = Vector2(game.top_right + (-100, 240))
        spawn_2 = Vector2(game.bottom_right + (-100, -320))

        super().__init__(spawn_1, spawn_2, game, EntranceZone.entity_scale)

        self.skeletons = []

    def create(self):
        if self.created:
            return

        super().create()

        self.spawn_monsters()

        border_left = Wall(self.game.top_left, self.game.bottom_left + (40, 0), self.game)
        border_right_1 = Wall(self.game.top_right + (-40, 0), self.game.top_right + (0, 240), self.game)
        border_right_2 = Wall(self.game.top_right + (-40, 480), self.game.bottom_right, self.game)
        border_right_3 = Wall(border_right_1.bottom_right, border_right_2.top_left + (80, 0), self.game)
        border_top = Wall(self.game.top_left, self.game.top_right + (0, 40), self.game)
        border_bottom = Wall(self.game.bottom_left + (0, -40), self.game.bottom_right, self.game)

        wall_1 = Wall((200, 500), (1250, 550), self.game)
        wall_2 = Wall((1050, 200), (1100, 500), self.game)
        wall_3 = Wall((850, 25), (900, 325), self.game)
        wall_4 = Wall((650, 200), (700, 500), self.game)
        wall_5 = BrittleWall([200, 40], [250, 550], list(self.skeletons), self.game)

        entrance_door = Door(
            self.game.top_right + (-40, 240),
            self.game.top_right + (0, 480),
            self.game.surface_zone,
            (Vector2(150, 150), Vector2(250, 150)),
            self.game)

        self.walls.extend([border_left, border_right_1, border_right_2, border_right_3, border_top, border_bottom, wall_1, wall_2, wall_3, wall_4, wall_5])
        self.doors.append(entrance_door)

    def spawn_monsters(self):
        skeleton_1 = Skeleton((525, 400), 64, self.game)
        skeleton_2 = Skeleton((425, 400), 64, self.game)
        skeleton_3 = Skeleton((325, 400), 64, self.game)
        skeleton_4 = Skeleton((525, 300), 64, self.game)
        skeleton_5 = Skeleton((425, 300), 64, self.game)
        skeleton_6 = Skeleton((325, 300), 64, self.game)
        skeleton_7 = Skeleton((525, 200), 64, self.game)
        skeleton_8 = Skeleton((425, 200), 64, self.game)
        skeleton_9 = Skeleton((325, 200), 64, self.game)

        self.skeletons.extend([skeleton_1, skeleton_2, skeleton_3, skeleton_4, skeleton_5, skeleton_6, skeleton_7, skeleton_8, skeleton_9])
        self.monsters.extend(self.skeletons)

        for skeleton in self.skeletons:
            skeleton.unload()

