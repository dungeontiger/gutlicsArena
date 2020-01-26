from game_engine.players.races.halfling import Halfling
from game_engine.types.trait import Trait


class LightfootHalfling(Halfling):
    def __init__(self):
        super(LightfootHalfling, self).__init__()
        self.cha = self.cha + 1
        self.name = 'Lightfoot Halfling'
        self.add_traits([Trait.NATURALLY_STEALTHY])


# TODO:
# Lightfoot: Stealthy: can hide even if only obscured by a larger size creature
