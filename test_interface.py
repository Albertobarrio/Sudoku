import unittest

from Interface import ( 
    Interface,
    IncorrectNumber,
)

# FIXME: Arreglar las recursividades 
# TODO: Validar las coordenadas
# TODO: Api

class TestSudoku(unittest.TestCase):

    def setUp(self):
       self.interface = Interface()

    def test_valid_number(self):
        self.assertTrue(self.interface.validate_input_number(1,8,6))
    
    def test_input_small_number(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(0,8,6)
    
    def test_input_big_number(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(11,8,6)


    def test_input_big_number_position_x(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(1,11,6)


    def test_input_small_number_position_x(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(1,-1,6)

    def test_input_big_number_position_y(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(1,8,11)

    def test_input_small_number_position_y(self):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(1,8,11)

    def test_input_letter(self):
        with self.assertRaises(TypeError):
            self.interface.validate_input_number("l",8,6)

if __name__ == '__main__':
    unittest.main()