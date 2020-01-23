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


if __name__ == '__main__':
    unittest.main()

"""
test monster damage
"""