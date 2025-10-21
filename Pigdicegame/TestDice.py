import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    """Unit tests for the Dice class to ensure correct initialization and rolling behavior."""

    def test_default_sides(self):
        """Test that a dice is created with 6 sides by default."""
        dice = Dice()
        self.assertEqual(dice.sides, 6)

    def test_custom_sides(self):
        """Test that a dice can be created with a custom number of sides."""
        dice = Dice(10)
        self.assertEqual(dice.sides, 10)

    def test_invalid_sides(self):
        """Test that creating a dice with fewer than 2 sides raises a ValueError."""
        with self.assertRaises(ValueError):
            Dice(1)

    def test_roll_within_range(self):
        """Test that the roll method always returns a value within the valid range."""
        dice = Dice(6)
        for _ in range(100):
            result = dice.roll()
            self.assertTrue(1 <= result <= 6)
