import unittest
from Intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """
    Unit tests for the Intelligence class.

    This test suite verifies the functionality of the Intelligence class,
    including score management, name setting, and difficulty handling.
    """

    def setUp(self):
        """
        Set up a new Intelligence instance before each test.
        """
        self.cpu = Intelligence()

    def test_set_score(self):
        """
        Test setting a valid score and handling of invalid input types.
        """
        self.cpu.set_score(1)
        self.assertEqual(self.cpu.get_score(), 1)

        with self.assertRaises(ValueError):
            self.cpu.set_score("B")

    def test_add_score(self):
        """
        Test adding to the score and validating input types.
        """
        result = self.cpu.add_score(2)
        self.assertEqual(result, 2)
        self.assertEqual(self.cpu.get_score(), 2)

        with self.assertRaises(ValueError):
            self.cpu.add_score("C")

    def test_get_score(self):
        """
        Test retrieving the current score.
        """
        self.assertEqual(self.cpu.get_score(), 0)

    def test_get_name(self):
        """
        Test retrieving the name of the Intelligence instance.
        """
        self.assertEqual(self.cpu.get_name(), "CPU")

    def test_set_name(self):
        """
        Test setting a valid name and handling of invalid input types.
        """
        self.assertEqual(self.cpu.set_name("CPU123"), "CPU123")

        with self.assertRaises(ValueError):
            self.cpu.set_name(192)

    def test_set_difficulty(self):
        """
        Test handling of invalid difficulty inputs.
        """
        self.assertEqual(
            self.cpu.set_difficulty("5"), "Incorrect input, Try again."
        )
        self.assertEqual(
            self.cpu.set_difficulty(5), "Incorrect input, Try again."
        )


if __name__ == "__main__":
    unittest.main()