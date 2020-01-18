"""Class for players"""
from gutlic_arena_server.entity import Entity
from gutlic_arena_server.players.race import Race
from gutlic_arena_server.players.player_class import Class


class Player(Entity):
    def __init__(self, name, stats, race, _class):
        super(Player, self).__init__(name)
        self.str = stats[0]
        self.dex = stats[1]
        self.con = stats[2]
        self.int = stats[3]
        self.wis = stats[4]
        self.cha = stats[5]
        self._class = _class
        self.race = race
        # first level get max hp which is your hit dice type
        self.hp = _class.get_hd() + self.get_con_mod()
        self.cur_hp = self.hp

    # stats have racial mods, always calculate to allow for race to change in the future (reincarnate?, wish?)
    def get_str(self):
        return self.str + self.race.get_str_mod()

    def get_dex(self):
        return self.dex + self.race.get_dex_mod()

    def get_con(self):
        return self.con + self.race.get_con_mod()

    def get_int(self):
        return self.int + self.race.get_int_mod()

    def get_wis(self):
        return self.wis + self.race.get_wis_mod()

    def get_cha(self):
        return self.cha + self.race.get_cha_mod()

    def __str__(self):
        return '{0}, {1} {2}'.format(self.name, self.race.get_name(), self._class.get_name())
