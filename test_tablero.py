import unittest
from torre import Torre
from tablero import tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = tablero(for_test=True)

    def test_init(self):
        self.assertEqual(len(self.__tablero__.__posiciones__), 8)
        for col in self.__tablero__.__posiciones__:
            self.assertEqual(len(col), 8)

    def test_str(self):
        expected_str = "        \n" * 8
        self.assertEqual(str(self.__tablero__), expected_str)

    def test_get_piece(self):
        torre = Torre("NEGRA", self.__tablero__)
        self.__tablero__.set_piece(0, 0, torre)
        self.assertEqual(self.__tablero__.get_piece(0, 0), torre)

    def test_set_piece(self):
        torre = Torre("NEGRA", self.__tablero__)
        self.__tablero__.set_piece(0, 0, torre)
        self.assertEqual(self.__tablero__.__posiciones__[0][0], torre)

if __name__ == '__main__':
    unittest.main()