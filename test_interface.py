import unittest

from Interface import ( 
    Interface,
    IncorrectNumber,
    NotNumber,
)


class TestSudoku(unittest.TestCase):

    #def setUp(self):
    #   self.interface = Interface()

    def test_valid_number(self):
        self.interface = Interface()
        self.interface.validate_input_number(5)
    
    def test_input_small_number(self):
        self.interface = Interface()
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(0)
    """
    def test_input_big_number(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(11)

    def test_input_letter(self):
        with self.assertRaises(NotNumber):
            self.interface.validate_input_number("l")
    """


if __name__ == '__main__':
    unittest.main()