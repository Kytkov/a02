"""Unit tests for Statistics Class."""

import unittest
from Statistics import Statistics


class TestStatistics(unittest.TestCase):
    """Unit tests for the Statistics class used in the Pig Dice Game."""

    def setUp(self):
        """Create a new Statistics instance before each test."""
        self.stats = Statistics()

    def test_initial_state(self):
        """The object should start with all counters set to zero."""
        self.assertEqual(self.stats.total_rolls, 0)
        self.assertEqual(self.stats.total_ones, 0)
        self.assertEqual(self.stats.total_rounds, 0)
        self.assertEqual(self.stats.total_points, 0)
        self.assertEqual(self.stats.highest_round_score, 0)
        self.assertEqual(self.stats.average_score_per_round(), 0)

    def test_record_roll_increments_total_rolls(self):
        """record_roll() should increment total_rolls for every roll."""
        for _ in range(5):
            self.stats.record_roll(3)
        self.assertEqual(self.stats.total_rolls, 5)

    def test_record_roll_counts_ones_only_when_1(self):
        """total_ones should only increase when the rolled value is 1."""
        self.stats.record_roll(4)
        self.stats.record_roll(1)
        self.stats.record_roll(6)
        self.stats.record_roll(1)
        self.assertEqual(self.stats.total_rolls, 4)
        self.assertEqual(self.stats.total_ones, 2)

    def test_record_round_updates_rounds_and_points(self):
        """record_round() should increase total_rounds.

        and total_points correctly.
        """
        self.stats.record_round(7)
        self.stats.record_round(0)
        self.stats.record_round(12)
        self.assertEqual(self.stats.total_rounds, 3)
        self.assertEqual(self.stats.total_points, 19)

    def test_highest_round_score_tracks_max(self):
        """highest_round_score should always reflect.

        the highest round score recorded.
        """
        for score in [5, 11, 3, 11, 14, 2]:
            self.stats.record_round(score)
        self.assertEqual(self.stats.highest_round_score, 14)

    def test_average_score_per_round_zero_safe(self):
        """average_score_per_round() should safely return 0.

        when no rounds have been played.
        """
        self.assertEqual(self.stats.average_score_per_round(), 0)

    def test_average_score_per_round(self):
        """average_score_per_round() should return the correct average."""
        self.stats.record_round(10)
        self.stats.record_round(5)
        self.stats.record_round(15)
        self.assertAlmostEqual(self.stats.average_score_per_round(),
                               10.0, places=6)

    def test_reset_restores_initial_state(self):
        """reset() should restore all fields to their initial values."""
        # Simulate game activity
        self.stats.record_roll(1)
        self.stats.record_roll(6)
        self.stats.record_round(8)
        self.stats.record_round(0)
        self.assertNotEqual(self.stats.total_rolls, 0)

        # Reset and verify all fields are back to default
        self.stats.reset()
        self.assertEqual(self.stats.total_rolls, 0)
        self.assertEqual(self.stats.total_ones, 0)
        self.assertEqual(self.stats.total_rounds, 0)
        self.assertEqual(self.stats.total_points, 0)
        self.assertEqual(self.stats.highest_round_score, 0)
        self.assertEqual(self.stats.average_score_per_round(), 0)

    def test_str_contains_key_numbers(self):
        """__str__() should include the main statistics.

        fields in the output string.
        """
        self.stats.record_roll(1)   # total_rolls=1, total_ones=1
        self.stats.record_round(9)  # total_rounds=1, total_points=9, highest=9
        s = str(self.stats)
        self.assertIn("Total Rolls: 1", s)
        self.assertIn("Total Ones: 1", s)
        self.assertIn("Total Rounds: 1", s)
        self.assertIn("Total Points: 9", s)
        self.assertIn("Highest Round Score: 9", s)
        self.assertIn("Average Score per Round:", s)


if __name__ == "__main__":
    unittest.main()
