# PA2 - Markov Model
### Julian Grunauer - 11/8/21 - CS76: Artificial Intelligence

## Description
I began by using the code that I had written for PA2: Mazeworld. I mainly used Maze.py, as the rest of the files were specific to PA2. I then created example mazes, but instead of representing spaces with '.', I used the elements {r,g,b,y} to represent the colors of the tiles. I then wrote a move function (which randomly selects horizontal/vertical movement) and a sensor function which finds the correct color of the floor 88% of the time and finds each of the remaining colors 4% of the time (as stated in the problem description). 

For this problem, the state space was a list of probabilities corresponding to each location of the maze. The state space is initialized with a uniform distribution of probabilities. Before each move, I update the state by multiplying each space that the robot could hypothetically move to by 0.25 (as the robot is equally likely to move in any direction, from any space). If the robot cannot move to the space, then the space the robot is in is multiplied by 0.25 (as the robot will remain in teh same square). The robot then moves randomly. After the robot's movement, the model is updated by multiplying each space that corresponds with the robot's sensor reading by 0.88 and each space that does not by 0.04. I then print out where the robot is along with the probability distribution. The robot continues to update its transition model, move, and update the probabilities based off of the sensor reading until the highest prediction in the model corresponds with the robot's actual location.

## Evaluation
The algorithm works exactly as it should. Averaging over 10 runs maze 1, 2, and 3 have the following results:
1: 12 moves with a probability of 46% certain that the robot is in the square
2: 26 moves with a probability of 20% certain that the robot is in the square
3: 3 moves with a probability of 30% certain that the robot is in the square

It is important to note that though the final probability seems low, in comparison to the probabilities of the rest of the squares, it is quite high. Also, when the robot is on a square of a certain color, the rest of the probabilities of squares of that color are much higher than the other squares and this tends to increase as the function continues to run.  