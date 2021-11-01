# CS76: AI - 21F - PA5 - Sudoku Solver - Julian Grunauer 10/31/21
from display import display_sudoku_solution
import random, sys
from SAT import SAT

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])

    sat = SAT(sys.argv[1])

    # GSAT and WALKSAT algorithms
    # result = sat.find_solution(2000, .8, 'GSAT')
    result = sat.find_solution(100000, .8, 'WALKSAT')

    if result:
        display_sudoku_solution(result)