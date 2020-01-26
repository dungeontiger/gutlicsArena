from .action import Action
from game_engine.types.action_type import ActionType
from game_engine.types.damage_type import DamageType


class Scimitar(Action):
    def __init__(self):
        super().__init__('Scimitar', ActionType.MELEE, 4, '1d6+2', DamageType.SLASHING, 5, 1)
