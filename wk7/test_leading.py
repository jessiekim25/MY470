import unittest
import leading  # here, importing the py file

class TestLeading(unittest.TestCase):
    '''Tests for leading.'''

    def test_word(self):
        '''Test a word'''
        word = 'bear'  # word as an input
        output = leading.leading_substrings(word)  ## Output structure: 'py file name'.function( )
        expected = ['b', 'be', 'bea', 'ber']
        self.assertEqual(expected, output, 'Argument is a word')
        
    def test_empty(self):
        word = ''
        output = leading.leading_substrings(word)  
        expected = []
        self.assertEqual(expected, output, 'Argument is an empty list')
        

if __name__ == '__main__':
    unittest.main()
