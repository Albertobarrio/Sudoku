from sudoku import (
    Sudoku,
    InvalidPosition,
    InvalidColumn,
    InvalidRow,
    InvalidRegion,
)
from api import Api


class IncorrectNumber(Exception):
    pass


class Interface():
    def __init__(self):
        self.api = Api()
        board = self.api.make_board()
        self.sudoku = Sudoku(board)

    def validate_input_number(self, number, position_x, position_y):
        # Funcionalidad: Verifica si el valor ingresado es una letra o un
        # numero fuera de rango
        if number.isalpha() or position_x.isalpha() or position_y.isalpha():
            raise ValueError()
        if 1 <= int(number) <= 9 and -1 < int(position_x) < 9 and -1 < int(position_y) < 9:
            return True
        raise IncorrectNumber()

    def play_sudoku(self):

        print(self.sudoku.print_board())
        try:
            while not self.sudoku.is_over():
                self.number = input("Ingrese un numero: ")
                self.position_x = input("Ingrese la posicion x: ")
                self.position_y = input("Ingrese la posicion y: ")
                print("\n")
                if self.validate_input_number(self.number, self.position_x, self.position_y):
                    self.sudoku.put_number(int(self.position_x), int(
                        self.position_y), int(self.number))
                print(self.sudoku.print_board())
            print("Felicitaciones ganaste")

        except InvalidPosition:
            print("No se puedo colocar el numero, hay un numero fijo")
            self.play_sudoku()
        except InvalidRow:
            print("El numero ya esta  en la fila")
            self.play_sudoku()
        except InvalidColumn:
            print("El numero ya esta  en la columna")
            self.play_sudoku()
        except InvalidRegion:
            print("El numero ya esta en la region")
            self.play_sudoku()
        except IncorrectNumber:
            print("Ha ingresado incorrecto, debe ingresar un numero entre 1 y 9")
            self.play_sudoku()
        except ValueError:
            print("Ha ingresado una letra")
            self.play_sudoku()