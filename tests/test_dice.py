import unittest
from unittest.mock import patch
from gutlic_arena_server import dice
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server.types.roll_type import RollType


class TestDice(unittest.TestCase):

    def test_random_int(self):
        r = dice._random_int(1, 4)
        self.assertTrue(1 <= r <= 4)

    def test_d20(self):
        self.assertTrue(1 <= dice.d20() <= 20)

    def test_d20_mock(self):
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 35
            self.assertEqual(dice.d20(), 35)

    def test_roll_dice(self):
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 10
            self.assertEqual(dice.roll_dice(3, 99, 5), 35)

    def test_simple_hd(self):
        hp = dice.roll('2d6 + 1')
        self.assertTrue(3 <= hp <= 13)

    def test_hd_again(self):
        hp = dice.roll('2D6')
        self.assertTrue(2 <= hp <= 12)

    """Really this is just to be sure I can simulate a set of dice rolls, not just a single one."""
    def test_side_effects(self):
        set_values([20,15,10,3])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(dice.d20(), 20)
            self.assertEqual(dice.d20(), 15)
            self.assertEqual(dice.d20(), 10)
            self.assertEqual(dice.d20(), 3)

    def test_critical_hit(self):
        set_values([8,8])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(dice.roll_damage('1d8 + 2', HitType.CRITICAL_HIT), 18)

    def test_advantage(self):
        set_values([10, 15])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(dice.d20(RollType.ADVANTAGE), 15)

    def test_disadvantage(self):
        set_values([10, 15])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            self.assertEqual(dice.d20(RollType.DISADVANTAGE), 10)


if __name__ == '__main__':
    unittest.main()
