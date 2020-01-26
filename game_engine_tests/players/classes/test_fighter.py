import unittest

from game_engine.players.classes.fighter import Fighter
from game_engine.players.player import Player
from game_engine.players.races.human import Human
from game_engine.armors import armors
from game_engine.weapons import weapons
from game_engine.types.weapon_id import WeaponId
from game_engine.types.armor_id import ArmorId


class TestFighter(unittest.TestCase):
    def test_weapon_proficiency(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        self.assertTrue(f.is_weapon_proficient(weapons[WeaponId.LONGSWORD]))

    def test_armor_proficiency(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        self.assertTrue(f.is_armor_proficient(armors[ArmorId.BREASTPLATE]))

    def test_shield_proficiency(self):
        f = Player('Bob', [10, 10, 17, 17, 17, 17], Human(), Fighter())
        self.assertTrue(f.is_armor_proficient(armors[ArmorId.SHIELD]))

if __name__ == '__main__':
    unittest.main()
