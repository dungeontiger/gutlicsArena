import unittest
from gutlic_arena_server.monsters.goblin import Goblin


class TestMonster(unittest.TestCase):
    """Tests the base class Monster through a Goblin instance"""
    def test_create_goblin(self):
        g = Goblin()

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


if __name__ == '__main__':
    unittest.main()
