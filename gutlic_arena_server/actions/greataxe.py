from .action import Action
from .weapon_type import WeaponType
from .damage_type import DamageType


class Greataxe(Action):
    def __init__(self):
        super().__init__('Greataxe', WeaponType.MELEE, 5, '1d12+3', DamageType.SLASHING, 5, 1)
