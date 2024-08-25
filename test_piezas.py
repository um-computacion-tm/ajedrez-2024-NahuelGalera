import unittest
from pieza import Pieza
from torre import Torre
from alfil import Alfil
from tablero import Tablero
from tablero import tablero
from peon import Peon

class TestPiezas(unittest.TestCase):
    def setUp(self):
        self.__alfil__ = Alfil("BLANCA")
        self.__torre__ = Torre("NEGRA")
        self.__tablero__ = tablero

    # PEON

    def test_peon(self):
        self.__tablero__ = Tablero()  # Asumiendo que tienes una clase Tablero
        self.__peon_blanco__ = Peon('BLANCA')
        self.__peon_negro__ = Peon('NEGRA')
    def test_mover_una_casilla_adelante(self):
        self.__tablero__.set_element(1, 1, self.__peon_blanco__)  # Coloca un peón blanco en (1, 1)
        self.assertTrue(self.__peon_blanco__.is_valid_move((1, 1), (2, 1), self.__tablero__))  # Mover una casilla adelante es válido

    def test_mover_dos_casillas_adelante(self):
        self.__tablero__.set_element(1, 1, self.__peon_blanco__)  # Coloca un peón blanco en (1, 1)
        self.assertTrue(self.__peon_blanco__.is_valid_move((1, 1), (3, 1), self.__tablero__))  # Mover dos casillas adelante es válido

    def test_captura(self):
        self.__tablero__.set_element(1, 1, self.__peon_blanco__)  # Coloca un peón blanco en (1, 1)
        self.__tablero__.set_element(2, 2, self.__peon_negro__)  # Coloca un peón negro en (2, 2)
        self.assertTrue(self.__peon_blanco__.is_valid_move((1, 1), (2, 2), self.__tablero__))  # Capturar es válido

    def test_movimiento_invalido(self):
        self.__tablero__.set_element(1, 1, self.__peon_blanco__)  # Coloca un peón blanco en (1, 1)
        self.assertFalse(self.__peon_blanco__.is_valid_move((1, 1), (3, 3), self.__tablero__))  # Mover en diagonal sin capturar no es válido


    # TORRE
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

    # ALFIL
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