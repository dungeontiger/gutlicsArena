import unittest
from gutlic_arena_server.faction import Faction


class TestFaction(unittest.TestCase):
    def test_create_faction(self):
        f = Faction('My Faction', [])
        self.assertIsNotNone(f)
