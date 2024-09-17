import unittest
from ajedrez import Ajedrez
from exceptions import InvalidMove

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.__game__ = Ajedrez()

    def test_initial_turn(self):
        self.assertEqual(self.__game__.turno, "BLANCA")

    def test_move_changes_turn(self):
        # Mocking a valid move
        self.__game__.move(6, 0, 5, 0)  # Assuming this is a valid move for a pawn
        self.assertEqual(self.__game__.turno, "NEGRA")

    def test_rendirse(self):
        self.__game__.rendirse()
        self.assertTrue(self.__game__.is_rendicion())
        self.assertTrue(self.__game__.is_game_over())

    def test_no_pieces_left(self):
        # Mocking the no_pieces_left method in Tablero
        self.__game__.__tablero__.no_pieces_left = lambda color: color == "BLANCA"
        self.assertTrue(self.__game__.is_game_over())

    def test_invalid_move(self):
        with self.assertRaises(InvalidMove):
            self.__game__.move(0, 0, 4, 4)  # Assuming this is an invalid move

if __name__ == '__main__':
    unittest.main()