import unittest
from piezas.torre import Torre
from codigo_ajedrez.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero([])

    def test_get_pieza(self):
        # Testeo de la ficha en pos especifica
        self.assertIsInstance(self.__tablero__.get_pieza(0, 0), Torre)
        self.assertEqual(self.__tablero__.get_pieza(0, 0).__color__, "NEGRA")
        self.assertIsInstance(self.__tablero__.get_pieza(7, 7), Torre)
        self.assertEqual(self.__tablero__.get_pieza(7, 7).__color__, "BLANCA")

        # Testeo poner ficha en donde no hay otra ficha
        self.assertIsNone(self.__tablero__.get_pieza(1, 1))

if __name__ == '__main__':
    unittest.main()