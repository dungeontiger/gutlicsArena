import unittest
from unittest.mock import patch
from game_engine.game import Game
from game_engine.monsters.goblin import Goblin
from game_engine.monsters.orc import Orc
from game_engine.faction import Faction
from game_engine_tests.dice_side_effects import set_values
from game_engine_tests.dice_side_effects import value


class TestGame(unittest.TestCase):
    def test_goblin_vs_orc(self):
        # this means hp rolls, initiative rolls, to hit roll and damage rolls until one dead
        set_values([3,3,4,4,20,10,10,3,10,8])
        with patch('game_engine.dice._random_int', side_effect=value):
            f1 = Faction('Goblins', [Goblin()])
            f2 = Faction('Orcs', [Orc()])
            game = Game([f1, f2])
            winner = game.play()
            self.assertEqual(winner.get_name(), 'Orcs')


if __name__ == '__main__':
    unittest.main()

