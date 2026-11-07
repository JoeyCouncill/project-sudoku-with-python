import clingo
import clingo.application
import sys


class ClingoApp(clingo.application.Application):
    def main (self, control, files):
        control.load("sudoku.lp")

        for input in files:
            control.load(input)
        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        sorted_symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(symbol) for symbol in sorted_symbols))

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp(), sys.argv[1:])