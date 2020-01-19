"""Human race"""
from .race import Race
from .size import Size
from .languages import Languages

class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human', 1, 1, 1, 1, 1, 1, size=Size.MEDIUM, speed=30, languages=[Languages.COMMON])

    def __str__(self):
        return self.name

"""
TODO:
Languages: one more choice
"""