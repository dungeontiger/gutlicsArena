"""Rogue Class"""
from gutlic_arena_server.players.player_class import PlayerClass


class Rogue(PlayerClass):
    def __init__(self):
        super(Rogue, self).__init__('Rogue', 8)

    def __str__(self):
        return self.name
