"""Rogue Class"""
from gutlic_arena_server.players.player_class import PlayerClass
from gutlic_arena_server.types.languages import Languages


class Rogue(PlayerClass):
    def __init__(self):
        super(Rogue, self).__init__('Rogue', 8)
        self.add_languages([Languages.THIEVES_CANT])

    def __str__(self):
        return self.name

"""
TODO: 

Expertise
Sneak Attack
"""