from .monster import Monster
from .target_strategy import TargetStrategy
from gutlic_arena_server.actions.scimitar import Scimitar
from gutlic_arena_server.actions.hit_type import HitType

# TODO: deal with short bow and shield
# TODO: speed, alignment, size, skills, senses, languages, CR

# TODO: Nimble Escape: Disengage or hide on each of its turns


class Goblin(Monster):
    def __init__(self):
        super().__init__('Goblin', 8, 14, 10, 10, 8, 8, 15, '2d6')
        super().set_actions([Scimitar()])

    def take_turn(self, arena):
        # TODO: select action: attack, flee, etc
        self.arena = arena
        self.attack()

    def attack(self):
        # assuming to attack, select target then select the weapon
        self.select_target(TargetStrategy.STICKY_RANDOM)
        action = self.select_action(self.target)
        roll = action.roll_to_hit(self.target)
        if roll is not HitType.MISS and roll is not HitType.CRITICAL_MISS:
            action.roll_damage(self.target)
