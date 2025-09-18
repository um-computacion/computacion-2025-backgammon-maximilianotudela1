import unittest
from backgammon.core.dice import Dice

class TestDice(unittest.TestCase):
    
    def setUp(self):
        self.dice = Dice()
    
    def test_initialization(self):
        self.assertEqual(self.dice.values, [])
        self.assertEqual(self.dice.get_available_moves(), [])
    
    def test_roll(self):
        values = self.dice.roll()
        self.assertEqual(len(values), 2)
        for value in values:
            self.assertTrue(1 <= value <= 6)
        self.assertEqual(self.dice.values, values)
    
    def test_roll_doubles(self):
        self.dice.values = []
        self.dice.values = [3, 3]
        available = self.dice.get_available_moves()
        self.assertEqual(available, [3, 3, 3, 3])
    
    def test_use_value(self):
        self.dice.values = [3, 5]
        self.assertTrue(self.dice.use_value(3))
        self.assertEqual(self.dice.get_available_moves(), [5])
        self.assertTrue(self.dice.use_value(5))
        self.assertEqual(self.dice.get_available_moves(), [])
    
    def test_use_invalid_value(self):
        self.dice.values = [2, 4]
        self.assertFalse(self.dice.use_value(6))
        self.assertEqual(self.dice.get_available_moves(), [2, 4])
    
    def test_reset(self):
        self.dice.values = [1, 6]
        self.dice.reset()
        self.assertEqual(self.dice.values, [])
        self.assertEqual(self.dice.get_available_moves(), [])
    
    def test_has_moves(self):
        self.assertFalse(self.dice.has_moves())
        self.dice.values = [3, 4]
        self.assertTrue(self.dice.has_moves())
        self.dice.use_value(3)
        self.dice.use_value(4)
        self.assertFalse(self.dice.has_moves())

if __name__ == '__main__':
    unittest.main() 