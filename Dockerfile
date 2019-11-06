FROM python:3

RUN git clone https://github.com/Albertobarrio/Sudoku.git && pip install requests && pip install parameterized

WORKDIR /Sudoku

CMD [ "python3" , "./suite_tests.py" ]