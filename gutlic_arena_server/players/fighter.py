"""Fighter Class"""
from .player import Player


class Fighter(Player):
    def __init__(self):
        super(Fighter, self).__init__()

    def __str__(self):
        return self.name + ' (Fighter)'
