import unittest
from unittest.mock import MagicMock, patch
from ajedrez import Ajedrez
from tablero import Tablero
from exceptions import GameOver
from io import StringIO
from piezas import Pieza

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        self.__ajedrez__ = Ajedrez()
        self.__ajedrez__.__tablero__ = MagicMock(spec=Tablero)
        self.__ajedrez__.__tablero__.__board__ = [[None for _ in range(8)] for _ in range(8)]  # Añadir el atributo __board__

    def test_inicializacion(self):
        self.assertIsInstance(self.__ajedrez__.__tablero__, Tablero)
        self.assertEqual(self.__ajedrez__.__turno__, 'BLANCA')
        self.assertFalse(self.__ajedrez__.__terminado__)
        self.assertIsNone(self.__ajedrez__.__ganador__)

    def test_move_valido(self):
        pieza_mock = MagicMock()
        pieza_mock.color = 'BLANCA'
        pieza_mock.is_valid_move.return_value = True
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza_mock

        self.assertTrue(self.__ajedrez__.move(0, 0, 1, 1))
        self.__ajedrez__.__tablero__.mover_pieza.assert_called_once_with(0, 0, 1, 1)
        self.assertEqual(self.__ajedrez__.__turno__, 'NEGRA')

    def test_move_invalido(self):
        pieza_mock = MagicMock()
        pieza_mock.color = 'BLANCA'
        pieza_mock.is_valid_move.return_value = False
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza_mock

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.__ajedrez__.move(0, 0, 1, 1))
            output = mock_stdout.getvalue()
            self.assertIn("Movimiento inválido.", output)

    def test_move_no_pieza_o_turno_incorrecto(self):
        self.__ajedrez__.__tablero__.get_piece.return_value = None

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.__ajedrez__.move(0, 0, 1, 1))
            output = mock_stdout.getvalue()
            self.assertIn("No es el turno de esta pieza o no hay pieza en la posición inicial.", output)

    def test_cambiar_turno(self):
        self.__ajedrez__.cambiar_turno()
        self.assertEqual(self.__ajedrez__.__turno__, 'NEGRA')
        self.__ajedrez__.cambiar_turno()
        self.assertEqual(self.__ajedrez__.__turno__, 'BLANCA')

    def test_rendirse(self):
        with self.assertRaises(GameOver) as context:
            self.__ajedrez__.rendirse('BLANCA')
        self.assertTrue(self.__ajedrez__.__terminado__)
        self.assertEqual(self.__ajedrez__.__ganador__, 'NEGRA')
        self.assertIn("El jugador con piezas BLANCA se ha rendido. El ganador es: NEGRA", str(context.exception))

    def test_empate(self):
        with self.assertRaises(GameOver) as context:
            self.__ajedrez__.empate()
        self.assertTrue(self.__ajedrez__.__terminado__)
        self.assertEqual(self.__ajedrez__.__ganador__, 'Empate')
        self.assertIn("El juego ha terminado en empate.", str(context.exception))

    def test_is_terminado(self):
        self.__ajedrez__.__tablero__.__board__ = [[None for _ in range(8)] for _ in range(8)]
        self.assertTrue(self.__ajedrez__.is_terminado())

    def test_ganador_negras(self):
        # Simular un tablero sin piezas blancas
        self.__ajedrez__.__tablero__.__board__[0][0] = MagicMock(spec=Pieza, color='NEGRA')
        self.assertEqual(self.__ajedrez__.obtener_ganador(), 'NEGRA')

    def test_ganador_blancas(self):
        # Simular un tablero sin piezas negras
        self.__ajedrez__.__tablero__.__board__[0][0] = MagicMock(spec=Pieza, color='BLANCA')
        self.assertEqual(self.__ajedrez__.obtener_ganador(), 'BLANCA')

if __name__ == '__main__':
    unittest.main()