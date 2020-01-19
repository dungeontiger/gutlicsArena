"""Halfling race"""
from gutlic_arena_server.players.race import Race
from gutlic_arena_server.types.size import Size
from gutlic_arena_server.types.languages import Languages
from gutlic_arena_server.types.trait import Trait


class Halfling(Race):
    def __init__(self):
        l = [Languages.COMMON, Languages.HALFLING]
        super(Halfling, self).__init__('Halfling', _dex=2, size=Size.SMALL, speed=25, languages=l)
        self.add_traits([Trait.LUCKY, Trait.BRAVE, Trait.HALFLING_NIMBLENESS])

    def __str__(self):
        return self.name

"""
TODO:

Lucky: Reroll any 1 on an attack roll, ability check or saving throw
Brave: Advantage on saves vs fear
Nimbleness: move through any creature larger size than us
"""