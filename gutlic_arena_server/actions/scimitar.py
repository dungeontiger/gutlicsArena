from .action import Action
from .weapon_type import WeaponType
from gutlic_arena_server.types.damage_type import DamageType


class Scimitar(Action):
    def __init__(self):
        super().__init__('Scimitar', WeaponType.MELEE, 4, '1d6+2', DamageType.SLASHING, 5, 1)
