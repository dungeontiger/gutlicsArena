import unittest
from unittest.mock import patch

from gutlic_arena_server.arena import Arena
from gutlic_arena_server.faction import Faction
from gutlic_arena_server.monsters.goblin import Goblin
from gutlic_arena_server.monsters.orc import Orc
from gutlic_arena_server.types.entity_state import EntityState


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

    def test_get_opposing_factions(self):
        f1 = Faction('Goblins', [Goblin()])
        f2 = Faction('Orcs', [Orc()])
        f3 = Faction('More Bad Orcs', [Orc()])
        a = Arena([f1, f2, f3])
        opposing = a.get_opposing_factions(f1)
        self.assertNotIn(f1, opposing)

    def test_is_not_over(self):
        f1 = Faction('Goblins', [Goblin(), Goblin()])
        f2 = Faction('Orcs', [Orc(), Orc()])
        f3 = Faction('More Bad Orcs', [Orc(), Orc()])
        a = Arena([f1, f2, f3])
        # kill the first faction and then one from the other two
        f1.get_entities()[0].state = EntityState.DEAD
        f1.get_entities()[1].state = EntityState.DEAD
        f2.get_entities()[0].state = EntityState.DEAD
        f3.get_entities()[1].state = EntityState.DEAD
        self.assertFalse(a.is_over())

    def test_is_over(self):
        f1 = Faction('Goblins', [Goblin(), Goblin()])
        f2 = Faction('Orcs', [Orc(), Orc()])
        a = Arena([f1, f2])
        f1.get_entities()[0].state = EntityState.DEAD
        f1.get_entities()[1].state = EntityState.DEAD
        self.assertTrue(a.is_over())

    def test_get_winning_faction(self):
        f1 = Faction('Goblins', [Goblin(), Goblin()])
        f2 = Faction('Orcs', [Orc(), Orc()])
        a = Arena([f1, f2])
        f1.get_entities()[0].state = EntityState.DEAD
        f1.get_entities()[1].state = EntityState.DEAD
        self.assertEqual(a.get_winning_faction(), f2)

    def test_all_factions_dead(self):
        f1 = Faction('Goblins', [Goblin(), Goblin()])
        f2 = Faction('Orcs', [Orc(), Orc()])
        a = Arena([f1, f2])
        f1.get_entities()[0].state = EntityState.DEAD
        f1.get_entities()[1].state = EntityState.DEAD
        f2.get_entities()[0].state = EntityState.DEAD
        f2.get_entities()[1].state = EntityState.DEAD
        self.assertIsNone(a.get_winning_faction())

    def test_no_winning_faction_yet(self):
        f1 = Faction('Goblins', [Goblin(), Goblin()])
        f2 = Faction('Orcs', [Orc(), Orc()])
        a = Arena([f1, f2])
        self.assertIsNone(a.get_winning_faction())


if __name__ == '__main__':
    unittest.main()
