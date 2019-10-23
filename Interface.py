from Sudoku import (
    Sudoku,
    InvalidPosition,
    InvalidColumn,
    InvalidRow,
    InvalidRegion,
)

class incorrectNumber(Exception):
    pass

class notLetter(Exception):
    pass

class Interface():
    def __init__(self):
        self.sudoku = Sudoku("534678912672195348198342567859761423426853791713924856961537284287419635345286x79")
    
    def validate_input_number(self, number):
        try:
            if number >= 10 or number <= 0:
                raise incorrectNumber
            if not int:
                raise notLetter
        except incorrectNumber:
            print("Ha ingresado incorrecto, debe ingresar un numero entre 1 y 9")
            self.play_sudoku()
        except notLetter:
            print("Ha ingresado una letra")

    def play_sudoku(self):
        print(self.sudoku.print_board())
        try:
            while not self.sudoku.is_over():
                self.number = int(input("Ingrese un numero: "))
                self.validate_input_number(self.number)
                self.position_x = int(input("Ingrese la posicion x: "))
                self.position_y = int(input("Ingrese la posicion y: "))
                self.sudoku.put_number(self.position_x,self.position_y,self.number)
                print(self.sudoku.print_board())
        
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



Interface().play_sudoku()

            
