import unittest
from piezas import Pieza
from torre import Torre

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.__torre__ = Torre()

    def test_valid_posiciones(self):
        self.assertTrue(self.__torre__.valid_posiciones(0, 0, 0, 1))
        self.assertFalse(self.__torre__.valid_posiciones(0, 0, 1, 1))

    def test_posibles_posiciones_vd(self):
        self.assertEqual(self.__torre__.posibles_posiciones_vd(0, 0), [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])

    def test_posibles_posiciones_va(self):
        self.assertEqual(self.__torre__.posibles_posiciones_va(7, 0), [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])

if __name__ == '__main__':
    unittest.main()