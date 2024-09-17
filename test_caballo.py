import unittest
from piezas import Pieza
from exceptions import InvalidMoveKnightMove
from caballo import Caballo

class TestCaballo(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = None  # Assuming tablero is not needed for these tests
        self.__caballo__ = Caballo("blanco", self.__tablero__)
        self.__caballo__.set_posicion((0, 0))

    def test_blanca_str(self):
        self.assertEqual(self.__caballo__.blanca_str, "♘")

    def test_negra_str(self):
        self.__caballo_negro__ = Caballo("negro", self.__tablero__)
        self.assertEqual(self.__caballo_negro__.negra_str, "♞")

    def test_set_get_posicion(self):
        self.__caballo__.set_posicion((1, 2))
        self.assertEqual(self.__caballo__.get_posicion(), (1, 2))

    def test_mover_valid(self):
        self.__caballo__.set_posicion((0, 0))
        self.__caballo__.mover((2, 1))
        self.assertEqual(self.__caballo__.get_posicion(), (2, 1))

    def test_mover_invalid(self):
        self.__caballo__.set_posicion((0, 0))
        with self.assertRaises(InvalidMoveKnightMove):
            self.__caballo__.mover((3, 3))

    def test_valid_positions(self):
        self.assertTrue(self.__caballo__.valid_positions(0, 0, 2, 1))
        self.assertTrue(self.__caballo__.valid_positions(0, 0, 1, 2))
        self.assertFalse(self.__caballo__.valid_positions(0, 0, 3, 3))

if __name__ == '__main__':
    unittest.main()