"""Class base class for players"""
import math
levels = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000,
          195000, 225000, 265000, 305000, 355000]


class PlayerClass:
    def __init__(self, name, hd):
        self.name = name
        self.hd = hd
        self.level = 1
        self.exp = 0
        self.traits = []
        self.languages = []
        self.weapon_proficiencies = []
        self.armor_proficiencies = []

    def get_hd(self):
        return self.hd

    def get_name(self):
        return self.name

    # TODO: this could be simplified
    def get_level(self):
        for level in range(0, 19):
            if levels[level] <= self.exp < levels[level + 1]:
                return level + 1
        return 20

    def get_exp(self):
        return self.exp

    def add_exp(self, xp):
        # TODO:
        self.exp = self.exp + xp
        if self.exp < 0:
            self.exp = 0
        # did they advance a level?
        return False

    def get_languages(self):
        return self.languages

    def add_languages(self, langs):
        self.languages.extend(langs)

    def add_weapon_proficiencies(self, profs):
        self.weapon_proficiencies.extend(profs)

    def add_armor_proficiencies(self, profs):
        self.armor_proficiencies.extend(profs)

    def is_weapon_proficient(self, weapon):
        # first check by weapon type, then check by weapon name
        if weapon.get_type() in self.weapon_proficiencies:
            return True
        elif weapon.get_id() in self.weapon_proficiencies:
            return True
        return False

    def is_armor_proficient(self, armor):
        # first check by armor type, then check by armor name
        if armor is None or armor.get_type() in self.armor_proficiencies:
            return True
        elif armor.get_id() in self.armor_proficiencies:
            return True
        return False

    def has_trait(self, trait):
        return trait in self.traits

    def get_proficiency_bonus(self):
        return math.ceil(self.get_level() / 4) + 1

    def __str__(self):
        return self.name


