import unittest
from piezas import Pieza

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.tablero_mock = "tablero_mock"
        self.pieza = Pieza('BLANCA', self.tablero_mock)

    def test_inicializacion(self):
        print("Probando inicialización...")
        self.assertEqual(self.pieza.color, 'BLANCA')
        self.assertEqual(self.pieza.tablero, self.tablero_mock)
        print("Prueba completada: inicialización.")

    def test_propiedades(self):
        print("Probando propiedades...")
        self.assertEqual(self.pieza.color, 'BLANCA')
        self.assertEqual(self.pieza.tablero, self.tablero_mock)
        print("Prueba completada: propiedades.")

    def test_mover_no_implementado(self):
        print("Probando método mover no implementado...")
        with self.assertRaises(NotImplementedError):
            self.pieza.mover(0, 0, 1, 1)
        print("Prueba completada: método mover no implementado.")

    def test_is_valid_move_no_implementado(self):
        print("Probando método is_valid_move no implementado...")
        with self.assertRaises(NotImplementedError):
            self.pieza.is_valid_move(self.tablero_mock, 0, 0, 1, 1)
        print("Prueba completada: método is_valid_move no implementado.")

if __name__ == '__main__':
    unittest.main()