from .arena import Arena


class Game:
    def __init__(self, factions):
        self.arena = Arena(factions)

    def start(self):
        while not self.arena.is_over():
            self.arena.play_turn()

