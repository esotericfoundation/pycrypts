from tickable.renderable.collidable.collidable import Collidable
from tickable.renderable.collidable.entities.entity import Entity
from tickable.renderable.collidable.entities.fireball import Fireball
from tickable.renderable.collidable.entities.living.living_entity import LivingEntity


class Arrow(Fireball):
    def __init__(self, target: tuple[int, int], position: tuple[int, int], size: int, game):
        super().__init__(target, position, size, game, 2, "arrow")

    def is_colliding(self, entity: Collidable) -> bool:
        if isinstance(entity, Entity) and entity.no_clip:
            return False

        from tickable.renderable.collidable.entities.living.players.player import Player
        if isinstance(entity, Player):
            return False

        if isinstance(entity, Arrow):
            return False

        is_colliding = Entity.is_colliding(self, entity)

        if is_colliding:
            if isinstance(entity, Fireball):
                entity.unload()
                return False

            self.unload()

            if isinstance(entity, LivingEntity):
                entity.damage(10)
                return False
            return True

        return False
