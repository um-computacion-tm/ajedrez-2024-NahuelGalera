import unittest
from unittest.mock import patch
from ajedrez import Ajedrez
from exceptions import InvalidMove
from cli import main

class TestAjedrez(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'a', '2', 'a'])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with('Turno de las piezas BLANCA')

if __name__ == '__main__':
    unittest.main()