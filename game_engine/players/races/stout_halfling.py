from game_engine.players.races.halfling import Halfling
from game_engine.types.trait import Trait


class StoutHalfling(Halfling):
    def __init__(self):
        super(StoutHalfling, self).__init__()
        self.con = self.con + 1
        self.name = 'Stout Halfling'
        self.add_traits([Trait.STOUT_RESISTANCE])

# TODO:
# Stout: Stout Resilience: Advantage save vs poison, resistance to poison
