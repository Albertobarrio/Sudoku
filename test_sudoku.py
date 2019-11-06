import unittest
from parameterized import parameterized
from sudoku import (
    Sudoku,
    InvalidPosition,
    InvalidColumn,
    InvalidRow,
    InvalidRegion,
)


class TestSudoku(unittest.TestCase):
    @parameterized.expand([(0, 2, 4, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (4, 4, 5, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (3, 6, 4, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (8, 3, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_put_number_ok(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.put_number(pos_x, pos_y, number))

    @parameterized.expand([(0, 0, 6, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (1, 3, 1, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (4, 5, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (8, 8, 7, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_put_number_invalin_position(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        with self.assertRaises(InvalidPosition):
            sudoku.put_number(pos_x, pos_y, number)

    @parameterized.expand([(1, 1, 3, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (4, 2, 8, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (6, 3, 8, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (7, 7, 6, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_put_number_invalid_column(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        with self.assertRaises(InvalidColumn):
            sudoku.put_number(pos_x, pos_y, number)

    @parameterized.expand([(0, 2, 7, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (3, 3, 6, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (6, 5, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (8, 2, 9, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_put_number_invalid_row(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        with self.assertRaises(InvalidRow):
            sudoku.put_number(pos_x, pos_y, number)

    @parameterized.expand([(1, 1, 8, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (3, 3, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (7, 7, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (6, 5, 4, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_put_number_invalid_region(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        with self.assertRaises(InvalidRegion):
            sudoku.put_number(pos_x, pos_y, number)

    @parameterized.expand([("53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ("75x9x8x4xxx4x7619x1xx34xx65xxxx9xx248x2x5x6x9xx7x8xx314x9xx12x3xx37xx4x6x2x4x598x"),
                           ("x3xx7869xx7x6x92xxx96x3xx7xxx1x547x972xxxxx46xx579x3x2xxx867xx36xx9x14x7x1xx4x96x"),
                           ("53x8x1xx697243xxxxxxxx792x3xxxxx29xxx6938xx1x15xxx4x3232179xxxxx4x21x5x97xxx4x321"),
                           ])
    def test_game_not_over(self, board):
        sudoku = Sudoku(board)
        over = sudoku.is_over()
        self.assertFalse(over)

    @parameterized.expand([(0, 2, 4, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (4, 4, 5, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (3, 6, 4, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           (8, 3, 2, "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ])
    def test_game_not_over_adding_numbers(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        sudoku.put_number(pos_x, pos_y, number)
        over = sudoku.is_over()
        self.assertFalse(over)

    @parameterized.expand([("534678912672195348198342567859761423426853791713924856961537284287419635345286179"),
                           ("812753649943682175675491283154237896369845721287169534521974368438526917796318452"),
                           ])
    def test_win(self, board):
        sudoku = Sudoku(board)
        over = sudoku.is_over()
        self.assertTrue(over)

    @parameterized.expand([(8, 6, 1, "534678912672195348198342567859761423426853791713924856961537284287419635345286x79"),
                           (0, 4, 5, "8127x3649943682175675491283154237896369845721287169534521974368438526917796318452"),
                           ])
    def test_win_after_last_play(self, pos_x, pos_y, number, board):
        sudoku = Sudoku(board)
        sudoku.put_number(pos_x, pos_y, number)
        over = sudoku.is_over()
        self.assertTrue(over)

    @parameterized.expand([("53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"),
                           ("75x9x8x4xxx4x7619x1xx34xx65xxxx9xx248x2x5x6x9xx7x8xx314x9xx12x3xx37xx4x6x2x4x598x"),
                           ("x3xx7869xx7x6x92xxx96x3xx7xxx1x547x972xxxxx46xx579x3x2xxx867xx36xx9x14x7x1xx4x96x"),
                           ("53x8x1xx697243xxxxxxxx792x3xxxxx29xxx6938xx1x15xxx4x3232179xxxxx4x21x5x97xxx4x321"),
                           ])
    def test_no_win(self, board):
        sudoku = Sudoku(board)
        over = sudoku.is_over()
        self.assertFalse(over)

    def test_print_board(self):
        sudoku = Sudoku(
            "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79")
        self.assertEqual(sudoku.print_board(), "5 3 x x 7 x x x x \n"
                         "6 x x 1 9 5 x x x \n"
                         "x 9 8 x x x x 6 x \n"
                         "8 x x x 6 x x x 3 \n"
                         "4 x x 8 x 3 x x 1 \n"
                         "7 x x x 2 x x x 6 \n"
                         "x 6 x x x x 2 8 x \n"
                         "x x x 4 1 9 x x 5 \n"
                         "x x x x 8 x x 7 9 \n")


if __name__ == '__main__':
    unittest.main()
