import unittest
from pieza import Pieza
from torre import Torre
from alfil import Alfil
from tablero import Tablero
from peon import Peon

class TestPiezas(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__peon_blanco__ = Peon('blanco')
        self.__alfil__ = Alfil('blanco')
        self.__torre__ = Torre('blanco')
        self.__peon_negro__ = Peon('negro')

    # PEON
    def test_peon_moves_one_square_forward(self):
        self.__tablero__.set_element(1, 1, self.__peon_blanco__)
        self.assertTrue(self.__peon_blanco__.is_valid_move((1, 1), (2, 1), self.__tablero__))

    # ... other tests ...

    # TORRE
    def test_torre_moves_vertically(self):
        self.assertTrue(self.__torre__.mover((0, 0), (0, 3), self.__tablero__))

    # ... other tests ...

    # ALFIL
    def test_alfil_moves_diagonally(self):
        self.assertTrue(self.__alfil__.mover((0, 0), (3, 3), self.__tablero__))

    # ... other tests ...

    def test_pieza_raises_type_error(self):
        with self.assertRaises(TypeError):
            Pieza("blanca")  # Should raise TypeError because Pieza is abstract

if __name__ == "__main__":
    unittest.main()