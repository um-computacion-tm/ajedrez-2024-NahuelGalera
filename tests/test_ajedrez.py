import unittest
from codigo_ajedrez.tablero import Tablero
from codigo_ajedrez.ajedrez import Ajedrez

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        posiciones = [...]
        self.__tablero__ = Tablero(posiciones)
        self.__ajedrez__ = Ajedrez(self.__tablero__)

    def test_cambiar_turno(self):
        self.assertEqual(self.__ajedrez__.__turno__, "BLANCAS")
        self.__ajedrez__.cambiar_turno()
        self.assertEqual(self.__ajedrez__.__turno__, "NEGRAS")
        self.__ajedrez__.cambiar_turno()
        self.assertEqual(self.__ajedrez__.__turno__, "BLANCAS")

    def test_validar_coordenadas(self):
        # Test coordenadas validas
        self.assertTrue(self.__ajedrez__.validar_coordenadas(0, 0, 7, 7))

        # Test coordenadas invalidas
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(-1, 0, 7, 7)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, -1, 7, 7)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, 0, 8, 7)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, 0, 7, 8)

if __name__ == "__main__":
    unittest.main()