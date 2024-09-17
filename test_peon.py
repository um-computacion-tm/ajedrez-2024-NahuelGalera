import unittest
from piezas import Pieza
from tablero import Tablero
from peon import Peon

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__peon_blanco__ = Peon("BLANCA", self.__tablero__)
        self.__peon_negro__ = Peon("NEGRA", self.__tablero__)

    def test_mover(self):
        # Test moving forward one square
        self.assertTrue(self.__peon_blanco__.mover(1, 0, 2, 0, self.__tablero__))
        self.assertTrue(self.__peon_negro__.mover(6, 0, 5, 0, self.__tablero__))

        # Test moving forward two squares from starting position
        self.assertTrue(self.__peon_blanco__.mover(1, 0, 3, 0, self.__tablero__))
        self.assertTrue(self.__peon_negro__.mover(6, 0, 4, 0, self.__tablero__))

        # Test moving forward two squares not from starting position
        self.assertFalse(self.__peon_blanco__.mover(2, 0, 4, 0, self.__tablero__))
        self.assertFalse(self.__peon_negro__.mover(5, 0, 3, 0, self.__tablero__))

        # Test capturing
        self.__tablero__.__posiciones__[2][1] = Pieza("NEGRA", self.__tablero__)
        self.__tablero__.__posiciones__[5][1] = Pieza("BLANCA", self.__tablero__)
        self.assertTrue(self.__peon_blanco__.mover(2, 0, 2, 1, self.__tablero__))
        self.assertTrue(self.__peon_negro__.mover(5, 0, 5, 1, self.__tablero__))
    
    def test_valid_positions(self):
        # Test moving forward one square
        self.assertTrue(self.__peon_blanco__.valid_positions(1, 0, 2, 0))
        self.assertTrue(self.__peon_negro__.valid_positions(6, 0, 5, 0))

        # Test moving forward two squares from starting position
        self.assertTrue(self.__peon_blanco__.valid_positions(1, 0, 3, 0))
        self.assertTrue(self.__peon_negro__.valid_positions(6, 0, 4, 0))

        # Test moving forward two squares not from starting position
        self.assertFalse(self.__peon_blanco__.valid_positions(2, 0, 4, 0))
        self.assertFalse(self.__peon_negro__.valid_positions(5, 0, 3, 0))

if __name__ == '__main__':
    unittest.main()