import unittest
from unittest.mock import MagicMock
from ajedrez import Ajedrez
from exceptions import InvalidMove, InvalidPlayer, GameOver

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        self.__ajedrez__ = Ajedrez()
        self.__ajedrez__.__tablero__ = MagicMock()

    def test_initialization(self):
        self.assertEqual(self.__ajedrez__.turno, "BLANCA")
        self.assertIsNone(self.__ajedrez__.ganador)
        self.assertFalse(self.__ajedrez__.is_rendicion())
        self.assertEqual(self.__ajedrez__.historial, [])

    def test_valid_move(self):
        piece = MagicMock()
        piece.color = "BLANCA"
        piece.valid_positions.return_value = True
        self.__ajedrez__.__tablero__.get_piece.return_value = piece

        self.__ajedrez__.move(0, 0, 1, 1)
        self.__ajedrez__.__tablero__.mover_pieza.assert_called_once_with(0, 0, 1, 1)
        self.assertEqual(self.__ajedrez__.historial, [((0, 0), (1, 1))])
        self.assertEqual(self.__ajedrez__.turno, "NEGRA")

    def test_invalid_move_no_piece(self):
        self.__ajedrez__.__tablero__.get_piece.return_value = None
        with self.assertRaises(InvalidMove):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_invalid_move_wrong_turn(self):
        piece = MagicMock()
        piece.color = "NEGRA"
        self.__ajedrez__.__tablero__.get_piece.return_value = piece
        with self.assertRaises(InvalidPlayer):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_invalid_move_invalid_position(self):
        piece = MagicMock()
        piece.color = "BLANCA"
        piece.valid_positions.return_value = False
        self.__ajedrez__.__tablero__.get_piece.return_value = piece
        with self.assertRaises(InvalidMove):
            self.__ajedrez__.move(0, 0, 1, 1)

    def test_game_over_by_resignation(self):
        self.__ajedrez__.rendirse()
        self.assertTrue(self.__ajedrez__.is_game_over())
        self.assertEqual(self.__ajedrez__.ganador, "NEGRA")

    def test_game_over_by_no_pieces(self):
        self.__ajedrez__.__tablero__.no_pieces_left.side_effect = lambda color: color == "BLANCA"
        self.assertTrue(self.__ajedrez__.is_game_over())
        self.assertEqual(self.__ajedrez__.ganador, "NEGRA")

    def test_reiniciar(self):
        self.__ajedrez__.move = MagicMock()
        self.__ajedrez__.reiniciar()
        self.assertEqual(self.__ajedrez__.turno, "BLANCA")
        self.assertIsNone(self.__ajedrez__.ganador)
        self.assertFalse(self.__ajedrez__.is_rendicion())
        self.assertEqual(self.__ajedrez__.historial, [])

if __name__ == '__main__':
    unittest.main()