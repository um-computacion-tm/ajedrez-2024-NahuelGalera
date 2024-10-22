import unittest
from unittest.mock import MagicMock
from alfil import Alfil
from exceptions import InvalidMoveSpecific as InvalidMoveBishopMove

class TestAlfil(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = MagicMock()
        self.__alfil_blanco__ = Alfil('BLANCA', self.__tablero__)
        self.__alfil_negro__ = Alfil('NEGRA', self.__tablero__)

    def test_str(self):
        self.assertEqual(str(self.__alfil_blanco__), 'B')
        self.assertEqual(str(self.__alfil_negro__), 'b')

    def test_possible_moves(self):
        self.__tablero__.is_empty.side_effect = lambda row, col: True
        moves = self.__alfil_blanco__.possible_moves(4, 4)
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal hacia arriba a la izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal hacia arriba a la derecha
            (5, 3), (6, 2), (7, 1),          # Diagonal hacia abajo a la izquierda
            (5, 5), (6, 6), (7, 7)           # Diagonal hacia abajo a la derecha
        ]
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_is_valid_move(self):
        self.__tablero__.get_piece.side_effect = lambda row, col: None
        self.assertTrue(self.__alfil_blanco__.is_valid_move(4, 4, 6, 6, self.__tablero__))
        self.assertFalse(self.__alfil_blanco__.is_valid_move(4, 4, 6, 5, self.__tablero__))

        pieza_opuesta = MagicMock()
        pieza_opuesta.color = 'NEGRA'
        self.__tablero__.get_piece.side_effect = lambda row, col: pieza_opuesta if (row, col) == (6, 6) else None
        self.assertTrue(self.__alfil_blanco__.is_valid_move(4, 4, 6, 6, self.__tablero__))

        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.__tablero__.get_piece.side_effect = lambda row, col: pieza_misma_color if (row, col) == (6, 6) else None
        self.assertFalse(self.__alfil_blanco__.is_valid_move(4, 4, 6, 6, self.__tablero__))

    def test_mover(self):
        self.__tablero__.get_piece.side_effect = lambda row, col: None
        self.__alfil_blanco__.mover(self.__tablero__, (4, 4), (6, 6))
        self.__tablero__.set_piece.assert_any_call(6, 6, self.__alfil_blanco__)
        self.__tablero__.set_piece.assert_any_call(4, 4, None)

        self.__tablero__.get_piece.side_effect = lambda row, col: MagicMock()
        with self.assertRaises(InvalidMoveBishopMove):
            self.__alfil_blanco__.mover(self.__tablero__, (4, 4), (6, 5))

if __name__ == '__main__':
    unittest.main()