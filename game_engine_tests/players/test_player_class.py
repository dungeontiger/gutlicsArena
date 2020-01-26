import unittest
from game_engine.players.player_class import PlayerClass
from game_engine.types.languages import Languages
from game_engine.types.weapon_type import WeaponType
from game_engine.types.weapon_id import WeaponId
from game_engine.weapons import weapons
from game_engine.types.armor_type import ArmorType
from game_engine.types.armor_id import ArmorId
from game_engine.armors import armors


class MyTestCase(unittest.TestCase):
    def test_language(self):
        c = PlayerClass('Bob', 10)
        c.add_languages([Languages.COMMON, Languages.ORC])
        self.assertTrue(Languages.ORC in c.get_languages())

    def test_weapon_proficiency(self):
        c = PlayerClass('Bob', 10)
        c.add_weapon_proficiencies([WeaponType.SIMPLE_RANGED, WeaponId.GREATSWORD])
        self.assertTrue(c.is_weapon_proficient(weapons[WeaponId.SHORTBOW]))
        self.assertTrue(c.is_weapon_proficient(weapons[WeaponId.GREATSWORD]))
        self.assertFalse(c.is_weapon_proficient(weapons[WeaponId.MAUL]))
        self.assertFalse(c.is_weapon_proficient(weapons[WeaponId.HEAVY_CROSSBOW]))

    def test_armor_proficiency(self):
        c = PlayerClass('Bob', 10)
        c.add_armor_proficiencies([ArmorType.MEDIUM_ARMOR, ArmorId.SPLINT])
        self.assertTrue(c.is_armor_proficient(armors[ArmorId.HIDE]))
        self.assertTrue(c.is_armor_proficient(armors[ArmorId.SPLINT]))
        self.assertFalse(c.is_armor_proficient(armors[ArmorId.LEATHER]))
        self.assertFalse(c.is_armor_proficient(armors[ArmorId.PLATE]))

    def test_level_1(self):
        c = PlayerClass('Bob', 10)
        self.assertEqual(1, c.get_level())

    def test_level_1_more(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(150)
        self.assertEqual(1, c.get_level())

    def test_level_2(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(300)
        self.assertEqual(2, c.get_level())

    def test_level_2_more(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(375)
        self.assertEqual(2, c.get_level())

    def test_level_3(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(1000)
        self.assertEqual(3, c.get_level())

    def test_level_10(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(80000)
        self.assertEqual(10, c.get_level())

    def test_level_19(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(305000)
        self.assertEqual(19, c.get_level())

    def test_level_20(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(355000)
        self.assertEqual(20, c.get_level())

    def test_level_20_more(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(1000000)
        self.assertEqual(20, c.get_level())

    def test_1_proficiency_bonus(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(150)
        self.assertEqual(2, c.get_proficiency_bonus())

    def test_2_proficiency_bonus(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(300)
        self.assertEqual(2, c.get_proficiency_bonus())

    def test_4_proficiency_bonus(self):
        c = PlayerClass('Bob', 10)
        c.add_exp(90000)
        self.assertEqual(4, c.get_proficiency_bonus())


if __name__ == '__main__':
    unittest.main()
