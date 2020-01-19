"""Class for players"""
from gutlic_arena_server.entity import Entity
from gutlic_arena_server import dice
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server import to_hit_engine
from gutlic_arena_server import damage_engine


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
        self.add_languages(_class.get_languages())
        self.weapons = []
        self.proficiency = 2

    def has_trait(self, trait):
        # traits currently come from the class or the race
        return self.race.has_trait(trait) or self._class.has_trait(trait)

    # the player takes the attack action
    def attack_action(self, weapon, target):
        hit = to_hit_engine.roll_to_hit(self, target, weapon, self.arena)
        damage = damage_engine.roll_damage(self, target, weapon, hit, self.arena)
        target.apply_damage(damage)

    def get_proficiency_bonus(self, weapon):
        if self._class.is_proficient(weapon):
            return self.proficiency
        return 0

    def is_proficient(self, weapon):
        return self._class.is_proficient(weapon)

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

    def __str__(self):
        return '{0}, {1} {2}'.format(self.name, self.race.get_name(), self._class.get_name())
