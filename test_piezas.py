import unittest
from unittest.mock import MagicMock
from piezas import Pieza

class PiezaConcreta(Pieza):
    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        return True  # Implementación ficticia para pruebas

    def is_valid_move(self, tablero, from_x, from_y, to_x, to_y):
        return True  # Implementación ficticia para pruebas

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = MagicMock()
        self.__pieza__ = PiezaConcreta('BLANCA', self.__tablero__)

    def test_color(self):
        self.assertEqual(self.__pieza__.color, 'BLANCA')

    def test_tablero(self):
        self.assertEqual(self.__pieza__.tablero, self.__tablero__)

    def test_possible_moves_general(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        moves = self.__pieza__.possible_moves_general(4, 4, directions)
        self.assertEqual(moves, expected_moves)

    def test_possible_moves_general_single_step(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        expected_moves = [(3, 4), (5, 4), (4, 3), (4, 5)]
        moves = self.__pieza__.possible_moves_general(4, 4, directions, single_step=True)
        self.assertEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()