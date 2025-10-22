"""necessary imports for unittesting."""

import unittest
from Game import Game
from dice import Dice
from Intelligence import Intelligence
from player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_objects(self):
        self.assertIsInstance(self.game.current_dice, Dice)
        self.assertIsInstance(self.game.current_intelligence, Intelligence)
        self.assertIsInstance(self.game.current_player, Player)


if __name__ == "__main__":
    unittest.main()
