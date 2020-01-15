# TODO: if PCs are going to be monsters, rename this to entity
import math, random
from .target_strategy import TargetStrategy
from gutlic_arena_server import dice
from .entity_state import EntityState


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
        self.hp = dice.roll(_hd)
        self.cur_hp = self.hp

        # not on constructor because it would be too long
        self.actions = []
        self.faction = None

        # game time attributes
        self.target = None
        self.state = EntityState.NORMAL

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

    def get_hp(self):
        return self.hp

    def get_cur_hp(self):
        return self.cur_hp

    def set_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions

    def get_state(self):
        return self.state

    def roll_initiative(self):
        # initiative is d20 plus dex mod
        # TODO: advantage / disadvantage support
        return dice.d20() + self.get_dex_mod()

    def set_faction(self, faction):
        self.faction = faction

    def get_faction(self):
        return self.faction

    def take_turn(self, arena):
        """Must be overloaded in the child class."""
        pass

    def select_target(self, strategy):
        if strategy == TargetStrategy.STICKY_RANDOM:
            if self.target is None or self.target.is_dead():
                self.target = random.choice(self.get_all_targets())
        elif strategy == TargetStrategy.RANDOM:
            self.target = random.choice(self.get_all_targets())

    def get_all_targets(self):
        targets = []
        for faction in self.arena.get_opposing_factions(self.faction):
            for e in faction.get_entities():
                targets.append(e)
        return targets

    def select_action(self, target):
        # for now just pick the first action
        return self.actions[0]

    def apply_damage(self, damage, damage_type):
        # eventually damage type will be used for resistances etc
        self.cur_hp = self.cur_hp - damage
        if self.cur_hp <= 0:
            self.state = EntityState.DEAD

    def is_dead(self):
        return self.state is EntityState.DEAD

    @staticmethod
    def _calc_stat_mod(stat):
        return math.floor((stat - 10) / 2)

    def __str__(self):
        return self.monsterName
