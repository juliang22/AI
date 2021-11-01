# CS76: AI - 21F - PA5 - Sudoku Solver - Julian Grunauer 10/31/21

## Description
* How do your implemented algorithms work?
  * Each algorithm is implemented according to the pseudocode provided. GSAT initializes a random model based off of variables listed in the rule-set's clauses, randomly flips variables according to a certain threshold, and otherwise chooses the variable (out of all variables) that, if flipped, satisfies the most amount of clauses. WALKSAT works similarly, however, instead of searching through all variables, it selects a variables from the list of clauses that have yet to be satisfies, thus reducing the search space/time complexity. 
* What design decisions did you make?
  * I decided to use a dictionary for the model because lookup time for dictionaries are a lot faster than lists. I also decided to select the variable that has been flipped the least amount of times (out of a selection of variables that satisfy the most amount of clauses), which helped to speed up the compute time. 
* How you laid out the problems?
  * The file ```solve_sudoku.py``` runs either GSAT or WALKSAT by calling ```SAT.py``` then displays the results using ```display.py```.

## Evaluation
* Do your implemented algorithms actually work? How well? 
  * All algorithms work exactly as they should. While WALKSAT drastically improves search time over GSAT, it still runs quite slow for the full puzzles (puzzle 1 averages at about 3 minutes, while puzzle 2 is about 10 minutes). The least-flipped heuristic definitely helped to speed up the computation, but despite this, the algorithm is still quite slow. The bonus puzzle was unable to be solved in 100,000 flips. 
* If it doesn’t work, can you tell why not? What partial successes did you have that deserve partial credit? 
  * Everything works as expected.
