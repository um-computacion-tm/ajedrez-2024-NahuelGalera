import unittest
from unittest.mock import MagicMock
from rey import Rey

class TestRey(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = MagicMock()
        self.__rey__ = Rey('BLANCA', self.__tablero__)

    def test_str(self):
        self.assertEqual(str(self.__rey__), 'K')
        self.__rey___negro = Rey('NEGRA', self.__tablero__)
        self.assertEqual(str(self.__rey___negro), 'k')

    def test_possible_moves(self):
        expected_moves = [(3, 3), (3, 5), (5, 3), (5, 5), (3, 4), (5, 4), (4, 3), (4, 5)]
        moves = self.__rey__.possible_moves(4, 4)
        self.assertEqual(moves, expected_moves)

    def test_is_valid_move(self):
        self.__tablero__.get_piece.return_value = None
        self.assertTrue(self.__rey__.is_valid_move(4, 4, 5, 5, self.__tablero__))
        self.assertFalse(self.__rey__.is_valid_move(4, 4, 6, 6, self.__tablero__))

        pieza_opuesta = MagicMock()
        pieza_opuesta.color = 'NEGRA'
        self.__tablero__.get_piece.return_value = pieza_opuesta
        self.assertTrue(self.__rey__.is_valid_move(4, 4, 5, 5, self.__tablero__))

        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.__tablero__.get_piece.return_value = pieza_misma_color
        self.assertFalse(self.__rey__.is_valid_move(4, 4, 5, 5, self.__tablero__))

    def test_mover(self):
        self.__tablero__.get_piece.return_value = None
        self.assertTrue(self.__rey__.mover(4, 4, 5, 5))
        self.__tablero__.set_piece.assert_any_call(5, 5, self.__rey__)
        self.__tablero__.set_piece.assert_any_call(4, 4, None)

        self.assertFalse(self.__rey__.mover(4, 4, 6, 6))

if __name__ == '__main__':
    unittest.main()