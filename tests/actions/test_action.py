import unittest
from gutlic_arena_server.actions.scimitar import Scimitar
from gutlic_arena_server.actions.greataxe import Greataxe
from gutlic_arena_server.actions.weapon_type import WeaponType
from gutlic_arena_server.actions.damage_type import DamageType


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


if __name__ == '__main__':
    unittest.main()
