from .monster import Monster
from gutlic_arena_server.actions.greataxe import Greataxe

# TODO: deal with javelin


class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 16, 12, 16, 7, 11, 10, 13, '2d8+6')
        super().set_actions([Greataxe()])