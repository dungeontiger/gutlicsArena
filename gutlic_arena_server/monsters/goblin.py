from .monster import Monster
from gutlic_arena_server.actions.scimitar import Scimitar

# TODO: deal with short bow and shield


class Goblin(Monster):
    def __init__(self):
        super().__init__('Goblin', 8, 14, 10, 10, 8, 8, 15, '2d6')
        super().set_actions([Scimitar()])