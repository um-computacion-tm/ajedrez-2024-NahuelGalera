import unittest
from unittest.mock import patch, Mock
from cli import main, jugar, obtener_movimiento
from exceptions import GameOver  # Add this import

class TestAjedrezCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'a', '2', 'a'])
    def test_obtener_movimiento(self, mock_input):
        from_fila, from_col, to_fila, to_col = obtener_movimiento()
        self.assertEqual(from_fila, 0)
        self.assertEqual(from_col, 0)
        self.assertEqual(to_fila, 1)
        self.assertEqual(to_col, 0)

    @patch('builtins.input', side_effect=['r'])
    def test_obtener_movimiento_rendirse(self, mock_input):
        from_fila, from_col, to_fila, to_col = obtener_movimiento()
        self.assertEqual(from_fila, 'r')
        self.assertIsNone(from_col)
        self.assertIsNone(to_fila)
        self.assertIsNone(to_col)

    @patch('cli.Ajedrez')
    @patch('builtins.input', side_effect=['1', 'a', '2', 'a'])
    def test_jugar(self, mock_input, MockAjedrez):
        game = MockAjedrez()
        jugar(game)
        game.move.assert_called_once_with(0, 0, 1, 0)
        game.__str__.assert_called_once()
        game.turno.__str__.assert_called_once()

    @patch('cli.Ajedrez')
    @patch('builtins.input', side_effect=['r'])
    def test_jugar_rendirse(self, mock_input, MockAjedrez):
        game = MockAjedrez()
        jugar(game)
        game.rendirse.assert_called_once()
        game.__str__.assert_called_once()
        game.turno.__str__.assert_called_once()

    @patch('cli.jugar')
    @patch('cli.Ajedrez')
    def test_main(self, MockAjedrez, mock_jugar):
        game = MockAjedrez()
        mock_jugar.side_effect = GameOver("Game Over")
        with self.assertRaises(SystemExit):
            main()
        mock_jugar.assert_called_once_with(game)

if __name__ == '__main__':
    unittest.main()