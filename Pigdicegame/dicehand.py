"""Dice hand module for Pig dice game.

This module defines :class:`DiceHand`, an object that manages one or more
dice (instances of :class:`Dice`), provides rolling utilities, a small
cheat hook for testing, and helpers commonly needed in Pig variants,
e.g. detecting a "pig out" (any 1) and computing the roll sum.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Sequence

import random

try:
    # Local dice module in the same package
    from .dice import Dice  # type: ignore
except Exception:  # pragma: no cover - fallback for flat-file layout
    from dice import Dice  # type: ignore


@dataclass
class DiceHand:
    """A hand of N dice.

    Parameters
    ----------
    count:
        Number of dice in the hand. Must be >= 1.
    sides:
        Number of sides per die (each die is identical).
    rng:
        Optional :class:`random.Random` instance for deterministic testing.
    """

    count: int = 1
    sides: int = 6
    rng: Optional[random.Random] = None
    _dice: List[Dice] = field(init=False, repr=False)
    _last: List[int] = field(default_factory=list, init=False, repr=False)
    _cheat_next: Optional[List[int]] = field(
        default=None, init=False, repr=False
        )

    def __post_init__(self) -> None:
        """Validate inputs and initialize dice list."""
        if not isinstance(self.count, int) or self.count < 1:
            raise ValueError("count must be an integer >= 1")
        if not isinstance(self.sides, int) or self.sides < 2:
            raise ValueError("sides must be an integer >= 2")

        # Create dice; each die uses randint from the shared RNG if provided.
        self._dice = [Dice(self.sides) for _ in range(self.count)]

    # --------------------------- public API ---------------------------
    def roll(self, hold: Optional[Sequence[bool]] = None) -> List[int]:
        """Roll the dice in the hand and store the values.

        Parameters
        ----------
        hold:
            Optional boolean mask the same length as the hand. ``True``
            means *hold* (keep previous value); ``False`` means re-roll.
            If omitted, all dice are rolled.

        Returns
        -------
        list[int]
            The list of face values after the roll.
        """
        if hold is not None:
            if len(hold) != self.count:
                raise ValueError("hold mask must match dice count")
            if not all(isinstance(b, bool) for b in hold):
                raise TypeError("hold must be a sequence of booleans")

        # Start from previous if we have them; otherwise initialize with 0s.
        cur = list(self._last) if self._last else [0] * self.count

        # Apply cheat if scheduled
        if self._cheat_next is not None:
            vals = self._cheat_next
            if (
                len(vals) != self.count
                or any(not (1 <= v <= self.sides) for v in vals)
            ):
                raise ValueError(
                    "cheat values must be within dice range "
                    "and match hand size"
                )
            self._last = list(vals)
            self._cheat_next = None
            return list(self._last)

        # Roll
        for i in range(self.count):
            should_roll = True
            if hold is not None and hold[i] is True and cur[i] != 0:
                should_roll = False
            if should_roll:
                cur[i] = self._randint(1, self.sides)
        self._last = cur
        return list(self._last)

    def values(self) -> List[int]:
        """Return the most recent roll values; empty list if never rolled."""
        return list(self._last)

    def sum(self) -> int:
        """Return the sum of the current face values (0 if never rolled)."""
        return sum(self._last)

    def pig_out(self) -> bool:
        """Return True if any die shows 1 (Pig 'pig out' condition)."""
        return any(v == 1 for v in self._last)

    def schedule_cheat(self, values: Iterable[int]) -> None:
        """Schedule a cheating roll with the provided values.

        The cheat applies to the *next* call to :meth:`roll` and then is
        cleared. Useful to reach end-game states deterministically while
        testing the outer game loop.
        """
        vals = list(values)
        if len(vals) != self.count:
            raise ValueError("cheat values must match dice count")
        if any(not isinstance(v, int) for v in vals):
            raise TypeError("cheat values must be integers")
        self._cheat_next = vals

    # --------------------------- helpers ---------------------------
    def _randint(self, a: int, b: int) -> int:
        """Return a random int using the injected RNG if present(for tests)."""
        if self.rng is None:
            return random.randint(a, b)
        return self.rng.randint(a, b)
