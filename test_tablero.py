import unittest
from tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero(for_test=True)

    def test_get_pieza(self):
        with self.assertRaises(ValueError):
            self.__tablero__.get_pieza(8, 8)  # Posición fuera de rango

    def test_set_pieza(self):
        with self.assertRaises(ValueError):
            self.__tablero__.set_pieza(8, 8, None)  # Posición fuera de rango

    def test_mover_pieza(self):
        with self.assertRaises(ValueError):
            self.__tablero__.mover_pieza(0, 0, 8, 8)  # Movimiento no válido

    def test_str(self):
        self.assertEqual(str(self.__tablero__), "  a b c d e f g h\n1 . . . . . . . . \n2 . . . . . . . . \n3 . . . . . . . . \n4 . . . . . . . . \n5 . . . . . . . . \n6 . . . . . . . . \n7 . . . . . . . . \n8 . . . . . . . . \n")

if __name__ == '__main__':
    unittest.main()