# PA2 - Mazeworld 
### Julian Grunauer - 9/30/21 - CS76: Artificial Intelligence

## How to run code
* Run ```$python3 test_mazeworld.py``` to see the A* algorithm in a printed GUI (works for both single or multi-robot systems)
* Run ```$python3 test_sensorless.py``` to see the A* algorithm in a printed GUI to finding the state of a blind robot in the fewest possible moves.

* Both test_mazeworld.py and test_sensorless.py can be modified to run on different mazes/stateconfigurations. Change the maze by modifying the parameter for the test_maze# variable and pass in new goal locations to the test_mp variable (test_sensorless.py does not need goal locations, so only modify the test_maze#). You can comment out different mazes to see each maze run independently.

## Problem Description
Here is a maze, drawn in the venerable tradition of ASCII art:

.......
.##....
..##...
.......
..##...
#.###..
....##.
The periods represent open floor tiles (places that can be walked on or over), and the number signs represents walls, places in the maze where a simple robot cannot go.

You have a robot. It can move in any of four directions: North (towards the top of the screen), East, South, and West. There are coordinates on the maze. (0, 0) is the bottom left corner of the maze. (6, 0) is the bottom right corner of the maze.

In this particular example, perhaps we'd like to plan a path for the robot to go through the maze from the bottom left corner to the bottom right corner, without going through any walls.

### 1. Implement A-star search
* Implement A* search in astar_search.py. 

### 2. Solve the Multi-robot coordination problem
* k robots live in an n x n rectangular maze. The coordinates of each robot are (x_i, y_i), and each coordinate is an integer in the range 0...n-1. For example, maybe the maze looks like this:

. B . . . . .
. # # . C . .
. . # # . . .
. . . . # . .
. . # # . . .
. . # . . . .
A . . . # # .
* That's three robots A, B, C in a 7x7 maze. You'd like to get the robots to another configuration. For example:

. . . . . . .
. # # . . . .
. . # # . . .
. . . . # . .
. . # # . . B
. . # . . . A
. . . . # # C
* There are some rules. The robots only move in four directions, north, south, east, and west. The robots cannot pass through each other, and may not occupy the same square. The robots move one at a time. First robot A moves, then robot B, then robot C, then D, E, and eventually, A gets another turn. Any robot may decide to give up its turn and not move. So there are five possible actions from any state.

* Let's make the cost function the total fuel expended by the robots. A robot expends one unit of fuel if it moves, and no fuel if it waits a turn.

* Only one robot may occupy one square at a time. You are given a map ahead of time, and it will not change during the course of the game.

### 3. Solve the Blind robot problem with Pacman physics
* Assume that you now only have a single robot in mazeworld, but there's a catch. The robot is blind, and doesn't know where it starts! The robot does know the map of the maze.

* The robot has a sensor that can tell it what direction is North (so that it can still move in intended directions). However, the robot has no other sensors.  No, it really can't tell when it hits a wall.

* If you execute the action "west" from a configuration where "west" is blocked, the robot simply doesn't move.

