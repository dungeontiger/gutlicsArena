"""Fighter Class"""
from gutlic_arena_server.players.player_class import PlayerClass


class Fighter(PlayerClass):
    def __init__(self):
        super(Fighter, self).__init__('Fighter', 10)

    def __str__(self):
        return self.name

# TODO: fighting style, second wind

"""
Fighting styles:

Archery +2 to hit ranged
Defence +1 to AC when wearing armor
Dueling +2 to hit if one handed weapon (only one weapon?)
Great Weapon Fighting reroll 1 or 2 on damage for verstaile or two handed weapons
Protection When a creature you can see attacks another target within 5 feet of you can force disadvantage on them; 
    must be using shield
Two-weapon fighting  Add your ability modifer to your second weapon damage
"""

"""
Second wind: one per rest, use bonus action to add 1d10 + level to hit points up to maximum hit points
"""