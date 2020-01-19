"""Rogue Class"""
from gutlic_arena_server.players.player_class import PlayerClass
from gutlic_arena_server.types.languages import Languages
from gutlic_arena_server.types.weapon_type import WeaponType


class Rogue(PlayerClass):
    def __init__(self):
        super(Rogue, self).__init__('Rogue', 8)
        self.add_languages([Languages.THIEVES_CANT])
        # rogues are proficient in a selection of weapons
        self.add_weapon_proficiencies([WeaponType.SIMPLE_MELEE,
                                       WeaponType.SIMPLE_RANGED,
                                       'Hand crossbow',
                                       'Longsword',
                                       'Rapier',
                                       'Shortsword'])

    def __str__(self):
        return self.name


"""
TODO: 

Expertise
Sneak Attack
"""