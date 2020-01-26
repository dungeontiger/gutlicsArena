import unittest
from unittest.mock import patch

from game_engine.to_hit_engine import roll_to_hit
from game_engine.types.hit_type import HitType
from game_engine.monsters.goblin import Goblin
from game_engine.types.weapon_id import WeaponId
from game_engine.players.races.stout_halfling import StoutHalfling
from game_engine.weapons import weapons
from game_engine.players.player import Player
from game_engine.players.races.human import Human
from game_engine.players.classes.fighter import Fighter
from game_engine.players.classes.rogue import Rogue
from game_engine_tests.dice_side_effects import set_values
from game_engine_tests.dice_side_effects import value
from game_engine.armors import armors
from game_engine.types.armor_id import ArmorId
from game_engine.types.trait import Trait
from game_engine.monsters.orc import Orc


class TestToHitEngine(unittest.TestCase):
    def test_simple_to_hit(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([17])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_simple_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([3])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.MISS)

    def test_critical_hit(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([20])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.CRITICAL_HIT)

    def test_critical_miss(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([1])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.CRITICAL_MISS)

    def test_lucky(self):
        attacker = Player('Bob', [10, 10, 10, 10, 10, 10], StoutHalfling(), Fighter())
        target = Goblin()
        attack = weapons[WeaponId.DAGGER]
        set_values([1, 17])
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
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
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.HIT)

    def test_proficieny_matters_not_rogue(self):
        # makes sure to use the higher mod to be able to hit
        # goblin AC is 15
        # rolls a 13
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        target = Goblin()
        attack = weapons[WeaponId.MAUL]
        set_values([13])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attack, None), HitType.MISS)

    def test_unproficient_armor(self):
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        target = Goblin()
        attacker.set_armor(armors[ArmorId.PLATE])
        set_values([20, 3])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, weapons[WeaponId.DAGGER], None), HitType.MISS)

    def test_natural_20(self):
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        target = Goblin()
        set_values([20])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, weapons[WeaponId.DAGGER], None), HitType.CRITICAL_HIT)

    def test_natural_1(self):
        attacker = Player('Bob', [18, 18, 17, 17, 17, 17], Human(), Fighter())
        target = Goblin()
        set_values([1])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, weapons[WeaponId.DAGGER], None), HitType.CRITICAL_MISS)

    def test_fs_archery(self):
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        attacker.add_fighting_style(Trait.FIGHTING_STYLE_ARCHERY)
        target = Goblin()
        set_values([11])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, weapons[WeaponId.SHORTBOW], None), HitType.HIT)

    def test_fs_defence_no_armor(self):
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        target = Player('Other Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        target.add_fighting_style(Trait.FIGHTING_STYLE_DEFENCE)
        set_values([8])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, weapons[WeaponId.DAGGER], None), HitType.HIT)

    def test_fs_defence_armor(self):
        attacker = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        target = Player('Other Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        target.add_fighting_style(Trait.FIGHTING_STYLE_DEFENCE)
        target.set_armor(armors[ArmorId.LEATHER])
        set_values([9])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(HitType.MISS, roll_to_hit(attacker, target, weapons[WeaponId.DAGGER], None))

    # monster hitting monster
    def test_goblin_attack_orc(self):
        attacker = Goblin()
        target = Orc()
        set_values([13])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attacker.get_actions()[0], None), HitType.HIT)

    def test_goblin_attack_player(self):
        attacker = Goblin()
        target = Player('Bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        target.set_armor(armors[ArmorId.CHAIN_SHIRT])
        target.set_left_hand(armors[ArmorId.SHIELD])
        set_values([11])
        with patch('game_engine.dice._random_int', side_effect=value):
            self.assertEqual(roll_to_hit(attacker, target, attacker.get_actions()[0], None), HitType.HIT)


if __name__ == '__main__':
    unittest.main()

