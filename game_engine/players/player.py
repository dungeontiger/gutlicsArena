"""Class for players"""
from game_engine.entity import Entity
from game_engine import to_hit_engine
from game_engine import damage_engine
from game_engine.types.armor_type import ArmorType
from game_engine.armor import Armor
from game_engine.weapon import Weapon


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
        self.armor = None
        # shield goes into one hand
        # EITHER two_hands is None or BOTH left and right hands are  None
        self.right_hand = None
        self.left_hand = None
        self.two_hands = None

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
            return self._class.get_proficiency_bonus()
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

    def set_right_hand(self, item):
        if isinstance(item, Weapon) and item.get_two_handed():
            return None
        self.right_hand = item
        return self.drop_two_hands()

    def set_left_hand(self, item):
        if isinstance(item, Weapon) and item.get_two_handed():
            return None
        self.left_hand = item
        return self.drop_two_hands()

    def set_two_hands(self, item):
        if isinstance(item, Weapon) and (item.get_two_handed() or item.get_versatile() is not None):
            self.two_hands = item
        # TODO: technically should return a list of what was dropped
        self.drop_right_hand()
        self.drop_left_hand()

    def drop_right_hand(self):
        item = self.right_hand
        self.right_hand = None
        return item

    def drop_left_hand(self):
        item = self.left_hand
        self.left_hand = None
        return item

    def drop_two_hands(self):
        item = self.two_hands
        self.two_hands = None
        return item

    def get_right_hand(self):
        return self.right_hand

    def get_left_hand(self):
        return self.left_hand

    def get_two_hands(self):
        return self.two_hands

    def wearing_unproficient_armor(self):
        return self.is_armor_proficient(self.armor) is False or self.is_armor_proficient(self.get_shield()) is False

    def add_fighting_style(self, fs):
        self._class.add_fighting_style(fs)

    def too_weak_for_armor(self):
        if self.armor is not None:
            required = self.armor.get_str_required()
            return required != 0 and self.get_str() < required
        return False

    def get_ac(self):
        ac = 10
        if self.armor is not None:
            ac = self.armor.get_ac()
            if self.armor.get_max_dex_mod() == -1:
                ac += self.get_dex_mod()
            elif self.armor.get_max_dex_mod() > 0:
                if self.get_dex_mod() > self.armor.get_max_dex_mod():
                    ac += self.armor.get_max_dex_mod()
                else:
                    ac += self.get_dex_mod()
        else:
            ac += self.get_dex_mod()

        shield = self.get_shield()
        if shield is not None:
            ac += shield.get_ac()
        return ac

    def get_shield(self):
        if self.right_hand and isinstance(self.right_hand, Armor) and self.right_hand.get_type() == ArmorType.SHIELD:
            return self.right_hand
        elif self.left_hand and isinstance(self.left_hand, Armor) and self.left_hand.get_type() == ArmorType.SHIELD:
            return self.left_hand
        return None

    def get_speed(self):
        speed = self.race.get_speed()
        if self.too_weak_for_armor():
            return speed - 10
        return speed

    def __str__(self):
        return '{0}, {1} {2}'.format(self.name, self.race.get_name(), self._class.get_name())
