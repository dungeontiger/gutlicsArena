from game_engine.types.size import Size
""""Base class for player races."""


class Race:
    def __init__(self, name, _str=0, _dex=0, _con=0, _int=0, _wis=0, _cha=0, size=Size.MEDIUM, speed=0, languages=[]):
        self.name = name
        self.str = _str
        self.dex = _dex
        self.con = _con
        self.int = _int
        self.wis = _wis
        self.cha = _cha
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = []

    def get_str_mod(self):
        return self.str

    def get_dex_mod(self):
        return self.dex

    def get_con_mod(self):
        return self.con

    def get_int_mod(self):
        return self.str

    def get_wis_mod(self):
        return self.wis

    def get_cha_mod(self):
        return self.cha

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_speed(self):
        return self.speed

    def get_languages(self):
        return self.languages

    def add_traits(self, traits):
        self.traits.extend(traits)

    def has_trait(self, trait):
        return trait in self.traits

    def __str__(self):
        return self.name
