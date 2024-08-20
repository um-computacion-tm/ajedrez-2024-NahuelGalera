import unittest
from codigo_ajedrez.piezas import Torre
from codigo_ajedrez.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        posiciones = [[None]*8 for _ in range(8)]
        self.tablero = Tablero(posiciones)

    def test_init(self):
        # Verifico la posicion de las torres
        posiciones_torre = [(0, 0, "NEGRA"), (0, 7, "NEGRA"), (7, 0, "BLANCA"), (7, 7, "BLANCA")]
        # Hago el bucle para no alargar tanto el test
        for x, y, color in posiciones_torre:
            torre = self.tablero.get_pieza(x, y)
            self.assertIsInstance(torre, Torre)
            self.assertEqual(torre.__color__, color)

    def test_get_pieza(self):
        # Verifico cuando get_pieza me de un valor None en una posicion vacia
        self.assertIsNone(self.tablero.get_pieza(1, 1))

if __name__ == '__main__':
    unittest.main()