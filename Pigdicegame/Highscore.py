class HighScore:
    """Store player's highscore by score and times played"""

    def __init__(self):
        self.amountOfTimesPlayed = 0
        self.highScore = 0

    def checkScore(self, score):
        """Check if received score is greater than highscore"""
        self.amountOfTimesPlayed += 1
        if score > self.highScore:
            self.highScore = score

    def getHighScore(self):
        """Return player's highscore"""
        return self.highScore

    def getTimesPlayed(self):
        """Return player's number of times played"""
        return self.amountOfTimesPlayed
