import unittest
from Highscore import HighScore


class Test_HighScore(unittest.TestCase):

    def make_object(self):
        obj = HighScore()
        self.possible_scores = [3, 18, 6, 15]
        for i in range(len(self.possible_scores)):
            obj.checkScore(self.possible_scores[i])
        return obj

    def test_getHighScore(self):
        obj = self.make_object()
        self.assertEqual(obj.getHighScore(), 18)

    def test_getTimesPlayed(self):
        obj = self.make_object()
        self.assertEqual(obj.getTimesPlayed(), len(self.possible_scores))


if __name__ == "__main__":
    unittest.main()
