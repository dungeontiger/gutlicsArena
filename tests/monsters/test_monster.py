import unittest
from unittest.mock import patch

from gutlic_arena_server.monsters.goblin import Goblin
from gutlic_arena_server.monsters.orc import Orc
from gutlic_arena_server.actions.scimitar import Scimitar


class TestMonster(unittest.TestCase):
    """Tests the base class Monster through a Goblin instance"""
    def test_create_goblin(self):
        g = Goblin()
        self.assertIsNotNone(g)

    def test_goblin_name(self):
        g = Goblin()
        self.assertEqual(g.get_name(), 'Goblin')

    def test_goblin_stats(self):
        g = Goblin()
        self.assertEqual(g.get_str(), 8)
        self.assertEqual(g.get_dex(), 14)
        self.assertEqual(g.get_con(), 10)
        self.assertEqual(g.get_int(), 10)
        self.assertEqual(g.get_wis(), 8)
        self.assertEqual(g.get_cha(), 8)

    def test_goblin_str_mod(self):
        g = Goblin()
        self.assertEqual(g.get_str_mod(), -1)
        self.assertEqual(g.get_dex_mod(), 2)
        self.assertEqual(g.get_con_mod(), 0)
        self.assertEqual(g.get_int_mod(), 0)
        self.assertEqual(g.get_wis_mod(), -1)
        self.assertEqual(g.get_cha_mod(), -1)

    def test_rounding_str_mod(self):
        g = Goblin()
        g.str = 13  # just for testing
        self.assertEqual(g.get_str_mod(), 1)

    def test_get_ac(self):
        g = Goblin()
        self.assertEqual(g.get_ac(), 15)

    def test_get_hd(self):
        g = Goblin()
        self.assertEqual(g.get_hd(), '2d6')

    def test_get_hp(self):
        g = Goblin()
        self.assertTrue(2 <= g.get_hp() <= 12)

    def test_goblin_actions(self):
        g = Goblin()
        self.assertIsInstance(g.get_actions()[0], Scimitar)

    def test_create_orc(self):
        o = Orc()
        self.assertIsNotNone(o)

    def test_goblin_initiative(self):
        g = Goblin()
        # goblin next mod
        self.assertTrue(3 <= g.roll_initiative() <= 22)

    def test_goblin_initiative_patch(self):
        g = Goblin()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 10
            self.assertEqual(g.roll_initiative(), 12)


if __name__ == '__main__':
    unittest.main()
