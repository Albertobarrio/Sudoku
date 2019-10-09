import unittest

from Sudoku import (
    Sudoku,
    InvalidPosition,
    InvalidColumn,
    InvalidRow,
    InvalidBlock,
)


class TestSudoku(unittest.TestCase):

    def test_put_number_1(self):
        sudoku = Sudoku("53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidPosition):
            sudoku.put_number(0, 0, 6)  # x,y,numero
    
    def test_put_number_2(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidColumn):
            sudoku.put_number(2, 0, 5)  
    
   
    def test_put_number_3(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidRow):
            sudoku.put_number(0, 3, 7)  
    
    
    
    """
    def test_game_not_over(self):
        sudoku = Sudoku( "53xx7xxxx 6xx195xxx x98xxxx6x 8xxx6xxx3 4xx8x3xx1 7xxx2xxx6 x6xxxx28x xxx419xx5 xxxx8xx79")
        over = sudoku.is_over()
        self.assertFalse(over)
    
   
    
    
    
    def test_put_number_4(self):
        sudoku = Sudoku( "53xx7xxxx 6xx195xxx x98xxxx6x 8xxx6xxx3 4xx8x3xx1 7xxx2xxx6 x6xxxx28x xxx419xx5 xxxx8xx79")
        self.assertEqual(sudoku.put_number(3,9,1),"Numero incorrecto,repetido en la region")#x,y,numero
    
    def test_put_number_5(self):
        sudoku = Sudoku( "53xx7xxxx 6xx195xxx x98xxxx6x 8xxx6xxx3 4xx8x3xx1 7xxx2xxx6 x6xxxx28x xxx419xx5 xxxx8xx79")
        self.assertEqual(sudoku.put_number(3,9,1),"El numero se pudo colocar")#x,y,numero

    def test_no_win(self):
        sudoku = Sudoku( "53xx7xxxx 6xx195xxx x98xxxx6x 8xxx6xxx3 4xx8x3xx1 7xxx2xxx6 x6xxxx28x xxx419xx5 xxxx8xx79")
        over = sudoku.is_over()
        self.assertFalse(over)
    
    def test_no_win_after_play(self):
        sudoku = Sudoku( "53xx7xxxx 6xx195xxx x98xxxx6x 8xxx6xxx3 4xx8x3xx1 7xxx2xxx6 x6xxxx28x xxx419xx5 xxxx8xx79")
        sudoku.put_number(3,9,1)
        over = sudoku.is_over()
        self.assertFalse(over)

    def test_win(self):
        sudoku = Sudoku( "tablero lleno")
        over = sudoku.is_over()
        self.assertTrue(over)

    def test_win_after_last_play(self):
        sudoku = Sudoku( "tablero casi lleno")
        sudoku.put_number(3,9,1)
        over = sudoku.is_over()
        self.assertTrue(over)
    """


if __name__ == '__main__':
    unittest.main()