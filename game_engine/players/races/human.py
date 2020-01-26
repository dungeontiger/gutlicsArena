"""Human race"""
from game_engine.players.race import Race
from game_engine.types.size import Size
from game_engine.types.languages import Languages

class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human', 1, 1, 1, 1, 1, 1, size=Size.MEDIUM, speed=30, languages=[Languages.COMMON])

    def __str__(self):
        return self.name

"""
TODO:
Languages: one more choice
"""