# test_tablero.py
import unittest
from tablero import Tablero
from torre import Torre
from caballo import Caballo
from alfil import Alfil
from reina import Reina
from rey import Rey
from peon import Peon
from exceptions import InvalidMoveBishopMove

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()

    def test_initial_setup(self):
        # Verificar que las piezas estén en las posiciones iniciales correctas
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

    def test_get_piece(self):
        # Verificar que get_piece devuelva la pieza correcta
        self.assertIsInstance(self.__tablero__.get_piece(0, 0), Torre)
        self.assertIsNone(self.__tablero__.get_piece(4, 4))

    def test_set_piece(self):
        # Verificar que set_piece coloque la pieza en la posición correcta
        alfil = Alfil("BLANCA", self.__tablero__)
        self.__tablero__.set_piece(4, 4, alfil)
        self.assertEqual(self.__tablero__.get_piece(4, 4), alfil)

    def test_mover_pieza(self):
        # Verificar que mover_pieza mueva la pieza correctamente
        self.__tablero__.mover_pieza(1, 0, 3, 0)  # Mover peón negro de (1, 0) a (3, 0)
        self.assertIsInstance(self.__tablero__.get_piece(3, 0), Peon)
        self.assertIsNone(self.__tablero__.get_piece(1, 0))

    def test_mover_pieza_invalid(self):
        # Verificar que mover_pieza lance una excepción para un movimiento inválido
        with self.assertRaises(ValueError):
            self.__tablero__.mover_pieza(0, 0, 4, 4)  # Intentar mover torre negra de (0, 0) a (4, 4)

    def test_no_pieces_left(self):
        # Verificar que no_pieces_left devuelva True cuando no hay piezas del color dado
        self.assertFalse(self.__tablero__.no_pieces_left("BLANCA"))
        self.assertFalse(self.__tablero__.no_pieces_left("NEGRA"))

if __name__ == '__main__':
    unittest.main()