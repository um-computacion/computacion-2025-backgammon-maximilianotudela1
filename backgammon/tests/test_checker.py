import unittest
from backgammon.core.checker import Checker

class TestChecker(unittest.TestCase):
    
    def test_initialization(self):
        white_checker = Checker(0)
        black_checker = Checker(1)
        
        self.assertEqual(white_checker.get_player_id(), 0)
        self.assertEqual(black_checker.get_player_id(), 1)
        
        self.assertFalse(white_checker.is_captured())
        self.assertFalse(white_checker.is_bearing_off())
        self.assertFalse(black_checker.is_captured())
        self.assertFalse(black_checker.is_bearing_off())
    
    def test_capture(self):
        checker = Checker(0)
        
        self.assertFalse(checker.is_captured())
        
        checker.set_captured(True)
        self.assertTrue(checker.is_captured())
        
        checker.set_captured(False)
        self.assertFalse(checker.is_captured())
    
    def test_bearing_off(self):
        checker = Checker(1)
        
        self.assertFalse(checker.is_bearing_off())
        
        checker.set_bearing_off(True)
        self.assertTrue(checker.is_bearing_off())
        
        checker.set_bearing_off(False)
        self.assertFalse(checker.is_bearing_off())
    
    def test_player_id_immutability(self):
        checker = Checker(0)
        self.assertEqual(checker.get_player_id(), 0)
        
        checker.set_captured(True)
        checker.set_bearing_off(True)
        self.assertEqual(checker.get_player_id(), 0)
    
    def test_state_transitions(self):
        checker = Checker(0)
        
        self.assertFalse(checker.is_captured())
        self.assertFalse(checker.is_bearing_off())
        
        checker.set_captured(True)
        self.assertTrue(checker.is_captured())
        self.assertFalse(checker.is_bearing_off())
        
        checker.set_captured(False)
        self.assertFalse(checker.is_captured())
        self.assertFalse(checker.is_bearing_off())
        
        checker.set_bearing_off(True)
        self.assertFalse(checker.is_captured())
        self.assertTrue(checker.is_bearing_off())

if __name__ == '__main__':
    unittest.main()