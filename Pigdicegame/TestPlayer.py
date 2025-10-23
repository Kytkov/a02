import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """
    Unit tests for the player class.

    This test suite verifies the correct behavior of player methods
    including setting and getting names and scores, as well as handling
    invalid input types.
    """

    def setUp(self):
        """ Set up a new player instance before each test."""
        self.p1 = Player("Marcus")

    def test_set_score(self):
        """ Test setting a valid score and handling invalid score input. """
        self.p1.set_score(0)
        self.assertEqual(self.p1.score, 0)

        with self.assertRaises(ValueError):
            self.p1.set_score("A")

    def test_add_score(self):
        """ Test adding a valid score and handling invalid score input. """
        self.p1.add_score(5)
        self.assertEqual(self.p1.score, 5)

        with self.assertRaises(ValueError):
            self.p1.add_score("A")

    def test_set_name(self):
        """Test setting a valid name and handling invalid name input. """
        self.p1.set_name('Marcus123')
        self.assertEqual(self.p1.name, "Marcus123")

        with self.assertRaises(ValueError):
            self.p1.set_name(8)

    def test_get_name(self):
        """Test retrieving the player's name."""
        self.assertEqual(self.p1.get_name(), "Marcus")

    def test_get_score(self):
        """ Test retrieving the player's score. """
        self.assertEqual(self.p1.get_score(), 0)


if __name__ == "__main__":
    unittest.main()
