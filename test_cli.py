import unittest
from unittest.mock import patch
from io import StringIO
from ajedrez import Ajedrez
from cli import main, jugar
from exceptions import GameOver

class TestAjedrez(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'a', '2', 'b'])
    def test_jugar(self, mock_input):
        game = Ajedrez()
        try:
            jugar(game)
        except GameOver:
            pass
        # Aquí puedes agregar aserciones para verificar que el estado del juego es el esperado después de jugar

class TestAjedrezCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['r'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_rendirse(self, mock_stdout, mock_input):
        game = Ajedrez()
        jugar(game)
        output = mock_stdout.getvalue()
        self.assertIn("El jugador con piezas BLANCA se ha rendido.", output)

    @patch('builtins.input', side_effect=['1', 'a', '3', 'a', 'r'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_and_rendirse(self, mock_stdout, mock_input):
        game = Ajedrez()
        jugar(game)
        output = mock_stdout.getvalue()
        self.assertIn("El jugador con piezas NEGRA se ha rendido.", output)

if __name__ == '__main__':
    unittest.main()