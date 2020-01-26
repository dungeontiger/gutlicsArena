from .action import Action
from game_engine.types.action_type import ActionType
from game_engine.types.damage_type import DamageType


class Greataxe(Action):
    def __init__(self):
        super().__init__('Greataxe', ActionType.MELEE, 5, '1d12+3', DamageType.SLASHING, 5, 1)
