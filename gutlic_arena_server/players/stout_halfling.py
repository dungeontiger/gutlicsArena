from .halfling import Halfling


class StoutHalfling(Halfling):
    def __init__(self):
        self.con = self.con + 1
        self.name = 'Stout Halfling'

# TODO:
# Stout: Stout Resilience: Advantage save vs poison, resistance to poison
