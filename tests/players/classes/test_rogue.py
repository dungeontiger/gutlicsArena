import unittest

from gutlic_arena_server.players.classes.rogue import Rogue
from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.weapons import weapons
from gutlic_arena_server.types.weapon_id import WeaponId


class TestFighter(unittest.TestCase):
    def test_weapon_proficiency_longsword(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertTrue(f.is_proficient(weapons[WeaponId.LONGSWORD]))

    def test_weapon_proficiency_club(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertTrue(f.is_proficient(weapons[WeaponId.CLUB]))

    def test_weapon_proficiency_heavy_crossbow(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertFalse(f.is_proficient(weapons[WeaponId.HEAVY_CROSSBOW]))

    def test_weapon_proficiency_maul(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Rogue())
        self.assertFalse(f.is_proficient(weapons[WeaponId.MAUL]))


if __name__ == '__main__':
    unittest.main()
