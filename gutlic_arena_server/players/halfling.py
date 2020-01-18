"""Halfling race"""
from .race import Race


class Halfling(Race):
    def __init__(self):
        # + 2 dex
        super(Halfling, self).__init__('Halfling', _dex=2)

    def __str__(self):
        return self.name
