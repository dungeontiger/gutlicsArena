import unittest
from unittest.mock import patch

from gutlic_arena_server.actions.scimitar import Scimitar
from gutlic_arena_server.actions.greataxe import Greataxe
from gutlic_arena_server.actions.weapon_type import WeaponType
from gutlic_arena_server.types.damage_type import DamageType
from gutlic_arena_server.monsters.orc import Orc
from tests.dice_side_effects import set_values
from tests.dice_side_effects import value
from gutlic_arena_server.types.hit_type import HitType


class TestActions(unittest.TestCase):
    """Test the action base class via a scimitar instance"""
    def test_create_scimitar(self):
        s = Scimitar()
        self.assertIsNotNone(s)

    def test_create_greataxe(self):
        a = Greataxe()
        self.assertIsNotNone(a)

    def test_scimitar_stats(self):
        s = Scimitar()
        self.assertEqual(s.get_name(), 'Scimitar')
        self.assertEqual(s.get_type(), WeaponType.MELEE)
        self.assertEqual(s.get_to_hit(), 4)
        self.assertEqual(s.get_dmg_str(), '1d6+2')
        self.assertTrue(3 <= s.get_dmg() <= 14)
        self.assertEqual(s.get_dmg_type(), DamageType.SLASHING)
        self.assertEqual(s.get_reach(), 5)
        self.assertEqual(s.get_targets(), 1)

    def test_critical_hit(self):
        s = Scimitar()
        o = Orc()
        # dice rolls for a critical hit and then max damage of 18
        set_values([20,8,8])
        with patch('gutlic_arena_server.dice._random_int', side_effect=value):
            hit = s.roll_to_hit(o)
            s.roll_damage(o, hit)
            self.assertEqual(o.cur_hp, o.get_hp() - 18)

    def test_miss_damage(self):
        s = Scimitar()
        o = Orc()
        s.roll_damage(o, HitType.MISS)
        self.assertEqual(o.get_cur_hp(), o.get_hp())


if __name__ == '__main__':
    unittest.main()
