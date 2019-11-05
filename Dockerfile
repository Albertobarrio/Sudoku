FROM python:3

RUN git clone https://github.com/Albertobarrio/Sudoku.git 

WORKDIR /Sudoku

CMD [ "python3" , "./suite_tests.py" ]