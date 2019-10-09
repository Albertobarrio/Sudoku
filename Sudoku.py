class InvalidPosition(Exception):
    pass


class InvalidColumn(Exception):
    pass


class InvalidRow(Exception):
    pass


class InvalidBlock(Exception):
    pass


class Sudoku():

    def __init__(self, board):
        self.original_board = list(board)
        self.position_fixed = []
        self.is_position_fixed(self.original_board)

    def is_position_fixed(self, original_board):
        for position, number in enumerate(self.original_board):
            if number != 'x':
                self.position_fixed.append(position)

    def number_in_column(self, lineal_position):
        column = []
        lineal_position = lineal_position % 9
        while lineal_position <= 80:
            column.append(self.original_board[lineal_position])
            lineal_position += 9
        return column

    def number_in_row(self, lineal_position):
        column = []
        lineal_position = (lineal_position // 9)*9
        for iterator in range(9):
            column.append(self.original_board[lineal_position])
            lineal_position += 1
        return column

    def number_in_block(self):

    def put_number(self, position_x, position_y, number):
        lineal_position = (position_x * 9) + position_y
        if lineal_position in self.position_fixed:
            raise InvalidPosition()
        elif str(number) in self.number_in_column(lineal_position):
            raise InvalidColumn()
        elif str(number) in self.number_in_row(lineal_position):
            raise InvalidRow()
