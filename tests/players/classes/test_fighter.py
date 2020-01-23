import unittest

from gutlic_arena_server.players.classes.fighter import Fighter
from gutlic_arena_server.players.player import Player
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.weapons import weapons
from gutlic_arena_server.types.weapon_id import WeaponId


class TestFighter(unittest.TestCase):
    def test_weapon_proficiency(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        self.assertTrue(f.is_proficient(weapons[WeaponId.LONGSWORD]))


if __name__ == '__main__':
    unittest.main()
