import unittest
from unittest.mock import MagicMock
from ajedrez import Ajedrez
from exceptions import InvalidMove, InvalidPlayer, GameOver

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        self.__ajedrez__ = Ajedrez()
        self.__ajedrez__.__tablero__ = MagicMock()

    def test_movimiento_valido(self):
        pieza = MagicMock()
        pieza.color = "BLANCA"
        pieza.valid_positions.return_value = True
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza

        self.__ajedrez__.move(0, 0, 1, 1)
        self.__ajedrez__.__tablero__.mover_pieza.assert_called_once_with(0, 0, 1, 1)
        self.assertEqual(self.__ajedrez__.historial, [((0, 0), (1, 1))])
        self.assertEqual(self.__ajedrez__.turno, "NEGRA")

    def test_movimiento_invalido_sin_pieza(self):
        self.__ajedrez__.__tablero__.get_piece.return_value = None
        with self.assertRaises(InvalidMove):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_movimiento_invalido_turno_incorrecto(self):
        pieza = MagicMock()
        pieza.color = "NEGRA"
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza
        with self.assertRaises(InvalidPlayer):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_movimiento_invalido_posicion_invalida(self):
        pieza = MagicMock()
        pieza.color = "BLANCA"
        pieza.valid_positions.return_value = False
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza
        with self.assertRaises(InvalidMove):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_cambio_de_turno(self):
        pieza = MagicMock()
        pieza.color = "BLANCA"
        pieza.valid_positions.return_value = True
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza

        self.__ajedrez__.move(0, 0, 1, 1)
        self.assertEqual(self.__ajedrez__.turno, "NEGRA")

    def test_fin_de_juego(self):
        pieza = MagicMock()
        pieza.color = "BLANCA"
        pieza.valid_positions.return_value = True
        self.__ajedrez__.__tablero__.get_piece.return_value = pieza
        self.__ajedrez__.is_game_over = MagicMock(return_value=True)

        with self.assertRaises(GameOver):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_rendirse(self):
        with self.assertRaises(GameOver):
            self.__ajedrez__.rendirse()
        self.assertTrue(self.__ajedrez__.is_rendicion())
        self.assertEqual(self.__ajedrez__.ganador, "NEGRA")

    def test_reiniciar(self):
        self.__ajedrez__.move = MagicMock()
        self.__ajedrez__.reiniciar()
        self.assertEqual(self.__ajedrez__.turno, "BLANCA")
        self.assertIsNone(self.__ajedrez__.ganador)
        self.assertEqual(self.__ajedrez__.historial, [])

if __name__ == '__main__':
    unittest.main()