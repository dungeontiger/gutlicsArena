from .monster import Monster


class Goblin(Monster):
    def __init__(self):
        super().__init__('Goblin', 8, 14, 10, 10, 8, 8, 15, '2d6')
