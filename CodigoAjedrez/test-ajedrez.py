import unittest
from ajedrez import Ajedrez
from tablero import Tablero

class Ajedrez:
    def __init__(self, tablero):
        self.__tablero__ = tablero
        self.__turno__ = "BLANCAS"

    def move (
            self,
            from_row,
            from_col,
            to_row,
            to_col):
        # Validar coordenadas
        self.validar_coordenadas(from_row, from_col, to_row, to_col)
        pieza = self.__tablero__.get_pieza(from_row, from_col)
        self.cambiar_turno()

    def cambiar_turno(self):
        if self.__turno__ == "BLANCAS":
            self.__turno__ = "NEGRAS"
        else:
            self.__turno__ = "BLANCAS"

    def validar_coordenadas(self, from_row, from_col, to_row, to_col):
        if from_row < 0 or from_row > 7 or from_col < 0 or from_col > 7:
            raise Exception("Coordenadas incorrectas")
        if to_row < 0 or to_row > 7 or to_col < 0 or to_col > 7:
            raise Exception("Coordenadas incorrectas")
        else:
            return True



class TestAjedrez(unittest.TestCase):
    def setUp(self):
        posiciones = [[None]*8 for _ in range(8)]  # Crea una matriz 8x8 de None
        tablero = Tablero(posiciones)
        self.__ajedrez__ = Ajedrez(tablero) 

    def test_cambiar_turno(self):
        self.assertEqual(self.__ajedrez__.__turno__, "BLANCAS")
        self.__ajedrez__.cambiar_turno()
        self.assertEqual(self.__ajedrez__.__turno__, "NEGRAS")

    def test_validar_coordenadas(self):
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(-1, 0, 0, 0)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, -1, 0, 0)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, 0, -1, 0)
        with self.assertRaises(Exception):
            self.__ajedrez__.validar_coordenadas(0, 0, 0, -1)

if __name__ == '__main__':
    unittest.main()