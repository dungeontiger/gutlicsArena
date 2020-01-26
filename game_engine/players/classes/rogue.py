"""Rogue Class"""
from game_engine.players.player_class import PlayerClass
from game_engine.types.languages import Languages
from game_engine.types.weapon_type import WeaponType
from game_engine.types.weapon_id import WeaponId
from game_engine.types.armor_type import ArmorType


class Rogue(PlayerClass):
    def __init__(self):
        super(Rogue, self).__init__('Rogue', 8)
        self.add_languages([Languages.THIEVES_CANT])
        # rogues are proficient in a selection of weapons
        self.add_weapon_proficiencies([WeaponType.SIMPLE_MELEE,
                                       WeaponType.SIMPLE_RANGED,
                                       WeaponId.HAND_CROSSBOW,
                                       WeaponId.LONGSWORD,
                                       WeaponId.RAPIER,
                                       WeaponId.SHORTSWORD])
        # rogues are proficient only in light armor
        self.add_armor_proficiencies([ArmorType.LIGHT_ARMOR])

    def __str__(self):
        return self.name


"""
TODO: 

Expertise
Sneak Attack
    Sneak attack bonus = level / 2 (rounded up) d6
"""