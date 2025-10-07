import random
from typing import Optional

class Dice:
    """En vanlig sexsidig tärning."""

    def __init__(self, rng: Optional[random.Random] = None) -> None:
        self._rng = rng or random.Random()

    def roll(self) -> int:
        return self._rng.randint(1, 6)

if __name__ == "__main__":
    d = Dice()
    print(d.roll())
