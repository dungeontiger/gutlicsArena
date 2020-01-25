"""Fighter Class"""
from gutlic_arena_server.players.player_class import PlayerClass
from gutlic_arena_server.types.weapon_type import WeaponType
from gutlic_arena_server.types.armor_type import ArmorType
from gutlic_arena_server.types.trait import Trait


class Fighter(PlayerClass):
    def __init__(self):
        super(Fighter, self).__init__('Fighter', 10)
        # fighters proficient in all weapons
        self.add_weapon_proficiencies([WeaponType.SIMPLE_MELEE,
                                       WeaponType.SIMPLE_RANGED,
                                       WeaponType.MARTIAL_MELEE,
                                       WeaponType.MARTIAL_RANGED])
        # fighters are proficient in all armor
        self.add_armor_proficiencies([ArmorType.HEAVY_ARMOR,
                                      ArmorType.MEDIUM_ARMOR,
                                      ArmorType.LIGHT_ARMOR,
                                      ArmorType.SHIELD])

        # all fighters get second wind
        self.traits.append(Trait.SECOND_WIND)

    def add_fighting_style(self, style):
        self.traits.append(style)

    def __str__(self):
        return self.name

# TODO:

"""
Fighting styles:

Protection When a creature you can see attacks another target within 5 feet of you can force disadvantage on them; 
    must be using shield
Two-weapon fighting  Add your ability modifer to your second weapon damage
"""

"""
Second wind: one per rest, use bonus action to add 1d10 + level to hit points up to maximum hit points
"""