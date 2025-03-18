import random
from typing import TYPE_CHECKING

from pygame import Vector2

from ..entity import Entity
from ..living.living_entity import LivingEntity

if TYPE_CHECKING:
    from ......game import PyCrypts
    from ......rooms.room import Room


class Fireball(Entity):

    def __init__(self, target: Vector2, position: Vector2, size: int, game: "PyCrypts", room: "Room", speed=1, character="fireball"):
        super().__init__(position, character, size, game, room)
        self.target = Vector2(target)
        self.direction = target - position
        self.speed = speed
        self.strong = random.randint(0, 1) == 0

    def move(self):
        self.move_without_collision(self.direction, self.speed)

    def render(self):
        super().render()

        from .arrow import Arrow
        if isinstance(self, Arrow):
            return

        position = self.get_int_position()
        x, y = position[0] - self.game.vision_radius // 4, position[1] - self.game.vision_radius // 4

        self.game.fog.blit(self.game.small_vision_texture, (x, y), special_flags=self.game.pygame.BLEND_RGBA_MIN)

    def is_colliding(self, entity: Entity) -> bool:
        if isinstance(entity, Entity) and entity.no_clip:
            return False

        from ..living.monsters.skeleton import Skeleton
        if isinstance(entity, Skeleton) or isinstance(entity, Fireball):
            return False

        is_colliding = super().is_colliding(entity)

        if is_colliding:
            self.unload()
            if isinstance(entity, LivingEntity):
                entity.damage(10)
                return False
            return True

        return False
