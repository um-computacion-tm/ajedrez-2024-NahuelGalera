import unittest
from tablero import Tablero
from peon import Peon

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__peon_blanco__ = Peon("BLANCA", self.__tablero__)
        self.__peon_negro__ = Peon("NEGRA", self.__tablero__)
        self.__tablero__.set_piece(6, 0, self.__peon_blanco__)
        self.__tablero__.set_piece(1, 1, self.__peon_negro__)

    def test_mover_blanco_un_cuadro(self):
        print("Before move:", self.__tablero__)
        self.assertTrue(self.__peon_blanco__.mover(6, 0, 5, 0, self.__tablero__))
        print("After move:", self.__tablero__)

    def test_captura_blanco(self):
        self.__tablero__.set_piece(5, 1, self.__peon_negro__)
        print("Before move:", self.__tablero__)
        result = self.__peon_blanco__.mover(6, 0, 5, 1, self.__tablero__)
        print("Move result:", result)
        print("After move:", self.__tablero__)
        self.assertTrue(result)  # Captura válida

    def test_mover_negro_un_cuadro(self):
        print("Before move:", self.__tablero__)
        self.assertTrue(self.__peon_negro__.mover(1, 1, 2, 1, self.__tablero__))
        print("After move:", self.__tablero__)

    def test_captura_negro(self):
        self.__tablero__.set_piece(2, 0, self.__peon_blanco__)
        print("Before move:", self.__tablero__)
        self.assertTrue(self.__peon_negro__.mover(1, 1, 2, 0, self.__tablero__))
        print("After move:", self.__tablero__)

if __name__ == '__main__':
    unittest.main()