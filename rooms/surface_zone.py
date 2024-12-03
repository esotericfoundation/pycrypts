from rooms.entrance_zone import EntranceZone
from rooms.room import Room
from tickable.renderable.collidable.entities.living.monsters.skeleton import Skeleton
from tickable.renderable.collidable.entities.living.monsters.zombie import Zombie
from tickable.renderable.collidable.walls.wall import Wall
from tickable.renderable.collidable.walls.door import Door


class SurfaceZone(Room):
    def __init__(self, game: "Game"):
        spawn_1 = (game.top_right + (-200, 240))
        spawn_2 = (game.bottom_right + (-200, -320))

        super().__init__(spawn_1, spawn_2, game)

    def create(self):
        super().create()

        self.spawn_monsters()

        border_left = Wall(self.game.top_left, self.game.bottom_left + (80, 0), self.game)
        border_right_1 = Wall(self.game.top_right + (-80, 0), self.game.top_right + (0, 240), self.game)
        border_right_2 = Wall(self.game.top_right + (-80, 480), self.game.bottom_right, self.game)
        border_right_3 = Wall(border_right_1.bottom_right, border_right_2.top_left + (160, 0), self.game)
        border_top_1 = Wall(self.game.top_left, self.game.top_left + (160, 80), self.game)
        border_top_2 = Wall(self.game.top_left + (400, 0), self.game.top_right + (0, 80), self.game)
        border_top_3 = Wall(border_top_1.bottom_right + (0, -160), border_top_2.top_left, self.game)
        border_bottom = Wall(self.game.bottom_left + (0, -80), self.game.bottom_right, self.game)

        wall_1 = Wall(self.game.top_left + (480, 0), self.game.top_left + (560, 160), self.game)
        wall_2 = Wall(self.game.top_left + (480, 320), self.game.bottom_left + (560, 0), self.game)

        entrance_door = Door(
            self.game.top_right + (-80, 240),
            self.game.top_right + (0, 480),
            None, None, self.game)

        exit_door = Door(
            self.game.top_left + (160, 0),
            self.game.top_left + (400, 80),
            self.game.entrance_zone,
            (self.game.entrance_zone.spawn_1, self.game.entrance_zone.spawn_2),
            self.game)

        self.walls.extend([border_left, border_right_1, border_right_2, border_right_3, border_top_1, border_top_2, border_top_3, border_bottom, wall_1, wall_2])
        self.doors.extend([entrance_door, exit_door])

    def spawn_monsters(self):
        skeleton_1 = Skeleton(self.game.bottom_left + (160, -200), 64, self.game)
        skeleton_2 = Zombie(self.game.bottom_left + (300, -200), 64, self.game)

        skeleton_1.unload()
        skeleton_2.unload()

        self.monsters.append(skeleton_1)
        self.monsters.append(skeleton_2)

