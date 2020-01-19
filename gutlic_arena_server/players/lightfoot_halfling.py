from .halfling import Halfling


class LightfootHalfling(Halfling):
    def __init__(self):
        self.cha = self.cha + 1
        self.name = 'Lightfoot Halfling'


# TODO:
# Lightfoot: Stealthy: can hide even if only obscured by a larger size creature
