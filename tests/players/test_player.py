import unittest
from unittest.mock import patch

from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.character_builder import CharacterBuilder
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.players.fighter import Fighter
from gutlic_arena_server.players.rogue import Rogue
from gutlic_arena_server.players.human import Human
from gutlic_arena_server.players.halfling import Halfling


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


if __name__ == '__main__':
    unittest.main()
