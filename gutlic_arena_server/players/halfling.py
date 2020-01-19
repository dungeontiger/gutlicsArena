"""Halfling race"""
from .race import Race
from .size import Size
from .languages import Languages


class Halfling(Race):
    def __init__(self):
        l = [Languages.COMMON, Languages.HALFLING]
        super(Halfling, self).__init__('Halfling', _dex=2, size=Size.SMALL, speed=25, languages=l)

    def __str__(self):
        return self.name

"""
TODO:

Lucky: Reroll any 1 on an attack roll, ability check or saving throw
Brave: Advantage on saves vs fear
Nimbleness: move through any creature larger size than us
"""