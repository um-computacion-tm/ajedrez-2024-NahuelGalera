import unittest
from unittest.mock import MagicMock
from caballo import Caballo
from tablero import Tablero

class TestCaballo(unittest.TestCase):
    def setUp(self):
        self.tablero = MagicMock(spec=Tablero)
        self.caballo_blanco = Caballo('BLANCA', self.tablero)
        self.caballo_negro = Caballo('NEGRA', self.tablero)
        self.caballo_blanco.set_posicion((1, 1))
        self.caballo_negro.set_posicion((6, 6))

    def test_mover_valido(self):
        self.tablero.get_piece.side_effect = lambda x, y: None
        print("Intentando mover caballo blanco de (1, 1) a (3, 2)")
        self.assertTrue(self.caballo_blanco.mover((3, 2)))
        print("Intentando mover caballo blanco de (3, 2) a (5, 3)")
        self.assertTrue(self.caballo_blanco.mover((5, 3)))
        print("Intentando mover caballo negro de (6, 6) a (8, 7)")
        self.assertTrue(self.caballo_negro.mover((8, 7)))
        print("Intentando mover caballo negro de (8, 7) a (6, 8)")
        self.assertTrue(self.caballo_negro.mover((6, 8)))

    def test_mover_invalido(self):
        self.tablero.get_piece.side_effect = lambda x, y: None
        print("Intentando mover caballo blanco de (1, 1) a (2, 2)")
        self.assertFalse(self.caballo_blanco.mover((2, 2)))
        print("Intentando mover caballo negro de (6, 6) a (5, 5)")
        self.assertFalse(self.caballo_negro.mover((5, 5)))

    def test_is_valid_move_valido(self):
        self.tablero.get_piece.side_effect = lambda x, y: None
        print("Verificando movimiento válido de caballo blanco de (1, 1) a (3, 2)")
        self.assertTrue(self.caballo_blanco.is_valid_move(1, 1, 3, 2, self.tablero))
        print("Verificando movimiento válido de caballo blanco de (1, 1) a (2, 3)")
        self.assertTrue(self.caballo_blanco.is_valid_move(1, 1, 2, 3, self.tablero))
        print("Verificando movimiento válido de caballo negro de (6, 6) a (8, 7)")
        self.assertTrue(self.caballo_negro.is_valid_move(6, 6, 8, 7, self.tablero))
        print("Verificando movimiento válido de caballo negro de (6, 6) a (7, 8)")
        self.assertTrue(self.caballo_negro.is_valid_move(6, 6, 7, 8, self.tablero))

    def test_is_valid_move_invalido(self):
        self.tablero.get_piece.side_effect = lambda x, y: None
        print("Verificando movimiento inválido de caballo blanco de (1, 1) a (2, 2)")
        self.assertFalse(self.caballo_blanco.is_valid_move(1, 1, 2, 2, self.tablero))
        print("Verificando movimiento inválido de caballo negro de (6, 6) a (5, 5)")
        self.assertFalse(self.caballo_negro.is_valid_move(6, 6, 5, 5, self.tablero))

    def test_is_valid_move_ocupado(self):
        pieza_misma_color = MagicMock()
        pieza_misma_color.color = 'BLANCA'
        self.tablero.get_piece.side_effect = lambda x, y: pieza_misma_color if (x, y) == (3, 2) else None
        print("Verificando movimiento inválido de caballo blanco de (1, 1) a (3, 2) con pieza del mismo color en destino")
        self.assertFalse(self.caballo_blanco.is_valid_move(1, 1, 3, 2, self.tablero))

if __name__ == '__main__':
    unittest.main()