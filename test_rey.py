import unittest
from unittest.mock import MagicMock
from rey import Rey
from tablero import Tablero

class TestRey(unittest.TestCase):
    def setUp(self):
        self.tablero = MagicMock(spec=Tablero)
        self.rey_blanco = Rey('BLANCA', self.tablero)
        self.rey_negro = Rey('NEGRA', self.tablero)

    def test_mover_valido(self):
        self.assertTrue(self.rey_blanco.mover((4, 4), (5, 5)))
        self.assertTrue(self.rey_blanco.mover((4, 4), (3, 3)))
        self.assertTrue(self.rey_blanco.mover((4, 4), (4, 5)))
        self.assertTrue(self.rey_blanco.mover((4, 4), (4, 3)))

    def test_mover_invalido(self):
        self.assertFalse(self.rey_blanco.mover((4, 4), (6, 6)))
        self.assertFalse(self.rey_blanco.mover((4, 4), (2, 2)))
        self.assertFalse(self.rey_blanco.mover((4, 4), (4, 6)))
        self.assertFalse(self.rey_blanco.mover((4, 4), (4, 2)))

    def test_is_valid_move_valido(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.rey_blanco.is_valid_move(4, 4, 5, 5, self.tablero))
        self.assertTrue(self.rey_blanco.is_valid_move(4, 4, 3, 3, self.tablero))
        self.assertTrue(self.rey_blanco.is_valid_move(4, 4, 4, 5, self.tablero))
        self.assertTrue(self.rey_blanco.is_valid_move(4, 4, 4, 3, self.tablero))

    def test_is_valid_move_invalido(self):
        self.tablero.get_piece.return_value = None
        self.assertFalse(self.rey_blanco.is_valid_move(4, 4, 6, 6, self.tablero))
        self.assertFalse(self.rey_blanco.is_valid_move(4, 4, 2, 2, self.tablero))
        self.assertFalse(self.rey_blanco.is_valid_move(4, 4, 4, 6, self.tablero))
        self.assertFalse(self.rey_blanco.is_valid_move(4, 4, 4, 2, self.tablero))

    def test_is_valid_move_ocupado(self):
        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.tablero.get_piece.return_value = pieza_misma_color
        self.assertFalse(self.rey_blanco.is_valid_move(4, 4, 5, 5, self.tablero))

if __name__ == '__main__':
    unittest.main()