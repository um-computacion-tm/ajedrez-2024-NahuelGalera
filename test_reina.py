import unittest
from unittest.mock import MagicMock
from reina import Reina

class TestReina(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = MagicMock()
        self.__reina__ = Reina('BLANCA', self.__tablero__)

    def test_str(self):
        self.assertEqual(str(self.__reina__), 'Q')
        self.__reina_negra__ = Reina('NEGRA', self.__tablero__)
        self.assertEqual(str(self.__reina_negra__), 'q')

    def test_possible_moves(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal hacia arriba a la izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal hacia arriba a la derecha
            (5, 3), (6, 2), (7, 1),          # Diagonal hacia abajo a la izquierda
            (5, 5), (6, 6), (7, 7),          # Diagonal hacia abajo a la derecha
            (4, 3), (4, 2), (4, 1), (4, 0),  # Horizontal hacia la izquierda
            (4, 5), (4, 6), (4, 7),          # Horizontal hacia la derecha
            (3, 4), (2, 4), (1, 4), (0, 4),  # Vertical hacia arriba
            (5, 4), (6, 4), (7, 4)           # Vertical hacia abajo
        ]
        moves = self.__reina__.possible_moves(4, 4)
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_is_valid_move(self):
        self.__tablero__.get_piece.return_value = None
        self.assertTrue(self.__reina__.is_valid_move(4, 4, 5, 5, self.__tablero__))
        self.assertTrue(self.__reina__.is_valid_move(4, 4, 6, 6, self.__tablero__))

        pieza_opuesta = MagicMock()
        pieza_opuesta.color = 'NEGRA'
        self.__tablero__.get_piece.return_value = pieza_opuesta
        self.assertTrue(self.__reina__.is_valid_move(4, 4, 5, 5, self.__tablero__))

        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.__tablero__.get_piece.return_value = pieza_misma_color
        self.assertFalse(self.__reina__.is_valid_move(4, 4, 5, 5, self.__tablero__))

    def test_mover(self):
        self.__tablero__.get_piece.return_value = None
        self.assertTrue(self.__reina__.mover(4, 4, 5, 5))
        self.__tablero__.set_piece.assert_any_call(5, 5, self.__reina__)
        self.__tablero__.set_piece.assert_any_call(4, 4, None)

        self.__tablero__.get_piece.return_value = MagicMock()
        self.assertFalse(self.__reina__.mover(4, 4, 6, 6))

if __name__ == '__main__':
    unittest.main()