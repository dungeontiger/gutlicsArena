import unittest
from unittest.mock import patch

from gutlic_arena_server.players.character_builder import CharacterBuilder
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.players.fighter import Fighter
from gutlic_arena_server.players.rogue import Rogue
from gutlic_arena_server.players.human import Human
from gutlic_arena_server.players.halfling import Halfling


class TestCharacterBuilder(unittest.TestCase):
    def test_single_stats_roll(self):
        set_values([3,3,1,3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(CharacterBuilder._roll_stat(), 9)

    def test_roll_all_stats(self):
        set_values([3,3,1,3, 2,4,3,4, 6,6,5,2, 2,3,1,3, 5,1,1,3, 2,6,3,3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            rolls, perfect = CharacterBuilder.roll_stats()
            self.assertEqual(rolls[0], 9)
            self.assertEqual(rolls[1], 11)
            self.assertEqual(rolls[2], 17)
            self.assertEqual(rolls[3], 8)
            self.assertEqual(rolls[4], 9)
            self.assertEqual(rolls[5], 12)
            expected_perfect = (9 + 11 + 17 + 8 + 9 + 12 - 3 * 6) / (15 * 6)
            self.assertEqual(perfect, expected_perfect)

    def test_available_class(self):
        self.assertTrue(isinstance(CharacterBuilder.available_classes()[0], Fighter))

    def test_available_race(self):
        self.assertTrue(isinstance(CharacterBuilder.available_races()[0], Human))

    def test_generate_name(self):
        self.assertEqual(CharacterBuilder.generate_name(Halfling()), 'Halflingnoname')

    def test_generate_name_full(self):
        self.assertEqual(CharacterBuilder.generate_name(Halfling(), True), 'Nameless Halfling')


if __name__ == '__main__':
    unittest.main()
