import unittest
from player import player

class TestPlayer(unittest.TestCase):
    

    def setUp(self):
        self.p1 = player('Marcus')

    def test_set_score(self):
        self.p1.set_score(0)
        self.assertEqual(self.p1.score, 0)

        with self.assertRaises(ValueError):
            self.p1.set_score('A')
    
    def test_add_score(self):
        self.assertEqual(self.p1.add_score(5),5)
        
        with self.assertRaises(ValueError):
            self.p1.add_score('A')

    def test_set_name(self):
        self.assertEqual(self.p1.set_name('Marcus123'),'Marcus123')
        with self.assertRaises(ValueError):
            self.p1.set_name(8)
            

    def test_get_name(self):
        self.assertEqual(self.p1.get_name(),'Marcus')

    def test_get_score(self):
        self.assertEqual(self.p1.get_score(), 0)

if __name__ == '__main__':
    unittest.main()