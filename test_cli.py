import unittest
from unittest.mock import patch
from ajedrez import Ajedrez
from exceptions import InvalidMove, GameOver, InvalidPiece, InvalidPlayer
from cli import jugar 

class TestAjedrez(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'a', '2', 'b'])
    def test_jugar(self, mock_input):
        game = Ajedrez()
        try:
            jugar(game)
        except GameOver:
            pass
        # Aquí puedes agregar aserciones para verificar que el estado del juego es el esperado después de jugar

if __name__ == '__main__':
    unittest.main()