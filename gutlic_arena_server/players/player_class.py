"""Class base class for players"""


class PlayerClass:
    def __init__(self, name, hd):
        self.name = name
        self.hd = hd
        self.level = 1
        self.exp = 0
        self.traits = []
        self.languages = []

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

    def get_languages(self):
        return self.languages

    def add_languages(self, langs):
        self.languages.extend(langs)

    def has_trait(self, trait):
        return trait in self.traits

    def __str__(self):
        return self.name


