import unittest
from unittest.mock import patch

from gutlic_arena_server.arena import Arena
from gutlic_arena_server.faction import Faction
from gutlic_arena_server.monsters.goblin import Goblin
from gutlic_arena_server.monsters.orc import Orc


class TestArena(unittest.TestCase):
    def test_create_arena(self):
        f1 = Faction('Goblins', [Goblin()])
        f2 = Faction('Orcs', [Orc()])
        a = Arena([f1, f2])
        self.assertIsNotNone(a)

    def test_initiative(self):
        f1 = Faction('Goblins', [Goblin()])
        f2 = Faction('Orcs', [Orc()])
        a = Arena([f1, f2])
        with patch('gutlic_arena_server.dice._random_int') as mock_roll:
            mock_roll.return_value = 10
            a.determine_initiative_order()
            self.assertIsInstance(a.get_init_order()[0], Goblin)
            self.assertIsInstance(a.get_init_order()[1], Orc)