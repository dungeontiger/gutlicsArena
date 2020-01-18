"""Rogue Class"""
from .player_class import Class


class Rogue(Class):
    def __init__(self):
        super(Rogue, self).__init__('Rogue', 8)

    def __str__(self):
        return self.name
