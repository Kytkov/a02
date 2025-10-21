import random


class Dice:
    """Creates a six sided dice."""    
    def __init__(self, sides=6):
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    """Return a random number between 1 and 6."""
    def roll(self):
        return random.randint(1, self.sides)
