from .action import Action
from gutlic_arena_server.types.action_type import ActionType
from gutlic_arena_server.types.damage_type import DamageType


class Scimitar(Action):
    def __init__(self):
        super().__init__('Scimitar', ActionType.MELEE, 4, '1d6+2', DamageType.SLASHING, 5, 1)
