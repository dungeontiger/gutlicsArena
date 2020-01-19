"""Fighter Class"""
from .player_class import PlayerClass


class Fighter(PlayerClass):
    def __init__(self):
        super(Fighter, self).__init__('Fighter', 10)

    def __str__(self):
        return self.name
