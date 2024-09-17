import unittest
from peon import Peon
from piezas import Pieza
from tablero import Tablero  # Asumiendo que tienes una clase Tablero

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()
        self.__peon_blanco__ = Peon('BLANCA', self.__tablero__)
        self.__peon_negro__ = Peon('NEGRA', self.__tablero__)

    def test_blanca_str(self):
        self.assertEqual(self.__peon_blanco__.blanca_str, "♙")

    def test_negra_str(self):
        self.assertEqual(self.__peon_negro__.negra_str, "♟")

    def test_mover_valido(self):
        self.__tablero__.set_piece(1, 0, self.__peon_blanco__)
        self.assertTrue(self.__peon_blanco__.mover(1, 0, 3, 0))  # Movimiento inicial de dos casillas
        self.assertTrue(self.__peon_blanco__.mover(3, 0, 4, 0))  # Movimiento de una casilla

    def test_mover_invalido(self):
        self.__tablero__.set_piece(1, 0, self.__peon_blanco__)
        self.assertFalse(self.__peon_blanco__.mover(1, 0, 4, 0))  # Movimiento inválido de tres casillas
        self.assertFalse(self.__peon_blanco__.mover(1, 0, 1, 1))  # Movimiento lateral inválido

    def test_captura_valida(self):
        peon_negro = Peon('NEGRA', self.__tablero__)
        self.__tablero__.set_piece(1, 0, self.__peon_blanco__)
        self.__tablero__.set_piece(2, 1, peon_negro)
        self.assertTrue(self.__peon_blanco__.mover(1, 0, 2, 1))  # Captura válida

    def test_captura_invalida(self):
        self.__tablero__.set_piece(1, 0, self.__peon_blanco__)
        self.assertFalse(self.__peon_blanco__.mover(1, 0, 2, 1))  # Captura inválida sin pieza enemiga

if __name__ == '__main__':
    unittest.main()