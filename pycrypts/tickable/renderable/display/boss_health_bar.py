from pygame import Vector2

from ..collidable.entities.living.living_entity import LivingEntity
from .health_bar import HealthBar


class BossHealthBar(HealthBar):

    def init(self, entity: LivingEntity, top_left: (int, int) or Vector2, width: int, height: int, game: "PyCrypts"):
        super().__init__(entity, top_left, width, height, game)

    def tick(self):
        super().tick()

        self.text.text = ""
