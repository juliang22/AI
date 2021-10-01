# PA2 - Mazeworld 
### Julian Grunauer - 9/30/21 - CS76: Artificial Intelligence

## Discussion Questions
1. If there are k robots, how would you represent the state of the system? Hint -- how many numbers are needed to exactly reconstruct the locations of all the robots, if we somehow forgot where all of the robots were? Further hint. Do you need to know anything else to determine exactly what actions are available from this state?

2. Give an upper bound on the number of states in the system, in terms of n and k.

3. Give a rough estimate on how many of these states represent collisions if the number of wall squares is w, and n is much larger than k.

4. If there are not many walls, n is large (say 100x100), and several  robots (say 10), do you expect a straightforward breadth-first search on the state space to be computationally feasible for all start and goal pairs? Why or why not?

5. Describe a useful, monotonic heuristic function for this search space. Show that your heuristic is monotonic. See the textbook for a formal definition of monotonic.
It may seem that you can just plan paths for the robots independently using three different breadth-first-searches, but this approach won't work very well if the robots get close to one another or have to move around one another. Therefore, you should plan paths in the complete state space for the system.

6. Describe why the 8-puzzle in the book is a special case of this problem. Is the heuristic function you chose a good one for the 8-puzzle?

7. The state space of the 8-puzzle is made of two disjoint sets.  Describe how you would modify your program to prove this. (You do not have to implement this.)

8. Describe what heuristic you used for the A* search. Is the heuristic optimistic? Are there other heuristics you might use? (An excellent might compare a few different heuristics for effectiveness and make an argument about optimality.)

