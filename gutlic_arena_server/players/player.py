"""Class for players"""
from gutlic_arena_server.entity import Entity
from gutlic_arena_server import to_hit_engine
from gutlic_arena_server import damage_engine
from gutlic_arena_server.types.armor_type import ArmorType


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
        self.armor = None
        self.shield = None

    def has_trait(self, trait):
        # traits currently come from the class or the race
        return self.race.has_trait(trait) or self._class.has_trait(trait)

    # the player takes the attack action
    def attack_action(self, weapon, target):
        hit = to_hit_engine.roll_to_hit(self, target, weapon, self.arena)
        damage = damage_engine.roll_damage(self, target, weapon, hit, self.arena)
        target.apply_damage(damage)

    def get_proficiency_bonus(self, weapon):
        if self._class.is_weapon_proficient(weapon):
            return self.proficiency
        return 0

    def is_weapon_proficient(self, weapon):
        # TODO: handle racial weapon proficiencies
        return self._class.is_weapon_proficient(weapon)

    def is_armor_proficient(self, armor):
        # TODO: handle racial armor proficiencies
        return self._class.is_armor_proficient(armor)

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

    def set_armor(self, armor):
        self.armor = armor

    def get_armor(self):
        return self.armor

    def set_shield(self, shield):
        if shield.get_type() == ArmorType.SHIELD:
            self.shield = shield

    def get_shield(self):
        return self.shield

    def get_ac(self):
        ac = 10
        if self.armor is not None:
            ac = self.armor.get_ac()
            if self.armor.get_max_dex_mod() == -1:
                ac += self.get_dex_mod()
            elif self.armor.get_max_dex_mod() > 0:
                ac += max(self.get_dex_mod(), self.armor.get_max_dex_mod())
        else:
            ac += self.get_dex_mod()

        if self.shield is not None:
            ac += self.shield.get_ac()
        return ac

    def __str__(self):
        return '{0}, {1} {2}'.format(self.name, self.race.get_name(), self._class.get_name())
