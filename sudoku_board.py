from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            for column in range(1, 10):
                s += str(self.sudoku[(row, column)])
                if column in (3, 6):
                    s += "  "
                elif column < 9:
                    s += " "
            s += "\n"
            if row in (3, 6):
                s += "\n"
            elif column < 9:
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            if symbol.match("sudoku", 3):
                row = symbol.arguments[0].number
                column = symbol.arguments[1].number
                value = symbol.arguments[2].number
                sudoku[(row, column)] = value

        return cls(sudoku)
