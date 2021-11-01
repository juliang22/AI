from Sudoku import Sudoku
import sys

def display_sudoku_solution(solution=None):

    test_sudoku = Sudoku()
    test_sudoku.read_solution(solution)
    print(test_sudoku)

if __name__ == "__main__":
    display_sudoku_solution()