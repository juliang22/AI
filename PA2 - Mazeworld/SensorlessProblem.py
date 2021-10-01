from Maze import Maze
from astar_search import AstarNode 
from time import sleep

class SensorlessProblem:

    # Initializes variables
    def __init__(self, maze):
        self.maze = maze
        self.start_state = self.create_locations()
        self.goal_locations = None #remnant from mazeworld

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    # Find new location that is valid
    def new_loc(self, x, y, prev_x, prev_y):
        if x < 0: x = 0
        if y < 0: y = 0
        if x >= self.maze.width: x = self.maze.width - 1
        if y >= self.maze.height: y = self.maze.height - 1
        if self.maze.lines[y][x] == '#': return (prev_x, prev_y)
        return (x,y)

    # Creates initial locations (all states that are valid for the robot to be in)
    def create_locations(self):
        locations = set()
        for y, line in enumerate(self.maze.lines):
            for x, char in enumerate(line):
                if self.test_valid(x, y): 
                    locations.add((x, y))
        return locations
    
    # Tests if the proposed state is a valid move or not
    def test_valid(self, x, y):
        if x >= 0 and y >= 0 and x < self.maze.width and y < self.maze.height and self.maze.lines[y][x] == '.':
            return True
        return False
    
    # Gets successors for the current state
    def get_successors(self, locations):
        successors = []
        for i, direc in enumerate([(0, 1), (0, -1), (-1, 0), (1,0)]): # up, down, left, right
            potential = set()
            for loc in locations:
                x, y = loc[0], loc[1]
                try_x, try_y = x + direc[0], y + direc[1]
                potential.add(self.new_loc(try_x, try_y, x, y))
            successors.append(potential)
        return successors

    # If state is equal to 1, the robot has been located
    def goal_test(self, state):
        if len(state) == 1: return True
        return False

    # Animate path once node is found
    def animate_path(self, path):
        for p in path:
            for y, line in enumerate(self.maze.lines):
                for x, char in enumerate(line):
                    if (x,y) in p: 
                        line = line[:x] + "A" + line[x + 1:]
                print(line)
            sleep(.3)
            print("\n")

