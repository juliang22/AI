# CS76: AI - 21F - PA1 - Chickens & Foxes Report - Julian Grunauer 9/21/21

## Problem Statement
Three chickens and three foxes come to the bank of a river as shown in the figure above. They would like to cross to the other side of the river. However, there is one boat. The boat can carry up to two animals at one time, but doesn't row itself -- at least one animal must be in the boat for the boat to move. If at any time there are more foxes than chickens on either side of the river, then those chickens get eaten. 

## Algorithms
In this assignement, I implemented BFS, Path-Checking DFS, and Iterative DFS.

## Code Design
The problem is modeled by FoxProblem.py which checks which is a class that represents the state of the problem and has methods to get new states, check valid states, and check if the goal state has been reached. SearchSolution.py stores the solution for the problem and has methods for printing out the results. uninformed_search.py is where generic searching algorithms are written that are written such that they could be utilized for problems outside of this specific scenario. Finally, foxes.py is a file to test each of the algorithms. 

## Execution Instructions
* Download the code and run ```$ python3 foxes.py``` to run the foxes.py file. 
* This file contains example test code which runs BFS, Path-Checking DFS, and Iterative DFS. Comment out certain tests if you would like to test each algorithm independently.  