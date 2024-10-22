import unittest
from unittest import mock
from peon import Peon

class TestPeon(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = mock.Mock()

    def test_str_method(self):
        '''
        The function test_str_method verifies that the __str__ method of the Peon class returns 'P' for a white piece and 'p' for a black piece.
        '''
        peon_blanco = Peon('BLANCA', self.__tablero__)
        peon_negro = Peon('NEGRA', self.__tablero__)
        self.assertEqual(str(peon_blanco), 'P')
        self.assertEqual(str(peon_negro), 'p')

    def test_possible_moves_white(self):
        '''
        The function test_possible_moves_white verifies the possible moves of a white pawn from different positions.
        It calls the possible_moves method of the Peon class with a starting row and column and verifies that the returned moves are as expected.
        '''
        peon = Peon('BLANCA', self.__tablero__)
        
        # Mock the tablero methods
        self.__tablero__.is_empty.side_effect = lambda x, y: True
        self.__tablero__.get_piece.side_effect = lambda x, y: None
        
        # Moves from the initial position (6, 3)
        expected_moves_initial = [(5, 3), (4, 3)]
        self.assertEqual(peon.possible_moves(6, 3), expected_moves_initial)
        
        # Moves from an intermediate position (5, 3)
        expected_moves_intermediate = [(4, 3)]
        self.assertEqual(peon.possible_moves(5, 3), expected_moves_intermediate)
        
        # Diagonal moves for capturing
        self.__tablero__.is_empty.side_effect = lambda x, y: False
        self.__tablero__.get_piece.side_effect = lambda x, y: mock.Mock(color='NEGRA')
        possible_moves = peon.possible_moves(5, 3)
        self.assertIn((4, 2), possible_moves)
        self.assertIn((4, 4), possible_moves)

    def test_possible_moves_black(self):
        '''
        The function test_possible_moves_black verifies the possible moves of a black pawn from different positions.
        It calls the possible_moves method of the Peon class with a starting row and column and verifies that the returned moves are as expected.
        '''
        peon = Peon('NEGRA', self.__tablero__)
        
        # Mock the tablero methods
        self.__tablero__.is_empty.side_effect = lambda x, y: True
        self.__tablero__.get_piece.side_effect = lambda x, y: None
        
        # Moves from the initial position (1, 3)
        expected_moves_initial = [(2, 3), (3, 3)]
        self.assertEqual(peon.possible_moves(1, 3), expected_moves_initial)
        
        # Moves from an intermediate position (2, 3)
        expected_moves_intermediate = [(3, 3)]
        self.assertEqual(peon.possible_moves(2, 3), expected_moves_intermediate)
        
        # Diagonal moves for capturing
        self.__tablero__.is_empty.side_effect = lambda x, y: False
        self.__tablero__.get_piece.side_effect = lambda x, y: mock.Mock(color='BLANCA')
        possible_moves = peon.possible_moves(2, 3)
        self.assertIn((3, 2), possible_moves)
        self.assertIn((3, 4), possible_moves)

    def test_is_valid_move(self):
        '''
        The function test_is_valid_move verifies if the move is valid for the Peon class.
        '''
        peon_blanco = Peon('BLANCA', self.__tablero__)
        peon_negro = Peon('NEGRA', self.__tablero__)
        
        # Mock the tablero methods
        self.__tablero__.is_empty.side_effect = lambda x, y: True
        self.__tablero__.get_piece.side_effect = lambda x, y: None
        
        # Valid moves for white pawn
        self.assertTrue(peon_blanco.is_valid_move(6, 3, 5, 3, self.__tablero__))
        self.assertTrue(peon_blanco.is_valid_move(6, 3, 4, 3, self.__tablero__))
        
        # Invalid moves for white pawn
        self.assertFalse(peon_blanco.is_valid_move(6, 3, 5, 4, self.__tablero__))
        self.assertFalse(peon_blanco.is_valid_move(6, 3, 4, 4, self.__tablero__))
        
        # Valid moves for black pawn
        self.assertTrue(peon_negro.is_valid_move(1, 3, 2, 3, self.__tablero__))
        self.assertTrue(peon_negro.is_valid_move(1, 3, 3, 3, self.__tablero__))
        
        # Invalid moves for black pawn
        self.assertFalse(peon_negro.is_valid_move(1, 3, 2, 4, self.__tablero__))
        self.assertFalse(peon_negro.is_valid_move(1, 3, 3, 4, self.__tablero__))

    def test_mover(self):
        '''
        The function test_mover verifies the move functionality of the Peon class.
        '''
        peon_blanco = Peon('BLANCA', self.__tablero__)
        peon_negro = Peon('NEGRA', self.__tablero__)
        
        # Mock the tablero methods
        self.__tablero__.is_empty.side_effect = lambda x, y: True
        self.__tablero__.get_piece.side_effect = lambda x, y: None
        self.__tablero__.set_piece.side_effect = lambda x, y, piece: None
        
        # Valid moves for white pawn
        self.assertTrue(peon_blanco.mover(6, 3, 5, 3))
        self.assertTrue(peon_blanco.mover(6, 3, 4, 3))
        
        # Invalid moves for white pawn
        self.assertFalse(peon_blanco.mover(6, 3, 5, 4))
        self.assertFalse(peon_blanco.mover(6, 3, 4, 4))
        
        # Valid moves for black pawn
        self.assertTrue(peon_negro.mover(1, 3, 2, 3))
        self.assertTrue(peon_negro.mover(1, 3, 3, 3))
        
        # Invalid moves for black pawn
        self.assertFalse(peon_negro.mover(1, 3, 2, 4))
        self.assertFalse(peon_negro.mover(1, 3, 3, 4))

if __name__ == '__main__':
    unittest.main()