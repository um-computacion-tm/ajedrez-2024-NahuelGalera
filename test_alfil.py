# test_alfil.py
import unittest
from tablero import Tablero
from alfil import Alfil
from exceptions import InvalidMoveBishopMove

class TestAlfil(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__alfil_blanco__ = Alfil("BLANCA", self.__tablero__)
        self.__tablero__.set_piece(2, 0, self.__alfil_blanco__)  # Colocar el alfil en la posición inicial (2, 0)

    def test_valid_move(self):
        # Mover el alfil de (2, 0) a (5, 3)
        self.assertTrue(self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (5, 3)))

    def test_valid_move_other_diagonal(self):
        # Mover el alfil de (2, 0) a (0, 2)
        self.assertTrue(self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (0, 2)))

    def test_invalid_move_blocked(self):
        # Colocar una pieza en el camino del alfil
        self.__tablero__.set_piece(3, 1, Alfil("NEGRA", self.__tablero__))
        with self.assertRaises(InvalidMoveBishopMove):
            self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (5, 3))

    def test_invalid_move_not_diagonal(self):
        # Intentar mover el alfil a una posición no diagonal
        with self.assertRaises(InvalidMoveBishopMove):
            self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (2, 3))

    def test_invalid_move_out_of_bounds(self):
        # Intentar mover el alfil fuera del tablero
        with self.assertRaises(InvalidMoveBishopMove):
            self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (8, 6))

    def test_valid_move_capture_enemy(self):
        # Colocar una pieza enemiga en la posición final
        self.__tablero__.set_piece(5, 3, Alfil("NEGRA", self.__tablero__))
        self.assertTrue(self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (5, 3)))

    def test_invalid_move_capture_friend(self):
        # Colocar una pieza amiga en la posición final
        self.__tablero__.set_piece(5, 3, Alfil("BLANCA", self.__tablero__))
        with self.assertRaises(InvalidMoveBishopMove):
            self.__alfil_blanco__.mover(self.__tablero__, (2, 0), (5, 3))

if __name__ == '__main__':
    unittest.main()