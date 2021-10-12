# CS76: AI - 21F - PA3 - Chess - Julian Grunauer 10/11/21

## Description
In this lab, I implemented three different versions of the minimax algorithm: normal, alphabeta pruning, and iterative deepening. I chose to use the heuristic algorithm described in the book "Artifical Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig. This algorithm ranks each piece by its in-game value, then finds the sum of the products of each of the pieces and their amount. The difference between the white's score and the black's score functions as our heuristic value (where a higher value is better for white, and a lower for black). Minimax uses this heuristic to recursively track every possible move up to a certain depth and return the best moves that the players could make at every level. This is extremely time intensive (b^m), as every single move is explored fully. This can be improved by pruning moves that won't affect returned score (alphabeta pruning). Further, if the algorithm is taking an unreasonable amount of time, iterative deepening can be used to return the best score found thus far.

## Evaluation
My algorithms are all implemented correctly. Each algorithm beats randomAI (and myself) with impressive speed. Each algorithm returns the same move. This was verified by checking planned moves that I (a human player) mapped out beforehand and checking to see if minimax and alphabeta_pruning_minimax returned the same results. Pruning should only reduce the amount of time it takes for the algorithm to run, the actual value returned should be the same. 

## Discussion Questions
Minimax and cutoff test: Vary maximum depth to get a feeling of the speed of the algorithm. Also, have the program print the number of calls it made to minimax as well as the maximum depth.  Record your observations.

Results of MinimaxAI playing against RandomAI
* Count is 420 at depth: 3
* Count is 441 at depth: 3
* Count is 462 at depth: 3
* Count is 565 at depth: 3
* Count is 752 at depth: 3
* Count is 711 at depth: 3
* Count is 772 at depth: 3
* Checkmate: g4h5
* Outcome(termination=<Termination.CHECKMATE: 1>, winner=True)
* White Wins!

 
* Observations
  * It seems that a couple hundred calls are made per move in the game. This can definitely be improved with pruning. I implemented an evaluative function from the beginning as seen in the results above. With no evaluative function, the program would operate randomly (whatever order the moves are generated then selected).

Evaluation function: Describe the evaluation function used, vary the allowed depth, and discuss and document the results.
* Evaluative Function
  * I used the heurstic described in the book: pieces are given value points according to their in-game worth. The functions sums the products of the amount of each of the piece and their value and then returns the difference between white vs black scores. This allows the white side to prefer maximizing in the minimax algorithm and black to prefer minimizing. 
  * Minimax runs best at depth 3. Depth 4 is slow, but manageable, while a depth of 5 is too slow for realistic gameplay. These results can definitely be sped up using pruning.

Alpha-beta: Record your observations on move-reordering in your document.
* At depth 5, unlike normal minimax, the algorithm, while slow, runs in a reasonable amount of time. With move reordering, the algorithm moved faster when their were captures in the next move, being that captured moves (which usually are high priority) are at the front of the move list, allowing other moves to be pruned faster.

Iterative deepening: Verify that for some start states, best_move changes (and hopefully improves) as deeper levels are searched. Discuss the observations.
* Yes, running iterative deepening on alpha_beta_pruning, causes the temporary moves returned at lower levels of recurision to improve as the depth increases. It seems (based on observation) lower levels of recursion will prioritize easy moves with low values (like capturing a pawn) over strategy-oriented moves that increase the odds of winning significantly more. 