import unittest
from parameterized import parameterized
from interface import (
    Interface,
    IncorrectNumber,
)


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.interface = Interface()

    @parameterized.expand([('4', '2', '4'),
                           ('4', '4', '5'),
                           ('3', '6', '4'),
                           ('8', '3', '2'),
                           ])
    def test_valid_number(self, number, pos_x, pos_y):
        self.assertTrue(
            self.interface.validate_input_number(number, pos_x, pos_y))

    @parameterized.expand([('0', '2', '4'),
                           ('-1', '4', '5'),
                           ('-2', '6', '4'),
                           ('-3', '3', '2'),
                           ])
    def test_input_small_number(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('10', '2', '4'),
                           ('11', '4', '5'),
                           ('100', '6', '4'),
                           ('15', '3', '2'),
                           ])
    def test_input_big_number(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('4', '10', '4'),
                           ('4', '11', '5'),
                           ('3', '12', '4'),
                           ('8', '100', '2'),
                           ])
    def test_input_big_number_position_x(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('4', '-3', '4'),
                           ('4', '-1', '5'),
                           ('3', '-2', '4'),
                           ('8', '-5', '2'),
                           ])
    def test_input_small_number_position_x(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('4', '2', '10'),
                           ('4', '4', '11'),
                           ('3', '6', '12'),
                           ('8', '3', '15'),
                           ])
    def test_input_big_number_position_y(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('4', '2', '-1'),
                           ('4', '4', '-2'),
                           ('3', '6', '-3'),
                           ('8', '3', '-8'),
                           ])
    def test_input_small_number_position_y(self, number, pos_x, pos_y):
        with self.assertRaises(IncorrectNumber):
            self.interface.validate_input_number(number, pos_x, pos_y)

    @parameterized.expand([('h', '2', '4'),
                           ('o', '4', '5'),
                           ('l', '6', '4'),
                           ('a', '3', '2'),
                           ])
    def test_input_letter(self, number, pos_x, pos_y):
        with self.assertRaises(ValueError):
            self.interface.validate_input_number(number, pos_x, pos_y)


if __name__ == '__main__':
    unittest.main()
