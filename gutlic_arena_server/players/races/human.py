"""Human race"""
from gutlic_arena_server.players.race import Race
from gutlic_arena_server.types.size import Size
from gutlic_arena_server.types.languages import Languages

class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human', 1, 1, 1, 1, 1, 1, size=Size.MEDIUM, speed=30, languages=[Languages.COMMON])

    def __str__(self):
        return self.name

"""
TODO:
Languages: one more choice
"""