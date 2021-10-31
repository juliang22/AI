from Sudoku import Sudoku
import sys

def display_sudoku_solution(solution):

    test_sudoku = Sudoku()
    # test_sudoku.read_sol('puzzle1.sud')
    test_sudoku.read_sol(solution)
    print(test_sudoku)

if __name__ == "__main__":
    display_sudoku_solution()