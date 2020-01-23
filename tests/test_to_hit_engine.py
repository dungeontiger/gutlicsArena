import unittest
from unittest.mock import patch

from gutlic_arena_server.to_hit_engine import roll_to_hit
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server.monsters.goblin import Goblin
from gutlic_arena_server.types.weapon_id import WeaponId
from gutlic_arena_server.players.races.stout_halfling import StoutHalfling
from gutlic_arena_server.weapons import weapons
from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.players.classes.fighter import Fighter
from gutlic_arena_server.players.classes.rogue import Rogue
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value


class TestToHitEngine(unittest.TestCase):
    def test_simple_to_hit(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([17])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_simple_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.MISS)

    def test_critical_hit(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([20])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.CRITICAL_HIT)

    def test_critical_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([1])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.CRITICAL_MISS)

    def test_lucky(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([1, 17])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_melee(self):
        # will hit if using the str bonus not the dex bonus (or no bonus for that matter)
        # goblin AC is 15
        # proficiency is +2
        # rolls a 10
        # needs a str mod of +3 to hit
        attacker = Player('Bob', [17, 10, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.CLUB]
        set_values([10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_ranged(self):
        # will hit if using the dex bonus not the str bonus (or no bonus for that matter)
        # goblin AC is 15
        # proficiency is +2
        # rolls a 10
        # needs a dex mod of +3 to hit
        attacker = Player('Bob', [10, 17, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.LIGHT_CROSSBOW]
        set_values([10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_finesse_str(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # proficiency is +2
        # rolls a 10
        # needs a str mod of +3 to hit
        attacker = Player('Bob', [17, 10, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_finesse_dex(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # proficiency is +2
        # rolls a 10
        # needs a str mod of +3 to hit
        attacker = Player('Bob', [10, 17, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_finesse_miss(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # proficiency is +2
        # rolls a 10
        # needs a str mod of +3 to hit
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([10])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.MISS)

    def test_proficieny_matters(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # proficiency is +2
        # rolls a 13
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([13])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_proficieny_matters_rogue(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # proficiency is +2
        # rolls a 13
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        target = Goblin()
        attack = weapons[WeaponId.RAPIER]
        set_values([13])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_proficieny_matters_not_rogue(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # rolls a 13
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        target = Goblin()
        attack = weapons[WeaponId.MAUL]
        set_values([13])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.MISS)

"""
    TODO:
    def test_goblin_attack_orc(self):
        attacker = Goblin()
        target = Orc()
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attacker.get_actions()[0], None), HitType.HIT)
"""

if __name__ == '__main__':
    unittest.main()

"""
monster hitting player
"""