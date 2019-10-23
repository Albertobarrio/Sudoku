import unittest

from Sudoku import (
    Sudoku,
    InvalidPosition,
    InvalidColumn,
    InvalidRow,
    InvalidRegion,
)


class TestSudoku(unittest.TestCase):

    def test_put_number_1(self):
        sudoku = Sudoku("53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidPosition):
            sudoku.put_number(0, 0, 6)  # x,y,numero
    
    def test_put_number_2(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidColumn):
            sudoku.put_number(2, 0, 5)  # x,y,numero
    
    def test_put_number_3(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidRow):
            sudoku.put_number(0, 3, 7)  # x,y,numero
    
    def test_put_number_4(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        with self.assertRaises(InvalidRegion):
            sudoku.put_number(4, 1, 7)  # x,y,numero
        
    def test_put_number_5(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        self.assertTrue(sudoku.put_number(0, 2, 4))  # x,y,numero

    def test_game_not_over(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        over = sudoku.is_over()
        self.assertFalse(over)

    def test_game_not_over_2(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        sudoku.put_number(0, 2, 4)
        sudoku.put_number(0, 3, 6)
        sudoku.put_number(0, 5, 8)
        over = sudoku.is_over()
        self.assertFalse(over)
    
    def test_win(self):
        sudoku = Sudoku( "534678912672195348198342567859761423426853791713924856961537284287419635345286179")
        over = sudoku.is_over()
        self.assertTrue(over)
    
    def test_win_after_last_play(self):
        sudoku = Sudoku( "534678912672195348198342567859761423426853791713924856961537284287419635345286x79")
        sudoku.put_number(8, 6, 1)
        over = sudoku.is_over()
        self.assertTrue(over)
    
    def test_no_win(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        over = sudoku.is_over()
        self.assertFalse(over)    

    def test_print_board(self):
        sudoku = Sudoku( "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        self.assertEqual(sudoku.print_board(),"5 3 x x 7 x x x x \n" 
                                              "6 x x 1 9 5 x x x \n" 
                                              "x 9 8 x x x x 6 x \n" 
                                              "8 x x x 6 x x x 3 \n" 
                                              "4 x x 8 x 3 x x 1 \n" 
                                              "7 x x x 2 x x x 6 \n" 
                                              "x 6 x x x x 2 8 x \n" 
                                              "x x x 4 1 9 x x 5 \n" 
                                              "x x x x 8 x x 7 9 \n" )


if __name__ == '__main__':
    unittest.main()