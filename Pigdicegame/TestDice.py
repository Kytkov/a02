import unittest
from dice import Dice


class TestDice(unittest.TestCase):

    def test_default_sides(self):
        dice = Dice()
        self.assertEqual(dice.sides, 6)

    def test_custom_sides(self):
        dice = Dice(10)
        self.assertEqual(dice.sides, 10)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Dice(1)

    def test_roll_within_range(self):
        dice = Dice(6)
        for _ in range(100):
            result = dice.roll()
            self.assertTrue(1 <= result <= 6)
