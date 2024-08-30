import unittest
from peon import Peon
from tablero import Tablero

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
        self.peon_blanco = Peon('BLANCA')
        self.peon_negro = Peon('NEGRA')

    def test_mover_una_casilla(self):
        self.tablero.set_element(6, 0, self.peon_blanco)
        self.assertTrue(self.peon_blanco.mover(6, 0, 5, 0, self.tablero))

    def test_mover_dos_casillas(self):
        self.tablero.set_element(6, 0, self.peon_blanco)
        self.assertTrue(self.peon_blanco.mover(6, 0, 4, 0, self.tablero))

    def test_capturar(self):
        self.tablero.set_element(6, 0, self.peon_blanco)
        self.tablero.set_element(5, 1, self.peon_negro)
        self.assertTrue(self.peon_blanco.mover(6, 0, 5, 1, self.tablero))

    def test_mover_invalido(self):
        self.tablero.set_element(6, 0, self.peon_blanco)
        self.assertFalse(self.peon_blanco.mover(6, 0, 4, 1, self.tablero))

if __name__ == '__main__':
    unittest.main()