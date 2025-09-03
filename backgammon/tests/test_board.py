import unittest
from backgammon.core.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        
    def test_initial_position(self):
        # Verifica la configuración inicial del tablero
        self.assertEqual(self.board.points[0], 2)
        self.assertEqual(self.board.points[5], -5)
        self.assertEqual(self.board.points[7], -3)
        self.assertEqual(self.board.points[11], 5)
        self.assertEqual(self.board.points[12], -5)
        self.assertEqual(self.board.points[16], 3)
        self.assertEqual(self.board.points[18], 5)
        self.assertEqual(self.board.points[23], -2)
        
    def test_get_point(self):
        self.assertEqual(self.board.get_point(0), 2)
        self.assertEqual(self.board.get_point(5), -5)
        
        with self.assertRaises(ValueError):
            self.board.get_point(-1)
        with self.assertRaises(ValueError):
            self.board.get_point(24)
            
    def test_get_pieces_on_bar(self):
        self.assertEqual(self.board.get_pieces_on_bar(True), 0)
        self.assertEqual(self.board.get_pieces_on_bar(False), 0)
        
        self.board.bar[0] = 2  
        self.board.bar[1] = 1  
        
        self.assertEqual(self.board.get_pieces_on_bar(True), 2)
        self.assertEqual(self.board.get_pieces_on_bar(False), 1)
        
    def test_get_pieces_at_home(self):
        self.assertEqual(self.board.get_pieces_at_home(True), 0)
        self.assertEqual(self.board.get_pieces_at_home(False), 0)
        
        self.board.home[0] = 3  
        self.board.home[1] = 2  
        
        self.assertEqual(self.board.get_pieces_at_home(True), 3)
        self.assertEqual(self.board.get_pieces_at_home(False), 2)
        
    def test_move_piece_normal(self):
        
        self.assertTrue(self.board.move_piece(0, 1, True))
        self.assertEqual(self.board.points[0], 1)  
        self.assertEqual(self.board.points[1], 1) 
        
    def test_move_piece_hit_opponent(self):
        self.board.points[2] = -1
        
        self.assertTrue(self.board.move_piece(0, 2, True))
        self.assertEqual(self.board.points[0], 1) 
        self.assertEqual(self.board.points[2], 1)  
        self.assertEqual(self.board.bar[1], 1)     
        
    def test_move_from_bar(self):
        self.board.bar[0] = 1  
        self.assertTrue(self.board.move_piece(-1, 0, True))
        self.assertEqual(self.board.bar[0], 0)     
        self.assertEqual(self.board.points[0], 3)  
        
    def test_invalid_moves(self):
        self.assertFalse(self.board.move_piece(1, 2, True))  
        
        self.assertFalse(self.board.is_valid_move(0, 5, True))  
        
    def test_bear_off_allowed(self):
        self.board = Board()  
        
        self.board.points = [0] * 24
        self.board.points[18] = 5
        self.board.points[19] = 5
        self.board.points[20] = 5
        
        self.assertTrue(self.board.can_bear_off(True))
        
        self.assertTrue(self.board.move_piece(18, 24, True))
        self.assertEqual(self.board.points[18], 4)
        self.assertEqual(self.board.home[0], 1)
        
    def test_bear_off_not_allowed(self):
        self.assertFalse(self.board.can_bear_off(True))
        
        board = Board()
        board.points = [0] * 24
        board.points[20] = 15  
        board.bar[0] = 1      
        self.assertFalse(board.can_bear_off(True))
        
if __name__ == '__main__':
    unittest.main()