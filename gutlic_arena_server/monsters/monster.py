import math


class Monster:
    def __init__(self, name, _str, _dex, _con, _int, _wis, _cha, _ac, _hd):
        self.monsterName = name
        self.str = _str
        self.dex = _dex
        self.con = _con
        self.int = _int
        self.wis = _wis
        self.cha = _cha
        self.ac = _ac
        self.hd = _hd

    def get_name(self):
        return self.monsterName

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

    def get_hd(self):
        return self.hd

    @staticmethod
    def _calc_stat_mod(stat):
        return math.floor((stat - 10) / 2)
