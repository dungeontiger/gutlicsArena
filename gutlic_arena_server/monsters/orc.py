from .monster import Monster
from gutlic_arena_server.actions.greataxe import Greataxe
from gutlic_arena_server.actions.hit_type import HitType
from gutlic_arena_server.monsters.target_strategy import TargetStrategy

# TODO: deal with javelin


class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 16, 12, 16, 7, 11, 10, 13, '2d8+6')
        super().set_actions([Greataxe()])

    def take_turn(self, arena):
        self.arena = arena
        # TODO: select action: attack, flee, etc
        self.attack()

    def attack(self):
        # assuming to attack, select target then select the weapon
        self.select_target(TargetStrategy.STICKY_RANDOM)
        action = self.select_action(self.target)
        roll = action.roll_to_hit(self.target)
        if roll is not HitType.MISS and roll is not HitType.CRITICAL_MISS:
            action.roll_damage(self.target)
