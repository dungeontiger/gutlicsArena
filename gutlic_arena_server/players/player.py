"""Class for players"""
from gutlic_arena_server.entity import Entity


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__()

    def __str__(self):
        return self.name
