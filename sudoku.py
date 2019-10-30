class InvalidPosition(Exception):
    pass


class InvalidColumn(Exception):
    pass


class InvalidRow(Exception):
    pass


class InvalidRegion(Exception):
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
        for _ in range(9):
            column.append(self.original_board[lineal_position])
            lineal_position += 1
        return column

    def number_in_region(self, position_x, position_y):
        region = []
        reg_x_init = position_x // 3
        reg_y_init = position_y // 3
        for i in range(3):
            for j in range(3):
                pos = i*9 + j + reg_x_init * 3 * 9 + reg_y_init * 3
                region.append(self.original_board[pos])
        return region

    def put_number(self, position_x, position_y, number):
        lineal_position = (position_x * 9) + position_y
        if lineal_position in self.position_fixed:
            raise InvalidPosition()
        elif str(number) in self.number_in_column(lineal_position):
            raise InvalidColumn()
        elif str(number) in self.number_in_row(lineal_position):
            raise InvalidRow()
        elif str(number) in self.number_in_region(position_x, position_y):
            raise InvalidRegion()
        else:
            self.original_board[lineal_position] = str(number)
            return True
        
    def print_board(self):
        board=""
        for i in range(0,9):
            for j in range(0,9):
                board += self.original_board[(i*9)+j] + " "
            board+="\n"
        return board
    
    def is_over(self):
        return 'x' not in self.original_board
