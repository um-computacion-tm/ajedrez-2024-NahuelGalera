import unittest
from tablero import Tablero
from unittest.mock import MagicMock

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.__tablero__ = Tablero()

        # Mock the move method of each piece to always return True
        for fila in self.__tablero__.__tablero__:  # Accediendo al atributo protegido
            for pieza in fila:
                if pieza != ' ':
                    pieza.mover = MagicMock(return_value=True)

    def test_mover_pieza(self):
        # Verificar que la pieza en la posición (1, 0) es un "Peon('blanco')"
        self.assertEqual(str(self.__tablero__.get_pieza(1, 0)), "Peon('blanco')")

        # Mover una pieza blanca
        self.__tablero__.mover_pieza((1, 0), (2, 0))

        # Verificar que la pieza se ha movido correctamente
        self.assertEqual(str(self.__tablero__.get_pieza(2, 0)), "Peon('blanco')")
        self.assertEqual(str(self.__tablero__.get_pieza(1, 0)), ' ')