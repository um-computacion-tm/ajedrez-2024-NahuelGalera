import unittest
from rey import Rey

class TestRey(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = None  # Assuming tablero is not used in the methods we are testing
        self.__rey_blanco__ = Rey("blanco", self.__tablero__)
        self.__rey_negro__ = Rey("negro", self.__tablero__)

    def test_mover_valid(self):
        self.assertTrue(self.__rey_blanco__.mover((4, 4), (5, 5)))
        self.assertTrue(self.__rey_blanco__.mover((4, 4), (4, 5)))
        self.assertTrue(self.__rey_blanco__.mover((4, 4), (3, 3)))

    def test_mover_invalid(self):
        self.assertFalse(self.__rey_blanco__.mover((4, 4), (6, 6)))
        self.assertFalse(self.__rey_blanco__.mover((4, 4), (4, 6)))
        self.assertFalse(self.__rey_blanco__.mover((4, 4), (2, 2)))

    def test_valid_positions_valid(self):
        self.assertTrue(self.__rey_blanco__.valid_positions(4, 4, 5, 5))
        self.assertTrue(self.__rey_blanco__.valid_positions(4, 4, 4, 5))
        self.assertTrue(self.__rey_blanco__.valid_positions(4, 4, 3, 3))

    def test_valid_positions_invalid(self):
        self.assertFalse(self.__rey_blanco__.valid_positions(4, 4, 6, 6))
        self.assertFalse(self.__rey_blanco__.valid_positions(4, 4, 4, 6))
        self.assertFalse(self.__rey_blanco__.valid_positions(4, 4, 2, 2))

if __name__ == '__main__':
    unittest.main()