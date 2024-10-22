import unittest
from unittest.mock import patch
from io import StringIO
from tablero import Tablero
from piezas import Pieza
from torre import Torre
from caballo import Caballo
from alfil import Alfil
from reina import Reina
from rey import Rey
from peon import Peon

class PiezaMock(Pieza):
    def is_valid_move(self, from_x, from_y, to_x, to_y, tablero):
        return False  # Simulamos que todos los movimientos son inválidos para esta prueba

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()

    def test_inicializacion(self):
        print("Probando inicialización del tablero...")
        self.assertEqual(len(self.__tablero__.__board__), 8)
        self.assertEqual(len(self.__tablero__.__board__[0]), 8)
        print("Prueba completada: inicialización del tablero.")

    def test_inicializar_piezas(self):
        print("Probando inicialización de piezas...")
        self.assertIsInstance(self.__tablero__.get_piece(0, 0), Torre)
        self.assertIsInstance(self.__tablero__.get_piece(0, 1), Caballo)
        self.assertIsInstance(self.__tablero__.get_piece(0, 2), Alfil)
        self.assertIsInstance(self.__tablero__.get_piece(0, 3), Reina)
        self.assertIsInstance(self.__tablero__.get_piece(0, 4), Rey)
        self.assertIsInstance(self.__tablero__.get_piece(1, 0), Peon)
        self.assertIsInstance(self.__tablero__.get_piece(7, 0), Torre)
        self.assertIsInstance(self.__tablero__.get_piece(7, 1), Caballo)
        self.assertIsInstance(self.__tablero__.get_piece(7, 2), Alfil)
        self.assertIsInstance(self.__tablero__.get_piece(7, 3), Reina)
        self.assertIsInstance(self.__tablero__.get_piece(7, 4), Rey)
        self.assertIsInstance(self.__tablero__.get_piece(6, 0), Peon)
        print("Prueba completada: inicialización de piezas.")

    def test_is_empty(self):
        print("Probando si una posición está vacía...")
        self.assertTrue(self.__tablero__.is_empty(4, 4))
        self.assertFalse(self.__tablero__.is_empty(0, 0))
        with self.assertRaises(IndexError):
            self.__tablero__.is_empty(8, 8)
        print("Prueba completada: si una posición está vacía.")

    def test_get_piece(self):
        print("Probando obtener pieza del tablero...")
        pieza = PiezaMock('BLANCA', self.__tablero__)
        self.__tablero__.__board__[0][0] = pieza
        self.assertEqual(self.__tablero__.get_piece(0, 0), pieza)
        self.assertIsNone(self.__tablero__.get_piece(4, 4))
        with self.assertRaises(IndexError):
            self.__tablero__.get_piece(8, 8)
        print("Prueba completada: obtener pieza del tablero.")

    def test_set_piece(self):
        print("Probando colocar pieza en el tablero...")
        pieza = PiezaMock('BLANCA', self.__tablero__)
        self.__tablero__.set_piece(4, 4, pieza)
        self.assertEqual(self.__tablero__.get_piece(4, 4), pieza)
        with self.assertRaises(IndexError):
            self.__tablero__.set_piece(8, 8, pieza)
        print("Prueba completada: colocar pieza en el tablero.")

    def test_is_enemy(self):
        print("Probando si una posición está ocupada por un enemigo...")
        pieza_blanca = PiezaMock('BLANCA', self.__tablero__)
        pieza_negra = PiezaMock('NEGRA', self.__tablero__)
        self.__tablero__.set_piece(4, 4, pieza_blanca)
        self.__tablero__.set_piece(5, 5, pieza_negra)
        self.assertTrue(self.__tablero__.is_enemy(5, 5, 'BLANCA'))
        self.assertFalse(self.__tablero__.is_enemy(4, 4, 'BLANCA'))
        self.assertTrue(self.__tablero__.is_enemy(4, 4, 'NEGRA'))
        self.assertFalse(self.__tablero__.is_enemy(5, 5, 'NEGRA'))
        print("Prueba completada: si una posición está ocupada por un enemigo.")

    def test_sin_fichas(self):
        print("Probando si no hay fichas de un color en el tablero...")
        self.assertFalse(self.__tablero__.sin_fichas('BLANCA'))
        self.assertFalse(self.__tablero__.sin_fichas('NEGRA'))
        self.__tablero__.__board__ = [[None for _ in range(8)] for _ in range(8)]
        self.assertTrue(self.__tablero__.sin_fichas('BLANCA'))
        self.assertTrue(self.__tablero__.sin_fichas('NEGRA'))
        print("Prueba completada: si no hay fichas de un color en el tablero.")

    def test_mover_pieza(self):
        print("Probando mover pieza en el tablero...")
        pieza = PiezaMock('BLANCA', self.__tablero__)
        self.__tablero__.set_piece(0, 0, pieza)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(ValueError):
                self.__tablero__.mover_pieza(0, 0, 1, 1)
            output = mock_stdout.getvalue()
            self.assertIn("Movimiento inválido para", output)
        print("Prueba completada: mover pieza en el tablero.")

    def test_mover_pieza_desde_posicion_vacia(self):
        print("Probando mover pieza desde una posición vacía...")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(ValueError):
                self.__tablero__.mover_pieza(4, 4, 5, 5)
            output = mock_stdout.getvalue()
            self.assertIn("No hay pieza en la posición inicial (4, 4)", output)
        print("Prueba completada: mover pieza desde una posición vacía.")

if __name__ == '__main__':
    unittest.main()