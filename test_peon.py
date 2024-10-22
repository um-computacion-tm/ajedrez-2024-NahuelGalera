import unittest
from piezas import Pieza
from peon import Peon

class MockTablero:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def set_piece(self, x, y, piece):
        self.board[x][y] = piece

    def get_piece(self, x, y):
        return self.board[x][y]

    def is_empty(self, x, y):
        return self.board[x][y] is None

    def is_enemy(self, x, y, color):
        piece = self.board[x][y]
        return piece is not None and piece.color != color

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.tablero = MockTablero()
        self.peon_blanco = Peon('BLANCA', self.tablero)
        self.peon_negro = Peon('NEGRA', self.tablero)
        self.tablero.set_piece(6, 0, self.peon_blanco)
        self.tablero.set_piece(1, 0, self.peon_negro)

    def test_mover_un_cuadro_adelante(self):
        self.assertTrue(self.peon_blanco.mover(6, 0, 5, 0))
        self.assertTrue(self.peon_negro.mover(1, 0, 2, 0))

    def test_mover_dos_cuadros_adelante_inicial(self):
        self.assertTrue(self.peon_blanco.mover(6, 0, 4, 0))
        self.assertTrue(self.peon_negro.mover(1, 0, 3, 0))

    def test_mover_dos_cuadros_adelante_no_inicial(self):
        self.peon_blanco.mover(6, 0, 5, 0)
        self.assertFalse(self.peon_blanco.mover(5, 0, 3, 0))

    def test_mover_diagonal_captura(self):
        self.tablero.set_piece(5, 1, Peon('NEGRA', self.tablero))
        self.assertTrue(self.peon_blanco.mover(6, 0, 5, 1))

    def test_mover_diagonal_no_captura(self):
        self.assertFalse(self.peon_blanco.mover(6, 0, 5, 1))

    def test_mover_invalido(self):
        self.assertFalse(self.peon_blanco.mover(6, 0, 4, 1))

if __name__ == '__main__':
    unittest.main()