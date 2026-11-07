import clingo
import clingo.application
import sys
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):
    def main (self, control, files):
        control.load("sudoku.lp")

        for input in files:
            control.load(input)
        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)
if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp(), sys.argv[1:])