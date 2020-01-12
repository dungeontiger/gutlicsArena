import unittest
from unittest.mock import patch
from gutlic_arena_server import dice


class TestMonster(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
