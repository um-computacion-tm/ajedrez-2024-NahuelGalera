import unittest
from rey import Rey

class TestRey(unittest.TestCase):
    def setUp(self):
        self.__rey__ = Rey('blanco')

    def test_movimiento_valido(self):
        self.assertTrue(self.__rey__.mover((1, 1), (1, 2)))
        self.assertTrue(self.__rey__.mover((1, 1), (2, 2)))
        self.assertTrue(self.__rey__.mover((1, 1), (2, 1)))

    def test_movimiento_invalido(self):
        self.assertFalse(self.__rey__.mover((1, 1), (3, 3)))
        self.assertFalse(self.__rey__.mover((1, 1), (1, 3)))
        self.assertFalse(self.__rey__.mover((1, 1), (3, 1)))

if __name__ == '__main__':
    unittest.main()