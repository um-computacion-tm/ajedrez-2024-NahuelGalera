import unittest
from unittest.mock import MagicMock
from tablero import Tablero
from reina import Reina

class TestReina(unittest.TestCase):
    def setUp(self):
        self.tablero = MagicMock(spec=Tablero)
        self.reina_blanca = Reina('BLANCA', self.tablero)
        self.reina_negra = Reina('NEGRA', self.tablero)

    def test_inicializacion(self):
        self.assertEqual(self.reina_blanca.color, 'BLANCA')
        self.assertEqual(self.reina_negra.color, 'NEGRA')
        self.assertEqual(self.reina_blanca.tablero, self.tablero)
        self.assertEqual(self.reina_negra.tablero, self.tablero)

    def test_blanca_str(self):
        self.assertEqual(self.reina_blanca.blanca_str, "♛")

    def test_negra_str(self):
        self.assertEqual(self.reina_negra.negra_str, "♕")

    def test_is_valid_move_diagonal(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.reina_blanca.is_valid_move(0, 0, 7, 7, self.tablero))
        self.assertTrue(self.reina_blanca.is_valid_move(7, 7, 0, 0, self.tablero))

    def test_is_valid_move_vertical(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.reina_blanca.is_valid_move(0, 0, 7, 0, self.tablero))
        self.assertTrue(self.reina_blanca.is_valid_move(7, 0, 0, 0, self.tablero))

    def test_is_valid_move_horizontal(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.reina_blanca.is_valid_move(0, 0, 0, 7, self.tablero))
        self.assertTrue(self.reina_blanca.is_valid_move(0, 7, 0, 0, self.tablero))

    def test_is_valid_move_invalid(self):
        self.assertFalse(self.reina_blanca.is_valid_move(0, 0, 6, 7, self.tablero))

    def test_is_valid_move_blocked(self):
        self.tablero.get_piece.side_effect = lambda fila, col: None if fila != 3 else MagicMock()
        self.assertFalse(self.reina_blanca.is_valid_move(0, 0, 7, 0, self.tablero))

    def test_is_valid_move_same_color(self):
        self.tablero.get_piece.side_effect = lambda fila, col: MagicMock(color='BLANCA') if (fila, col) == (7, 0) else None
        self.assertFalse(self.reina_blanca.is_valid_move(0, 0, 7, 0, self.tablero))

    def test_mover(self):
        self.tablero.get_piece.return_value = None
        self.assertTrue(self.reina_blanca.mover(0, 0, 7, 0))
        self.tablero.set_piece.assert_any_call(7, 0, self.reina_blanca)
        self.tablero.set_piece.assert_any_call(0, 0, None)

    def test_mover_invalido(self):
        self.tablero.get_piece.return_value = None
        self.assertFalse(self.reina_blanca.mover(0, 0, 6, 7))
        self.tablero.set_piece.assert_not_called()

if __name__ == '__main__':
    unittest.main()