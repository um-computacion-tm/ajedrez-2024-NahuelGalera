import unittest
from caballo import Caballo
from exceptions import InvalidMoveKnightMove

class TestCaballo(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = [[None]*8 for _ in range(8)]  # Crear un tablero vacío
        self.__caballo__ = Caballo('blanca', self.__tablero__)  # Crear un caballo blanco

    def test_set_posicion(self):
        self.__caballo__.set_posicion((3, 3))
        self.assertEqual(self.__caballo__.get_posicion(), (3, 3))

    def test_mover_valido(self):
        self.__caballo__.set_posicion((3, 3))
        self.__caballo__.mover((5, 4))  # Mover el caballo a una posición válida
        self.assertEqual(self.__caballo__.get_posicion(), (5, 4))

    def test_mover_invalido(self):
        self.__caballo__.set_posicion((3, 3))
        with self.assertRaises(InvalidMoveKnightMove):
            self.__caballo__.mover((5, 5))  # Intentar mover el caballo a una posición inválida

if __name__ == '__main__':
    unittest.main()