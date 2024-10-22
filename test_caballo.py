import unittest
from caballo import Caballo

class TestCaballo(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method verifies that the __str__ method of the Caballo class returns 'N' for a white piece and 'n' for a black piece.
        '''
        caballo_blanco = Caballo('BLANCA', None)
        caballo_negro = Caballo('NEGRA', None)
        self.assertEqual(str(caballo_blanco), 'N')
        self.assertEqual(str(caballo_negro), 'n')

    def test_generate_knight_directions(self):
        '''
        The function test_generate_knight_directions verifies that the generate_knight_directions method of the Caballo class returns the correct list of directions for a knight piece.
        '''
        caballo = Caballo('BLANCA', None)
        expected_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(caballo.generate_knight_directions(), expected_directions)

if __name__ == '__main__':
    unittest.main()