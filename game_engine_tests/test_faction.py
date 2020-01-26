import unittest
from game_engine.faction import Faction


class TestFaction(unittest.TestCase):
    def test_create_faction(self):
        f = Faction('My Faction', [])
        self.assertIsNotNone(f)


if __name__ == '__main__':
    unittest.main()

