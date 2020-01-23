from .action import Action
from gutlic_arena_server.types.action_type import ActionType
from gutlic_arena_server.types.damage_type import DamageType


class Greataxe(Action):
    def __init__(self):
        super().__init__('Greataxe', ActionType.MELEE, 5, '1d12+3', DamageType.SLASHING, 5, 1)
