"""Statistics Class."""


class Statistics:
    """Tracks player and game statistics for Pig Dice Game."""

    def __init__(self):
        """Test."""
        self.total_rolls = 0
        self.total_ones = 0
        self.total_rounds = 0
        self.total_points = 0
        self.highest_round_score = 0

    def record_roll(self, roll_value):
        """Record each dice roll and check if it was a 1."""
        self.total_rolls += 1
        if roll_value == 1:
            self.total_ones += 1

    def record_round(self, round_score):
        """Record stats for a finished round."""
        self.total_rounds += 1
        self.total_points += round_score
        if round_score > self.highest_round_score:
            self.highest_round_score = round_score

    def average_score_per_round(self):
        """Return the average score per round."""
        if self.total_rounds == 0:
            return 0
        return self.total_points / self.total_rounds

    def reset(self):
        """Reset all statistics."""
        self.__init__()

    def __str__(self):
        """Return a formatted summary of statistics."""
        avg = self.average_score_per_round()
        return (
            f"--- Game Statistics ---\n"
            f"Total Rolls: {self.total_rolls}\n"
            f"Total Ones: {self.total_ones}\n"
            f"Total Rounds: {self.total_rounds}\n"
            f"Total Points: {self.total_points}\n"
            f"Highest Round Score: {self.highest_round_score}\n"
            f"Average Score per Round: {avg:.2f}"
        )
