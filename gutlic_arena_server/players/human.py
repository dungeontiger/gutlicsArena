"""Human race"""
from .race import Race


class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human', 1, 1, 1, 1, 1, 1)

    def __str__(self):
        return self.name
