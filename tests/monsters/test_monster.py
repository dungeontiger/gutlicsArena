import unittest
from unittest.mock import patch

from gutlic_arena_server.monsters.goblin import Goblin
from gutlic_arena_server.monsters.orc import Orc
from gutlic_arena_server.actions.scimitar import Scimitar
from gutlic_arena_server.actions.hit_type import HitType
from gutlic_arena_server.faction import Faction
from gutlic_arena_server.arena import Arena
from gutlic_arena_server.monsters.target_strategy import TargetStrategy
from gutlic_arena_server.monsters.entity_state import EntityState

"""Tests the base class Monster through a Goblin instance"""


class TestMonster(unittest.TestCase):
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
        # goblin dex mod
        self.assertTrue(3 <= g.roll_initiative() <= 22)

    def test_goblin_initiative_patch(self):
        g = Goblin()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 10
            self.assertEqual(g.roll_initiative(), 12)

    def test_random_target(self):
        g = Goblin()
        o1 = Orc()
        o2 = Orc()
        o3 = Orc()
        goblins = Faction('Goblins', [g])
        orcs = Faction('Orcs', [o1, o2, o3])
        arena = Arena([goblins, orcs])
        # this is only for testing, need to set the arena on the goblin
        # normally this would happen via the take_turn method
        g.arena = arena
        g.select_target(TargetStrategy.RANDOM)
        self.assertTrue(g.target is not None)
        self.assertIn(g.target, [o1, o2, o3])

    def test_roll_to_hit(self):
        s = Scimitar()
        o = Orc()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 3
            roll = s.roll_to_hit(o)
            self.assertEqual(roll, HitType.MISS)

    def test_roll_to_hit_critical(self):
        s = Scimitar()
        o = Orc()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 20
            roll = s.roll_to_hit(o)
            self.assertEqual(roll, HitType.CRITICAL_HIT)

    def test_roll_damage(self):
        s = Scimitar()
        o = Orc()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 3  # means 5 damage
            s.roll_damage(o)
            self.assertEqual(o.get_cur_hp(), o.get_hp() - 5)
            self.assertEqual(o.get_state(), EntityState.NORMAL)

    def test_death(self):
        s = Scimitar()
        o = Orc()
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 100    # rolling 100 on a d6?  Anyway this will kill the orc
            s.roll_damage(o)
            self.assertTrue(o.get_cur_hp() < 1)
            self.assertEqual(o.get_state(), EntityState.DEAD)


if __name__ == '__main__':
    unittest.main()
