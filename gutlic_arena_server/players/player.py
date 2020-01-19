"""Class for players"""
from gutlic_arena_server.entity import Entity
from gutlic_arena_server.players.race import Race
from gutlic_arena_server.players.player_class import PlayerClass
from gutlic_arena_server import dice
from gutlic_arena_server.actions.hit_type import HitType


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
        self.add_languages(race.get_languages())
        self.weapons = []
        self.proficiency = 2

    # the player takes the attack action
    def attack_action(self, weapon, target):
        hit = self._roll_to_hit(weapon, target)
        if hit is HitType.HIT or HitType.CRITICAL_HIT:
            self._roll_damage(weapon, target, hit)

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

    def add_languages(self, language):
        self.languages.extend(language)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def _roll_to_hit(self, weapon, target):
        # determine the modifier, skill + proficiency
        hit = HitType.MISS
        # TODO: only if proficient
        mod = self.proficiency
        if weapon.get_finesse():
            mod = mod + max(self.get_dex_mod(), self.get_str_mod())
        elif weapon.is_melee():
            mod = mod + self.get_str_mod()
        elif weapon.is_ranged():
            mod = mod + self.get_dex_mod()
        # TODO: determine advantage / disadvantage
        # roll to hit
        roll = dice.d20()
        # TODO: luck of the halfling
        if roll == 1:
            roll = dice.d20()
        if roll == 20:
            hit = HitType.CRITICAL_HIT
        elif roll == 1:
            hit = HitType.CRITICAL_MISS
        elif roll + mod >= target.get_ac():
            hit = HitType.HIT
        return hit

    def _roll_damage(self, weapon, target, hit):
        mod = 0
        if weapon.get_finesse():
            mod = mod + max(self.get_dex_mod(), self.get_str_mod())
        elif weapon.is_melee():
            mod = mod + self.get_str_mod()
        elif weapon.is_ranged():
            mod = mod + self.get_dex_mod()
        damage = dice.roll_damage(weapon.get_damage(), hit, mod)
        target.apply_damage(damage)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.name, self.race.get_name(), self._class.get_name())
