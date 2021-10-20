# CS76: AI - 21F - PA4 - CSP Map/Circuitboard Solver - Julian Grunauer - 10/19/21

## Problem Statement
1. CSP problem - start with map coloring
Develop a framework that poses the map-coloring problem (as described in the book) as a CSP that the solver can solve.

As a reminder, the map-coloring problem involves several binary constraints. For each pair of adjacent countries, there is a binary constraint that prohibits those countries from having the same color.

2. Heuristics
Add the heuristics we have seen in class (MRV, degree heuristic, LCV). Make it easy to enable or disable each, since you will want to compare the effectiveness of your results, and since that will aid debugging.

3. Inference
Add an inference technique (AC-3). Make it easy to enable or disable inference, since you will need to test effectiveness.

4. Test on map coloring
You can test your solver with and without heuristics and inference on the map-coloring problem, and describe it in the writeup.

5. New problem: Circuit-board layout problem
Write code that describes and solves the circuit-board layout problem. Solve it for at least the example case I have suggested. You should not have to write any more backtracking code; you should be able to use the same implementation you used for map-coloring.

Details about the problem
You are given a rectangular circuit board of size n x m, and k rectangular components of arbitrary sizes.  Your job is to lay the components out in such a way that they do not overlap.  For example, maybe you are given these components:

      bbbbb   cc
aaa   bbbbb   cc  eeeeeee
aaa           cc
and are asked to lay them out on a 10x3 grid

..........
..........
..........
A solution might be

eeeeeee.cc
aaabbbbbcc
aaabbbbbcc

## Algorithms Implemented
* I implemented a backtracking CSP solver, 3 heuristics to speed up computation (MRV, LCV, and degree), as well as the AC3 inference algorithm.

## Execution Instructions
	* Download the code and run ```$ python3 map_csp.py``` to run the map solving algorithm and ```$ python3 circuitboard_csp.py``` to run the circuitboard algorithm. These files can be modified to test out each of the heuristics and the AC3 inference algorithm. Simply uncomment out the code block referencing these tests to try them out.