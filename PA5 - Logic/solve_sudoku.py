from display import display_sudoku_solution
import random, sys
from SAT import SAT

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    # puzzle_name = 'one_cell.cnf'
    # sol_filename = puzzle_name + ".sol"
    # display_sudoku_solution('puzzle1.sud')
    # exit()

    sat = SAT(sys.argv[1])
    # result = sat.find_solution(2000, .75, 'GSAT')
    result = sat.find_solution(100000, .7, 'WALKSAT')
    display_sudoku_solution(result)


    if result:
        sat.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)