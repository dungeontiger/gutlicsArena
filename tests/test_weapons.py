import unittest
from gutlic_arena_server import weapons
from gutlic_arena_server.types.weapon_id import WeaponId


class TestWeapons(unittest.TestCase):
    def test_load_weapons(self):
        self.assertEqual(len(weapons.weapons), 38)

    def test_longsword(self):
        longsword = weapons.weapons[WeaponId.LONGSWORD]
        self.assertEqual(longsword.get_damage(), '1d8')
        self.assertEqual(longsword.get_versatile(), '1d10')
        self.assertEqual(longsword.get_finesse(), False)


if __name__ == '__main__':
    unittest.main()

