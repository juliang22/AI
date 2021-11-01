# CS76: AI - 21F - PA5 - Sudoku Solver - Julian Grunauer 10/31/21

## How to run
Run ```python3 solve_sudoku.py <insert_rule-set_here>``` to see use GSAT/WALKSAT to solve sudoku problems. Included in this repo are the following rule-sets in increasing difficulty: 
* one_cell.cnf: rules that ensure that the upper left cell has exactly one value between 1 and 9.
* all_cells.cnf: rules that ensure that all cells have exactly one value between 1 and 9.
* rows.cnf: rules that ensure that all cells have a value, and every row has nine unique values.
* rows_and_cols.cnf: rules that ensure that all cells have a value, every row has nine unique values, and every column has nine unique * values.
* rules.cnf: adds block constraints, so each block has nine unique values. (The complete rules for an empty sudoku board.)
* puzzle1.cnf: Adds a few starting values to the game to make a puzzle.
* puzzle2.cnf: Some different starting values.
* puzzle_bonus.cnf: Several starting values. Difficult; solution welcome but not required.

Uncomment code in solve_sudoku.py to use either GSAT or WALKSAT (currently set on WALKSAT as GSAT is not capable of solving any rule set past rows.cnf).

## Problem Description
==Required tasks==
1. Implement GSAT
The GSAT algorithm intuition is described on Wikipedia. It is quite simple. The pseudocode can be found at the related research paper.

1) Choose a random assignment (a model).
2) If the assignment satisfies all the clauses, stop.
3) Pick a number between 0 and 1. If the number is greater than some threshold h, choose a variable uniformly at random and flip it; go back to step 2.
3) Otherwise, for each variable, score how many clauses would be satisfied if the variable value were flipped.
4) Uniformly at random choose one of the variables with the highest score. (There may be many tied variables.) Flip that variable. Go back to step 2.

Implement GSAT (see implementation notes below before starting). You should be able to solve the first few .cnf problems with your implementation. The real sudoku puzzles are probably too hard to solve with GSAT in a reasonable time frame, however.

2. Implement WalkSAT
The scoring step in GSAT can be slow. If there are 729 variables, and a few thousand clauses, the obvious scoring method (and I haven't clearly thought out a better one) loops more than a million times. And that only flips a single bit in the assignment. Ouch.

WalkSAT chooses a smaller number of candidate variables that might be flipped. For the current assignment, some clauses are unsatisfied. Choose one of these unsatisfied clauses uniformly at random. The resulting set will be your candidate set. Use these candidate variables when scoring. Implement WalkSAT.

I found that WalkSAT needed very many iterations to solve puzzle1.cnf and puzzle2.cnf. I limited to 100,000 iterations, and chose .3 as my magic threshold value for a random move in step 3.

There are many variations on WalkSAT. Some variations do a GSAT step occasionally to try to escape local minima. You should implement the simple version described above as a first step, although exploration of variants is always welcome as an extension.