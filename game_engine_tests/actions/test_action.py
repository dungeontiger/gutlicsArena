import unittest
from unittest.mock import patch

from game_engine.monsters.actions.scimitar import Scimitar
from game_engine.monsters.actions.greataxe import Greataxe
from game_engine.types.action_type import ActionType
from game_engine.types.damage_type import DamageType
from game_engine.monsters.orc import Orc
from game_engine_tests.dice_side_effects import set_values
from game_engine_tests.dice_side_effects import value
from game_engine.types.hit_type import HitType


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
        self.assertEqual(s.get_type(), ActionType.MELEE)
        self.assertEqual(s.get_to_hit(), 4)
        self.assertEqual(s.get_damage(), '1d6+2')
        self.assertEqual(s.get_dmg_type(), DamageType.SLASHING)
        self.assertEqual(s.get_reach(), 5)
        self.assertEqual(s.get_targets(), 1)

    def test_critical_hit(self):
        s = Scimitar()
        o = Orc()
        # dice rolls for a critical hit and then max damage of 18
        set_values([20,8,8])
        with patch('game_engine.dice._random_int', side_effect=value):
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
