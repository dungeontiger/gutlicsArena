"""Base class for monsters and players"""
import math

from . import dice


class Entity:
    def __init__(self, name='', s=0, d=0, c=0, i=0, w=0, h=0):
        self.name = name
        self.str = s
        self.dex = d
        self.con = c
        self.int = i
        self.wis = w
        self.cha = h
        self.ac = 0
        self.hp = 0
        self.cur_hp = 0
        self.faction = None
        self.arena = None

    def get_name(self):
        return self.name

    def get_str(self):
        return self.str

    def get_dex(self):
        return self.dex

    def get_con(self):
        return self.con

    def get_int(self):
        return self.int

    def get_wis(self):
        return self.wis

    def get_cha(self):
        return self.cha

    def get_str_mod(self):
        return self._calc_stat_mod(self.str)

    def get_dex_mod(self):
        return self._calc_stat_mod(self.dex)

    def get_con_mod(self):
        return self._calc_stat_mod(self.con)

    def get_int_mod(self):
        return self._calc_stat_mod(self.int)

    def get_wis_mod(self):
        return self._calc_stat_mod(self.wis)

    def get_cha_mod(self):
        return self._calc_stat_mod(self.cha)

    def get_ac(self):
        return self.ac

    def get_hp(self):
        return self.hp

    def get_cur_hp(self):
        return self.cur_hp

    def set_faction(self, faction):
        self.faction = faction

    def get_faction(self):
        return self.faction

    def roll_initiative(self):
        # initiative is d20 plus dex mod
        # TODO: advantage / disadvantage support
        return dice.d20() + self.get_dex_mod()

    @staticmethod
    def _calc_stat_mod(stat):
        return math.floor((stat - 10) / 2)

    def __str__(self):
        return self.name


