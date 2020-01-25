import unittest

from gutlic_arena_server.players.classes.rogue import Rogue
from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.weapons import weapons
from gutlic_arena_server.types.weapon_id import WeaponId
from gutlic_arena_server.armors import armors
from gutlic_arena_server.types.armor_id import ArmorId


class TestFighter(unittest.TestCase):
    def test_weapon_proficiency_longsword(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertTrue(f.is_weapon_proficient(weapons[WeaponId.LONGSWORD]))

    def test_weapon_proficiency_club(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertTrue(f.is_weapon_proficient(weapons[WeaponId.CLUB]))

    def test_weapon_proficiency_heavy_crossbow(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertFalse(f.is_weapon_proficient(weapons[WeaponId.HEAVY_CROSSBOW]))

    def test_weapon_proficiency_maul(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertFalse(f.is_weapon_proficient(weapons[WeaponId.MAUL]))

    def test_armor_proficiency_plate(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertTrue(f.is_armor_proficient(armors[ArmorId.LEATHER]))

    def test_shield_proficiency(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertFalse(f.is_armor_proficient(armors[ArmorId.SHIELD]))


if __name__ == '__main__':
    unittest.main()
