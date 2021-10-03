# PA2 - Mazeworld 
### Julian Grunauer - 9/30/21 - CS76: Artificial Intelligence

## Discussion Questions
1. If there are k robots, how would you represent the state of the system? Hint -- how many numbers are needed to exactly reconstruct the locations of all the robots, if we somehow forgot where all of the robots were? Further hint. Do you need to know anything else to determine exactly what actions are available from this state?
* k*2 numbers are needed to represent all of the nodes in the form (node_1_x, node_1_y, node_n_x, node_n_y, ..., node_k_x, node_k_y).
* To determine what actions to take, you need to know the width and height of the maze as well as the goal locations that the robots are trying to get to.


2. Give an upper bound on the number of states in the system, in terms of n and k.

* The upper limit on the number of states in the system would be a maze with no walls. The upper bound on the number of states is k* n^2*(n^2-1)...*(n^2-k + 1) because for each k robots moving the state is the number of squares it could be in.


3. Give a rough estimate on how many of these states represent collisions if the number of wall squares is w, and n is much larger than k.
* The estimate of the number of states that could represent collisions is k* n^2-w*(n^2-w-1)...*(n^2-k-w + 1) because this would represent the total number of legal states substracting the amount of walls in each location.

4. If there are not many walls, n is large (say 100x100), and several robots (say 10), do you expect a straightforward breadth-first search on the state space to be computationally feasible for all start and goal pairs? Why or why not?
* In the worst case scenario for this problem, the robots would have to visit every single node in the maze. Since BFS stores each of the nodes it visits, the memory cost for such a algorithm would be extremely high and thus not feasible. Going off of the upper limit of the amount of states from question 2, the robot would have to visit 10* 100^2*(100^2-1)...*(100^2-10 + 1) which would be an extraordinary amount of memory cost. 


5. Describe a useful, monotonic heuristic function for this search space. Show that your heuristic is monotonic. See the textbook for a formal definition of monotonic.
It may seem that you can just plan paths for the robots independently using three different breadth-first-searches, but this approach won't work very well if the robots get close to one another or have to move around one another. Therefore, you should plan paths in the complete state space for the system.
* The manhattan heuristic represents the minimum amount of moves from a node location to the goal while still remaining consistent. Since this heuristic represents the most optimal path to the goal, while not overestimating the cost, this is the best heuristic. 

6. Describe why the 8-puzzle in the book is a special case of this problem. Is the heuristic function you chose a good one for the 8-puzzle?
* The 8-puzzle is a subset of the maze problem because it is the case where you take a maze with no walls and fill in the maze with all robots except for one space. The manhattan heuristic is still the best heuristic for this maze. 

7. The state space of the 8-puzzle is made of two disjoint sets.  Describe how you would modify your program to prove this. (You do not have to implement this.)
* The state space of the 8-puzzle is split into solvable and unsolvable puzzles. To prove this, our program could check the state space at the beginning of the algorithm and verify that it is solvable by checking the amount of inversions. If the amount of inversions is even, then it is solvable, if it is odd, you would terminate the problem because you know it won't be solvable. 


1. Describe what heuristic you used for the A* search. Is the heuristic optimistic? Are there other heuristics you might use? (An excellent might compare a few different heuristics for effectiveness and make an argument about optimality.)
* I used the length of the state as the heuristic. This heuristic is optimistic, but not the most optimal heursitic. Another heuristic that would improve this algorithm would be to use the log(2) of the length of the state because the amount of possible states is cut in half every for every action in the path.

