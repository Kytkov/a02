

"""necessary imports for unittesting"""
import unittest
from game import Game
from dice import Dice
from Intelligence import Intelligence
from player import Player
from Statistics import Statistics


class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()
    
    def test_objects(self):
        self.assertIsInstance(self.game.current_dice, Dice)
        self.assertIsInstance(self.game.current_intelligence, Intelligence)
        self.assertIsInstance(self.game.current_player, Player )
        self.assertIsInstance(self.game.stats, Statistics)


if __name__ == "__main__":
    unittest.main()