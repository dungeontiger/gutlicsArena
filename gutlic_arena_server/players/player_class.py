"""Class base class for players"""


class PlayerClass:
    def __init__(self, name, hd):
        self.name = name
        self.hd = hd
        self.level = 1
        self.exp = 0

    def get_hd(self):
        return self.hd

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def add_exp(self, xp):
        # TODO:
        self.exp = self.exp + xp
        # did they advance a level?
        return False

    def __str__(self):
        return self.name


