"""Fighter Class"""
from .player_class import Class


class Fighter(Class):
    def __init__(self):
        super(Fighter, self).__init__('Fighter', 10)

    def __str__(self):
        return self.name
