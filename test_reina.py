import unittest
from reina import Reina
from piezas import Pieza
from exceptions import InvalidMoveQueenMove

class TestReina(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = [[None]*8 for _ in range(8)]  # Crear un tablero vacío
        self.__reina__ = Reina('blanca', self.__tablero__)  # Crear una reina blanca

    def test_movimientos_validos(self):
        self.__reina__.__fila__ = 3
        self.__reina__.__columna__ = 3
        movimientos = self.__reina__.movimientos_validos(3, 3)
        self.assertEqual(len(movimientos), 27)  # La reina debería tener 27 movimientos válidos desde el centro del tablero

    def test_mover_valido(self):
        self.__reina__.__fila__ = 3
        self.__reina__.__columna__ = 3
        self.__reina__.mover(5, 5)  # Mover la reina a una posición válida
        self.assertEqual(self.__reina__.__fila__, 5)
        self.assertEqual(self.__reina__.__columna__, 5)

    def test_mover_invalido(self):
        self.__reina__.__fila__ = 3
        self.__reina__.__columna__ = 3
        with self.assertRaises(InvalidMoveQueenMove):
            self.__reina__.mover(5, 4)  # Intentar mover la reina a una posición inválida

if __name__ == '__main__':
    unittest.main()