import unittest
from Intelligence import Intelligence


class TestIntelligence(unittest.TestCase):

    def setUp(self):
        self.cpu = Intelligence()

    def test_set_score(self):
        self.cpu.set_score(1)
        self.assertEqual(self.cpu.get_score(), 1)

        with self.assertRaises(ValueError):
            self.cpu.set_score("B")

    def test_add_score(self):
        result = self.cpu.add_score(2)
        self.assertEqual(result, 2)
        self.assertEqual(self.cpu.get_score(), 2)

        with self.assertRaises(ValueError):
            self.cpu.add_score("C")

    def test_get_score(self):
        self.assertEqual(self.cpu.get_score(), 0)

    def test_get_name(self):
        self.assertEqual(self.cpu.get_name(), "CPU")

    def test_set_name(self):
        self.assertEqual(self.cpu.set_name("CPU123"), "CPU123")

        with self.assertRaises(ValueError):
            self.cpu.set_name(192)

    def test_set_difficulty(self):
        self.assertEqual(
            self.cpu.set_difficulty("5"), "Incorrect input, Try again."
        )
        self.assertEqual(
            self.cpu.set_difficulty(5), "Incorrect input, Try again."
        )


if __name__ == "__main__":
    unittest.main()
