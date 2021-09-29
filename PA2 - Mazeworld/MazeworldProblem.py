from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs
    def __init__(self, maze, goal_locations, start_state=None):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = start_state or self.find_valid_start()

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    def test_valid(self, x, y):
        if x >= 0 and y >= 0 and x < self.maze.width and y < self.maze.height and not self.maze.has_robot(x,y) and self.maze.lines[y][x] == '.':
            return True
        return False

    def find_valid_start(self):
        for y, line in enumerate(self.maze.lines):
            for x, char in enumerate(line):
                #print(char, maze.has_robot(col, row), col, row)
                if self.test_valid(x, y): 
                    return [x, y]
   
    def get_successors(self, state):
        x, y = state[0], state[1]
        successors = []
        for direc in [(0, 1), (0, -1), (-1, 0), (1,0)]: # up, down, left, right
            try_x, try_y = x + direc[0], y + direc[1]
            if self.test_valid(try_x, try_y): successors.append([try_x, try_y])
        return successors

    # given a sequence of states (including robot turn), modify the maze and print it out. (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)
        
        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(.2)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
