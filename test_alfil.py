import unittest
from unittest.mock import MagicMock
from alfil import Alfil
from tablero import Tablero
from exceptions import InvalidMoveSpecific as InvalidMoveBishopMove

class TestAlfil(unittest.TestCase):
    def setUp(self):
        self.tablero = MagicMock(spec=Tablero)
        self.alfil_blanco = Alfil('BLANCA', self.tablero)
        self.alfil_negro = Alfil('NEGRA', self.tablero)

    def test_mover_valido(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.alfil_blanco.mover(self.tablero, (0, 0), (3, 3)))
        self.assertTrue(self.alfil_negro.mover(self.tablero, (7, 7), (4, 4)))

    def test_mover_invalido(self):
        self.tablero.get_piece.return_value = None
        with self.assertRaises(InvalidMoveBishopMove):
            self.alfil_blanco.mover(self.tablero, (0, 0), (3, 4))
        with self.assertRaises(InvalidMoveBishopMove):
            self.alfil_negro.mover(self.tablero, (7, 7), (4, 5))

    def test_is_valid_move_valido(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.alfil_blanco.is_valid_move(0, 0, 3, 3, self.tablero))
        self.assertTrue(self.alfil_negro.is_valid_move(7, 7, 4, 4, self.tablero))

    def test_is_valid_move_invalido(self):
        self.tablero.get_piece.return_value = None
        self.assertFalse(self.alfil_blanco.is_valid_move(0, 0, 3, 4, self.tablero))
        self.assertFalse(self.alfil_negro.is_valid_move(7, 7, 4, 5, self.tablero))

    def test_is_valid_move_ocupado(self):
        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.tablero.get_piece.return_value = pieza_misma_color
        self.assertFalse(self.alfil_blanco.is_valid_move(0, 0, 3, 3, self.tablero))

if __name__ == '__main__':
    unittest.main()