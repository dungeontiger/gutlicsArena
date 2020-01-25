import unittest
from unittest.mock import patch

from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.character_builder import CharacterBuilder
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.players.classes.fighter import Fighter
from gutlic_arena_server.players.classes.rogue import Rogue
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.players.races.halfling import Halfling
from gutlic_arena_server.types.armor_id import ArmorId
from gutlic_arena_server.armors import armors


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
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            stats, _ = CharacterBuilder.roll_stats()
            player = Player('Radrick', stats, Halfling(), Fighter())
            self.assertEqual(1, player.get_dex_mod())

    def test_fighter_hp(self):
        #              9        12       17       8        9        11
        set_values([3,3,1,3, 2,4,6,1, 6,6,5,2, 2,3,1,3, 5,1,1,3, 2,6,3,3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            stats, _ = CharacterBuilder.roll_stats()
            player = Player('Radrick', stats, Human(), Fighter())
            self.assertEqual(14, player.get_cur_hp())

    def test_ac_naked(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        self.assertEqual(14, player.get_ac())

    def test_ac_naked_shield(self):
        player = Player('Radrick', [10, 10, 10, 10, 10, 10], Human(), Fighter())
        player.set_shield(armors[ArmorId.SHIELD])
        self.assertEqual(player.get_ac(), 12)

    def test_ac_heavy_high_dex(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_shield(armors[ArmorId.SHIELD])
        player.set_armor(armors[ArmorId.PLATE])
        self.assertEqual(20, player.get_ac())

    def test_medium_armor_dex(self):
        player = Player('Radrick', [10, 18, 10, 10, 10, 10], Human(), Fighter())
        player.set_armor(armors[ArmorId.HIDE])
        self.assertEqual(16, player.get_ac())

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

# non proficient armor

if __name__ == '__main__':
    unittest.main()
