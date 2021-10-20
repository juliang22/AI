# CS76: AI - 21F - PA4 - CSP Map/Circuitboard Solver - Julian Grunauer - 10/19/21

## Description
Using backtracking, heuristics, and inference techniques, I solved both the map coloring constrain-satisfaction problem and the 2D circuitboard layout problem. The algorithms work very well and run extremely fast. I decided to make a class for the CSP problem and instantiate it with variable names, variable domains, total of all possible domain, variable constraints, and a function to check constraints, abstracted outside the class so that it could change depending on the type of problem. Further, you can optionally pass in lcv, degree, and mrv heuristics as well as the AC3 inference algorithm. On initialization of the class, all variables, domains, and constraints are converted into integer values to speed up computation. 


## Evaluation
The algorithms run extremely fast and are implemented well. All aspects of each problem were solved and, to my knowledge, there are 0 bugs.  

No Heuristic Solution:
* Western Australia is Red
* Northern Territory is Green
* South Australia is Blue
* Queensland is Red
* New South Wales is Green
* Victoria is Red
* Tasmania is Green
* Explored [12] possible states

MRV Heuristic Solution:
* Western Australia is Red
* Northern Territory is Green
* South Australia is Blue
* Queensland is Red
* New South Wales is Green
* Victoria is Red
* Tasmania is Green
* Explored [12] possible states
* CSP was sped up by mrv_heuristic

Degree Heuristic Solution:
* South Australia is Red
* Northern Territory is Green
* Queensland is Blue
* New South Wales is Green
* Victoria is Blue
* Western Australia is Blue
* Tasmania is Red
* Explored [15] possible states
* CSP used the degree_heuristic

LCV Heuristic Solution:
* Western Australia is Blue
* Northern Territory is Green
* South Australia is Red
* Queensland is Blue
* New South Wales is Green
* Victoria is Blue
* Tasmania is Green
* Explored [7] possible states
* CSP used the lcv_heuristic

AC3 Inference Solution:
* Western Australia is Red
* Northern Territory is Green
* South Australia is Blue
* Queensland is Red
* New South Wales is Green
* Victoria is Red
* Tasmania is Green
* Explored [7] possible states
* CSP used the AC3 inference algorithm




## Discussion Questions

* (map coloring test) Describe the results from the test of your solver with and without heuristic, and with and without inference on the map coloring problem.
  * I manipulated the order of the variables to test out each heuristic. For example, if I initialize the values to ['Western Australia', 'Northern Territory', 'Queensland', 'South Australia' ...], the order selected will go 0, 1, 3. Queensland is skipped over because South Australia has less possible options for what it could be. For the degree heuristic, regardless of the order of the values, South Australia is selected because it is implicated in the most amount of constraints. The least constraining value simply selects the value for a given variable that allows for the most future choices. For example, in the order ['Western Australia', 'Northern Territory',  'Queensland', 'South Australia',...] , my algorithm first assigns Western Australia to blue, Northern Territory to green. Since Queensland has 2 valid domains left (blue or red), lcv selects blue as it allows for more potential options for Southern Australia (1 option) vs red which restricts Southern Australia to 0 options. With forward checking, AC3 is able to vastly speed up the algorithm by reducing the domain of other variables after a selection has been made. With my implementation, my backtracking algorithm is able to find the solution with only 7 recursions. Check the above results to compare the amount of times each algorithm recursed. 

* (circuit-board) In your write-up, describe the domain of a variable corresponding to a component of width w and height h, on a circuit board of width n and height m.  Make sure the component fits completely on the board.
	* I set the domain of each variable to an array of elements where each element was an array containing the top-left coordinates, top-right coordinates, and downward height. A component with w width and h height would have the first potential domain of [[(0, 0), (0,w-1), h]]. While w < n and the y coordinate + h < m, the domain is added to the list of possible domains for that component.

* (circuit-board) Consider components a and b above, on a 10x3 board.  In your write-up, write the constraint that enforces the fact that the two components may not overlap.  Write out legal pairs of locations explicitly.
    * With the implementation described above, A has the possible domains of "[[(0, 0), (2, 0), 2], [(1, 0), (3, 0), 2], [(2, 0), (4, 0), 2], [(3, 0), (5, 0), 2], [(4, 0), (6, 0), 2], [(5, 0), (7, 0), 2], [(6, 0), (8, 0), 2], [(7, 0), (9, 0), 2], [(0, 1), (2, 1), 2], [(1, 1), (3, 1), 2], [(2, 1), (4, 1), 2], [(3, 1), (5, 1), 2], [(4, 1), (6, 1), 2], [(5, 1), (7, 1), 2], [(6, 1), (8, 1), 2], [(7, 1), (9, 1), 2]]" and B has the possible domains of "A [[(0, 0), (2, 0), 2], [(1, 0), (3, 0), 2], [(2, 0), (4, 0), 2], [(3, 0), (5, 0), 2], [(4, 0), (6, 0), 2], [(5, 0), (7, 0), 2], [(6, 0), (8, 0), 2], [(7, 0), (9, 0), 2], [(0, 1), (2, 1), 2], [(1, 1), (3, 1), 2], [(2, 1), (4, 1), 2], [(3, 1), (5, 1), 2], [(4, 1), (6, 1), 2], [(5, 1), (7, 1), 2], [(6, 1), (8, 1), 2], [(7, 1), (9, 1), 2]]."
    * The constraint maintaining non-overlapping distinct components involves checking to see if the max of top-left x coordinates is less than the min of the top right x coordinates as well as checking if the max of one of the top y coordinates is less than the min of one of the bottom y coordinates. If both conditions are true, then the pieces are overlapping.
    * Valid combinations of A and B are as follows:
        * A - [[(0,0),(0,2), 2]], B - [[(0,3),(0,7), 2]]
        * A - [[(0,1),(0,3), 2]], B - [[(0,4),(0,8), 2]]
        * A - [[(0,2),(0,4), 2]], B - [[(0,5),(0,9), 2]]
        * A - [[(0,5),(0,7), 2]], B - [[(0,0),(0,4), 2]]
        * A - [[(0,6),(0,8), 2]], B - [[(0,1),(0,5), 2]]
        * A - [[(0,7),(0,9), 2]], B - [[(0,2),(0,6), 2]]
        * A - [[(1,0),(1,2), 2]], B - [[(1,3),(1,7), 2]]
        * A - [[(1,1),(1,3), 2]], B - [[(1,4),(1,8), 2]]
        * A - [[(1,2),(1,4), 2]], B - [[(1,5),(1,9), 2]]
        * A - [[(1,5),(1,7), 2]], B - [[(1,0),(1,4), 2]]
        * A - [[(1,6),(1,8), 2]], B - [[(1,1),(1,5), 2]]
        * A - [[(1,7),(1,9), 2]], B - [[(1,2),(1,6), 2]]


* (circuit-board) Describe how your code converts constraints, etc, to integer values for use by the generic CSP solver.
  * I initialize many variables to aid in the conversion process
    * self.v_list = list of variable names
    * self.total_domains = list of all possible domains for all variables
    * self.v_names = variables mapped to their index of variables names
    * self.d_names = Map of variable index to domain index
    * self.c_names = Map of variable name to constraint name
    * Map of variable index to constraint index
  * Then, after the algorithm finds a valid domain for every value, the to_str function simply prints out the mapping back to the variable's initial name/domain



