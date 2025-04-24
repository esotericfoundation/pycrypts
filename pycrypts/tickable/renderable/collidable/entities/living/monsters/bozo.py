import random
from typing import TYPE_CHECKING

from .ai.goals.back_off_from_target import BackOffFromTargetGoal
from .ai.goals.blast_bozos_balls import BlastBozosBallsGoal
from .ai.goals.random_wander import RandomWanderGoal
from .ai.goals.walk_to_target import WalkToTargetGoal
from ..players.player import Player
from ...bozos_ball import BozosBall
from ....collidable import Collidable
from .......rooms.room import Room
from .monster import Monster

if TYPE_CHECKING:
    from .......game import PyCrypts
    from ..living_entity import LivingEntity


class Bozo(Monster):

    def __init__(self, game: "PyCrypts", room: "Room", position: tuple[int, int]):
        self.backOffGoal = BackOffFromTargetGoal(self, 0, game, Player, game.players, 0.7, 200)
        self.chaseGoal = WalkToTargetGoal(self, 1, game, Player, game.players, 1.1)
        self.blastBallsGoal = BlastBozosBallsGoal(self, 1, game)
        self.wanderGoal = RandomWanderGoal(self, 1, game, 1.5, 1.5, 0.1, 0.35)
        self.crazyWanderGoal = RandomWanderGoal(self, 1, game, 2.0, 1.5, 0.1, 0.35)

        damage_sound = game.get_sound("bozo_damage")
        damage_sound.set_volume(0.5)

        super().__init__(game, room, position, "bozo", 70, 600, damage_sound)

        self.is_calm = True
        self.is_aggressive = False
        self.is_going_crazy = False

        self.remaining_calmness = 5
        self.remaining_aggression = 0
        self.remaining_craziness = 0


    def register_goals(self):
        self.goals.append(self.blastBallsGoal)
        self.goals.append(self.backOffGoal)
        self.goals.append(self.chaseGoal)
        self.goals.append(self.wanderGoal)

    def ai_tick(self):
        super().ai_tick()

        if self.is_calm:
            self.remaining_calmness -= self.game.dt

            if self.remaining_calmness < 0:
                self.is_calm = False

                if random.choice([True, False]):
                    self.is_aggressive = True
                    self.remaining_aggression = random.randint(5, 7)
                    self.on_aggressive()
                else:
                    self.is_going_crazy = True
                    self.remaining_craziness = random.randint(4, 5)
                    self.on_going_crazy()
        elif self.is_aggressive:
            self.remaining_aggression -= self.game.dt

            if self.remaining_aggression < 0:
                self.is_aggressive = False

                if random.choice([True, False]):
                    self.is_calm = True
                    self.remaining_calmness = random.randint(5, 7)
                    self.on_calm()
                else:
                    self.is_going_crazy = True
                    self.remaining_craziness = random.randint(4, 5)
                    self.on_going_crazy()
        elif self.is_going_crazy:
            self.remaining_craziness -= self.game.dt

            if self.remaining_craziness < 0:
                self.is_going_crazy = False

                if random.choice([True, False]):
                    self.is_aggressive = True
                    self.remaining_aggression = random.randint(5, 7)
                    self.on_aggressive()
                else:
                    self.is_calm = True
                    self.remaining_calmness = random.randint(5, 7)
                    self.on_calm()

    def on_calm(self):
        self.game.logger.debug("Bozo calm phase has begun")
        self.goals.clear()

        self.goals.append(self.backOffGoal)
        self.goals.append(self.blastBallsGoal)
        self.goals.append(self.wanderGoal)

    def on_aggressive(self):
        self.game.logger.debug("Bozo aggressive phase has begun")
        self.goals.clear()

        self.goals.append(self.blastBallsGoal)
        self.goals.append(self.chaseGoal)

    def on_going_crazy(self):
        self.game.logger.debug("Bozo crazy phase has begun")
        self.goals.clear()

        self.goals.append(self.blastBallsGoal)
        self.goals.append(self.crazyWanderGoal)

    def is_colliding(self, entity: Collidable) -> bool:
        if isinstance(entity, BozosBall):
            return False

        return super().is_colliding(entity)

    def attack_entity(self, entity: "LivingEntity"):
        if self.position.distance_squared_to(entity.position) < (10000 * self.game.current_room.scale * self.game.current_room.scale):
            entity.damage(15)
            entity.velocity += (entity.position - self.position).normalize() * 40 * self.room.scale

    def die(self):
        super().die()

        self.game.won = True
