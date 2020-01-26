import unittest
from unittest.mock import patch

from game_engine.players.player import Player
from game_engine.players.character_builder import CharacterBuilder
from game_engine_tests.dice_side_effects import set_values
from game_engine_tests.dice_side_effects import value
from game_engine.players.classes.fighter import Fighter
from game_engine.players.classes.rogue import Rogue
from game_engine.players.races.human import Human
from game_engine.players.races.halfling import Halfling
from game_engine.types.armor_id import ArmorId
from game_engine.armors import armors
from game_engine.types.armor_type import ArmorType
from game_engine.weapons import weapons
from game_engine.types.weapon_id import WeaponId


class TestPlayer(unittest.TestCase):
    def test_create(self):
        stats, _ = CharacterBuilder.roll_stats()
        player = Player('Radrick', stats, Human(), Fighter())
        self.assertIsNotNone(player)

    def test_halfling_racial_str_mods(self):
        stats, _ = CharacterBuilder.roll_stats()
        player = Player('Radrick', stats, Halfling(), Fighter())
        self.assertEqual(stats[0], player.get_str())

    def test_halfling_racial_dex_mods(self):
        stats, _ = CharacterBuilder.roll_stats()
        player = Player('Radrick', stats, Halfling(), Fighter())
        self.assertEqual(stats[1] + 2, player.get_dex())

    def test_halfling_human_int_mods(self):
        stats, _ = CharacterBuilder.roll_stats()
        player = Player('Radrick', stats, Human(), Fighter())
        self.assertEqual(stats[3] + 1, player.get_int())

    def test_halfling_racial_dex_roll_mod(self):
        # roll a dex of 10, (+0) add 2 for halfling results in a mod of +1
        #              9        10       17       8        9        11
        set_values([3,3,1,3, 2,2,6,1, 6,6,5,2, 2,3,1,3, 5,1,1,3, 2,6,3,3])
        with patch('game_engine.dice._random_int', side_effect=value):
            stats, _ = CharacterBuilder.roll_stats()
            player = Player('Radrick', stats, Halfling(), Fighter())
            self.assertEqual(1, player.get_dex_mod())

    def test_fighter_hp(self):
        #              9        12       17       8        9        11
        set_values([3,3,1,3, 2,4,6,1, 6,6,5,2, 2,3,1,3, 5,1,1,3, 2,6,3,3])
        with patch('game_engine.dice._random_int', side_effect=value):
            stats, _ = CharacterBuilder.roll_stats()
            player = Player('Radrick', stats, Human(), Fighter())
            self.assertEqual(14, player.get_cur_hp())

    def test_ac_naked(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        self.assertEqual(14, player.get_ac())

    def test_ac_naked_shield(self):
        player = Player('Radrick', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        player.set_right_hand(armors[ArmorId.SHIELD])
        self.assertEqual(player.get_ac(), 12)

    def test_ac_heavy_high_dex(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_right_hand(armors[ArmorId.SHIELD])
        player.set_armor(armors[ArmorId.PLATE])
        self.assertEqual(20, player.get_ac())

    def test_medium_armor_dex(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.HIDE])
        self.assertEqual(14, player.get_ac())

    def test_too_weak_no_armor(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        self.assertFalse(player.too_weak_for_armor())

    def test_too_weak_no_requirement(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.LEATHER])
        self.assertFalse(player.too_weak_for_armor())

    def test_too_weak_has_str(self):
        player = Player('Radrick', [13, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.CHAIN_MAIL])
        self.assertFalse(player.too_weak_for_armor())

    def test_too_weak_low_str(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.CHAIN_MAIL])
        self.assertTrue(player.too_weak_for_armor())

    def test_normal_speed(self):
        player = Player('Radrick', [13, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.CHAIN_MAIL])
        self.assertEqual(30, player.get_speed())

    def test_encumbered_speed(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.CHAIN_MAIL])
        self.assertEqual(20, player.get_speed())

    def test_proficient_armor_none(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        self.assertFalse(player.wearing_unproficient_armor())

    def test_proficient_armor(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        player.set_armor(armors[ArmorId.LEATHER])
        self.assertFalse(player.wearing_unproficient_armor())

    def test_not_proficient_armor_none(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        player.set_armor(armors[ArmorId.PLATE])
        self.assertTrue(player.wearing_unproficient_armor())

    def test_no_shield(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        self.assertIsNone(player.get_shield())

    def test_right_shield(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        player.set_right_hand(armors[ArmorId.SHIELD])
        self.assertEqual(ArmorType.SHIELD, player.get_shield().get_type())

    def test_left_shield(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        player.set_left_hand(armors[ArmorId.SHIELD])
        self.assertEqual(ArmorType.SHIELD, player.get_shield().get_type())

    def test_replace(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Rogue())
        player.set_right_hand(weapons[WeaponId.RAPIER])
        player.set_left_hand(armors[ArmorId.SHIELD])
        player.set_left_hand(weapons[WeaponId.DAGGER])
        self.assertEqual(WeaponId.DAGGER, player.get_left_hand().get_id())

    def test_two_hands(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        player.set_right_hand(armors[ArmorId.SHIELD])
        player.set_two_hands(weapons[WeaponId.MAUL])
        self.assertIsNone(player.get_right_hand())
        self.assertEqual(WeaponId.MAUL, player.get_two_hands().get_id())

    def test_spear_one_hand(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        player.set_right_hand(weapons[WeaponId.SPEAR])
        self.assertEqual(WeaponId.SPEAR, player.get_right_hand().get_id())

    def test_spear_two_hands(self):
        player = Player('bob', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        player.set_two_hands(weapons[WeaponId.SPEAR])
        self.assertEqual(WeaponId.SPEAR, player.get_two_hands().get_id())


if __name__ == '__main__':
    unittest.main()
