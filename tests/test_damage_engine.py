import unittest
from unittest.mock import patch

from gutlic_arena_server.damage_engine import roll_damage
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server.weapons import weapons
from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.players.classes.fighter import Fighter
from gutlic_arena_server.types.weapon_id import WeaponId
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.types.trait import Trait
from gutlic_arena_server.armors import armors
from gutlic_arena_server.types.armor_id import ArmorId


class TestDamageEngine(unittest.TestCase):
    def test_simple_damage(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 3)

    def test_ranged(self):
        attacker = Player('Bob', [10, 16, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.LIGHT_CROSSBOW]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 6)

    def test_melee(self):
        attacker = Player('Bob', [16, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.CLUB]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 6)

    def test_finesse_str(self):
        attacker = Player('Bob', [16, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 6)

    def test_finesse_dex(self):
        attacker = Player('Bob', [10, 16, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 6)

    def test_finesse_no_mod(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 3)

    def test_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.MISS, None), 0)

    def test__critical_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.CRITICAL_MISS, None), 0)

    def test_critical_hit(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.DAGGER]
        set_values([4, 3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.CRITICAL_HIT, None), 7)

    def test_critical_hit_maul(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attack = weapons[WeaponId.MAUL]
        set_values([4, 3, 6, 5])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.CRITICAL_HIT, None), 18)

    def test_negative_damage(self):
        attacker = Player('Bob', [3, 3, 10, 10, 10, 10], Human(), Fighter())
        set_values([1])
        attack = weapons[WeaponId.DAGGER]
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_damage(attacker, None, attack, HitType.HIT, None), 0)

    def test_using_versatile_one_handed(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_right_hand(weapons[WeaponId.SPEAR])
        d = roll_damage(attacker, None, attacker.get_right_hand(), HitType.HIT, None)
        # kind of lame, not always going to fail, not sure how else to be sure
        # TODO: could be solved by a debugging option to focus dice to roll max then check for 6
        self.assertTrue(1 <= d <= 6)

    def test_using_versatile_two_handed(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_two_hands(weapons[WeaponId.SPEAR])
        d = roll_damage(attacker, None, attacker.get_two_hands(), HitType.HIT, None)
        # kind of lame, not always going to fail, not sure how else to be sure
        # TODO: could be solved by a debugging option to focus dice to roll max then check for 8
        self.assertTrue(1 <= d <= 8)

    def test_fs_dueling_two_handed(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_two_hands(weapons[WeaponId.SPEAR])
        attacker.add_fighting_style(Trait.FIGHTING_STYLE_DUELING)
        set_values([6])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(6, roll_damage(attacker, None, attacker.get_two_hands(), HitType.HIT, None))

    def test_fs_dueling_two_weapons(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_right_hand(weapons[WeaponId.SPEAR])
        attacker.set_left_hand(weapons[WeaponId.DAGGER])
        attacker.add_fighting_style(Trait.FIGHTING_STYLE_DUELING)
        set_values([6])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(6, roll_damage(attacker, None, attacker.get_right_hand(), HitType.HIT, None))

    def test_fs_dueling_shield(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_right_hand(weapons[WeaponId.SPEAR])
        attacker.set_left_hand(armors[ArmorId.SHIELD])
        attacker.add_fighting_style(Trait.FIGHTING_STYLE_DUELING)
        set_values([6])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(8, roll_damage(attacker, None, attacker.get_right_hand(), HitType.HIT, None))

    def test_fs_greatweapon(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        attacker.set_two_hands(weapons[WeaponId.LONGSWORD])
        attacker.add_fighting_style(Trait.FIGHTING_STYLE_GREAT_WEAPON_FIGHTING)
        set_values([1, 10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(10, roll_damage(attacker, None, attacker.get_two_hands(), HitType.HIT, None))


if __name__ == '__main__':
    unittest.main()

"""
test monster damage
"""