import unittest
from pieza import Pieza
from torre import Torre
from alfil import Alfil
from tablero import tablero

class TestPiezas(unittest.TestCase):
    def setUp(self):
        self.__alfil__ = Alfil()
        self.__torre__ = Torre()
        self.__tablero__ = tablero

    # Tests TORRE
    def test_torre(self):
        torre = Torre("BLANCA")
        self.assertTrue(torre.mover((0, 0), (0, 3)))
        self.assertTrue(torre.mover((0, 0), (5, 0)))
        self.assertFalse(torre.mover((0, 0), (3, 3)))
    def test_mover_torre(self):
        # Prueba un movimiento válido de la torre
        self.assertTrue(self.__torre__.mover(self.__tablero__, (0, 0), (0, 2)))

        # Prueba un movimiento inválido de la torre
        self.assertFalse(self.__torre__.mover(self.__tablero__, (0, 0), (2, 2)))

    # Tests ALFIL
    def test_alfil(self):
        alfil = Alfil("NEGRA")
        self.assertTrue(alfil.mover((0, 0), (3, 3)))
        self.assertTrue(alfil.mover((3, 3), (0, 0)))
        self.assertFalse(alfil.mover((0, 0), (0, 3)))

    def test_mover_alfil(self):
        # Prueba un movimiento válido del alfil
        self.assertTrue(self.__alfil__.mover(self.__tablero__, (0, 0), (2, 2)))
        # Prueba un movimiento inválido del alfil
        self.assertFalse(self.__alfil__.mover(self.__tablero__, (0, 0), (0, 2)))

    def test_pieza(self):
        with self.assertRaises(TypeError):
            p = Pieza("BLANCA")  # Should raise TypeError because Pieza is abstract

if __name__ == "__main__":
    unittest.main()