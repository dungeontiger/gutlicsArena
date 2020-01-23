import unittest
from gutlic_arena_server.armors import armors
from gutlic_arena_server.types.armor_type import ArmorType
from gutlic_arena_server.types.armor_id import ArmorId
from gutlic_arena_server.types.roll_type import RollType


class TestWeapons(unittest.TestCase):
    def test_load_armors(self):
        self.assertEqual(len(armors), 13)

    def test_plate(self):
        plate = armors[ArmorId.PLATE]
        self.assertEqual(plate.get_type(), ArmorType.HEAVY_ARMOR)
        self.assertEqual(plate.get_ac(), 18)
        self.assertEqual(plate.get_str_required(), 15)
        self.assertEqual(plate.get_stealth(), RollType.DISADVANTAGE)


if __name__ == '__main__':
    unittest.main()

