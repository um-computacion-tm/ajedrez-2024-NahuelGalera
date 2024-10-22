import unittest
from unittest.mock import MagicMock
from torre import Torre

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = MagicMock()
        self.__torre__ = Torre('BLANCA', self.__tablero__)

    def test_str(self):
        self.assertEqual(str(self.__torre__), 'R')
        self.__torre___negra = Torre('NEGRA', self.__tablero__)
        self.assertEqual(str(self.__torre___negra), 'r')

    def test_possible_moves(self):
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        moves = self.__torre__.possible_moves(4, 4)
        self.assertEqual(moves, expected_moves)

    def test_is_valid_move(self):
        self.__tablero__.get_piece.return_value = None
        self.assertTrue(self.__torre__.is_valid_move(4, 4, 4, 7, self.__tablero__))
        self.assertFalse(self.__torre__.is_valid_move(4, 4, 5, 5, self.__tablero__))

        pieza_opuesta = MagicMock()
        pieza_opuesta.color = 'NEGRA'
        self.__tablero__.get_piece.return_value = pieza_opuesta
        self.assertFalse(self.__torre__.is_valid_move(4, 4, 4, 7, self.__tablero__))

        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.__tablero__.get_piece.return_value = pieza_misma_color
        self.assertFalse(self.__torre__.is_valid_move(4, 4, 4, 7, self.__tablero__))

if __name__ == '__main__':
    unittest.main()