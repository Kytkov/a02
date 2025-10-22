"""Unit tests for the DiceHand used in the Pig dice game.

These tests focus on construction, rolling with/without hold masks,
cheat scheduling, and helper behaviors like `values`, `sum`, and
`pig_out`.
"""

import unittest
import random

try:
    from dicehand import DiceHand  # package style
except Exception:
    from dicehand import DiceHand  # flat style


class TestDiceHand(unittest.TestCase):
    """Test suite for DiceHand behaviors."""

    def setUp(self):
        """Create a deterministic RNG for tests that need stability."""
        self.rng = random.Random(123)

    def test_init_defaults(self):
        """`DiceHand` defaults: 1 die, 6 sides, and no previous values."""
        dh = DiceHand()
        self.assertEqual(dh.count, 1)
        self.assertEqual(dh.sides, 6)
        self.assertEqual(dh.values(), [])

    def test_invalid_init(self):
        """Invalid constructor arguments should raise ValueError."""
        with self.assertRaises(ValueError):
            DiceHand(0)
        with self.assertRaises(ValueError):
            DiceHand(1, sides=1)

    def test_roll_single_die_deterministic(self):
        """Roll one die with an injected RNG; values in range and update."""
        dh = DiceHand(count=1, sides=6, rng=self.rng)
        vals1 = dh.roll()
        self.assertEqual(len(vals1), 1)
        self.assertTrue(1 <= vals1[0] <= 6)
        self.assertEqual(dh.values(), vals1)
        vals2 = dh.roll()
        self.assertNotEqual(vals1, vals2)  # likely different with RNG

    def test_roll_multiple_with_hold_mask(self):
        """Hold mask keeps True-indexed dice and re-rolls others."""
        dh = DiceHand(count=3, rng=self.rng)
        first = dh.roll()
        self.assertEqual(len(first), 3)
        # Hold middle die, re-roll others
        second = dh.roll(hold=[False, True, False])
        self.assertEqual(second[1], first[1])  # held
        # Others may change or not; ensure range valid
        for v in second:
            self.assertTrue(1 <= v <= 6)

    def test_hold_mask_validation(self):
        """Hold mask must be correct length and boolean-only."""
        dh = DiceHand(count=2, rng=self.rng)
        with self.assertRaises(ValueError):
            dh.roll(hold=[True])  # wrong length
        with self.assertRaises(TypeError):
            dh.roll(hold=[1, 0])  # not booleans

    def test_sum_and_pig_out(self):
        """Cheat to a known roll; verify sum and pig_out detection."""
        dh = DiceHand(count=3, rng=self.rng)
        dh.schedule_cheat([1, 3, 5])
        vals = dh.roll()
        self.assertEqual(vals, [1, 3, 5])
        self.assertTrue(dh.pig_out())
        self.assertEqual(dh.sum(), 9)

    def test_schedule_cheat_validates(self):
        """schedule_cheat validates length and integer types."""
        dh = DiceHand(count=2)
        with self.assertRaises(ValueError):
            dh.schedule_cheat([6])  # size mismatch
        with self.assertRaises(TypeError):
            dh.schedule_cheat([6, "x"])  # non-int

    def test_cheat_applies_once(self):
        """Cheat affects only the next roll; then clears."""
        dh = DiceHand(count=2, rng=self.rng)
        dh.schedule_cheat([2, 2])
        first = dh.roll()
        self.assertEqual(first, [2, 2])
        second = dh.roll()
        # After cheat cleared, values should be in valid range but not forced
        self.assertTrue(all(1 <= v <= 6 for v in second))
        self.assertNotEqual(first, second)

    def test_values_is_copy(self):
        """values() returns a copy; external mutation won't leak back."""
        dh = DiceHand(count=2, rng=self.rng)
        vals = dh.roll()
        vals.append(99)
        self.assertNotEqual(vals, dh.values())

    def test_cheat_out_of_range_rejected(self):
        """Out-of-range cheat values should trigger a ValueError."""
        # For a 6-sided die, 0 and 7 are invalid
        dh = DiceHand(count=2, sides=6)
        dh.schedule_cheat([0, 7])  # schedule invalid values
        with self.assertRaises(ValueError):
            dh.roll()  # applying the cheat should raise


if __name__ == "__main__":
    unittest.main()
