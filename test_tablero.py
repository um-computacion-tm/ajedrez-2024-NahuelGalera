import unittest
from tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()

    def test_crear_tablero(self):
        self.assertEqual(len(self.__tablero__.__tablero__), 8)  # Check if the board has 8 rows
        self.assertEqual(len(self.__tablero__.__tablero__[0]), 8)  # Check if each row has 8 columns

    def test_get_pieza(self):
        self.assertEqual(self.__tablero__.get_pieza(0, 0), 'T')  # Check if the top left piece is a 'T'
        self.assertEqual(self.__tablero__.get_pieza(7, 7), 't')  # Check if the bottom right piece is a 't'

    def test_get_element(self):
        self.assertEqual(self.__tablero__.get_element(0, 0), 'T')  # Check if the top left element is a 'T'
        self.assertEqual(self.__tablero__.get_element(7, 7), 't')  # Check if the bottom right element is a 't'

if __name__ == '__main__':
    unittest.main()