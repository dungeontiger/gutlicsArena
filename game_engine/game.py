from .arena import Arena


class Game:
    def __init__(self, factions):
        self.arena = Arena(factions)

    def play(self):
        while not self.arena.is_over():
            self.arena.play_turn()
        return self.arena.get_winning_faction()

