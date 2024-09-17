# test_torre.py
import unittest
from tablero import Tablero
from torre import Torre

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__torre_blanca__ = Torre("BLANCA", self.__tablero__)
        self.__tablero__.set_piece(0, 0, self.__torre_blanca__)  # Colocar la torre en la posición inicial (0, 0)

    def test_valid_move_vertical(self):
        # Mover la torre de (0, 0) a (3, 0)
        self.assertTrue(self.__torre_blanca__.mover(0, 0, 3, 0, self.__tablero__))
        self.assertIsNone(self.__tablero__.get_piece(0, 0))
        self.assertEqual(self.__tablero__.get_piece(3, 0), self.__torre_blanca__)

    def test_valid_move_horizontal(self):
        # Mover la torre de (0, 0) a (0, 3)
        self.assertTrue(self.__torre_blanca__.mover(0, 0, 0, 3, self.__tablero__))
        self.assertIsNone(self.__tablero__.get_piece(0, 0))
        self.assertEqual(self.__tablero__.get_piece(0, 3), self.__torre_blanca__)

    def test_invalid_move_diagonal(self):
        # Intentar mover la torre a una posición diagonal
        self.assertFalse(self.__torre_blanca__.mover(0, 0, 3, 3, self.__tablero__))
        self.assertEqual(self.__tablero__.get_piece(0, 0), self.__torre_blanca__)
        self.assertIsNone(self.__tablero__.get_piece(3, 3))

    def test_invalid_move_blocked(self):
        # Colocar una pieza en el camino de la torre
        self.__tablero__.set_piece(1, 0, Torre("NEGRA", self.__tablero__))
        self.assertFalse(self.__torre_blanca__.mover(0, 0, 3, 0, self.__tablero__))
        self.assertEqual(self.__tablero__.get_piece(0, 0), self.__torre_blanca__)
        self.assertEqual(self.__tablero__.get_piece(1, 0).color, "NEGRA")
        self.assertIsNone(self.__tablero__.get_piece(3, 0))

if __name__ == '__main__':
    unittest.main()