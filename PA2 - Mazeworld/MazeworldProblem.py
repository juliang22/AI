from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs
    def __init__(self, maze, goal_locations):
        self.maze = maze

        robots = list(maze.robotloc)
        self.num_robs = len(robots)//2
        if len(robots) == 0: self.start_state = self.find_valid_start()
        else:
            robots.insert(0, 0)
            self.start_state = tuple(robots)

        self.goal_locations = set()
        for goal in goal_locations:
            self.goal_locations.add(goal)

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    def test_valid(self, x, y, x_i=None, y_i=None, state=None):
        # If there are robots in the maze
        if state:
            for i in range(1, len(state), 2):
                if x == state[i] and y == state[i+1] and x_i != i and y_i != i: 
                    return False

        if x >= 0 and y >= 0 and x < self.maze.width and y < self.maze.height and self.maze.lines[y][x] == '.':
            return True
        return False

    def find_valid_start(self):
        for y, line in enumerate(self.maze.lines):
            for x, char in enumerate(line):
                if self.test_valid(x, y): 
                    return (0, x, y)


    def make_next_state(self, state, try_x=None, try_y=None, x_i=None, y_i=None):
        next_state = []

        for i, el in enumerate(state):
            if i == 0:
                # If last robot in list, go back to robot 0, else go to next robot's turn 
                next_state.append(0 if state[0]+1 >= self.num_robs else state[0] + 1)
                continue
            if i == x_i: next_state.append(try_x)
            elif i == y_i: next_state.append(try_y)
            else: next_state.append(el)
        return tuple(next_state)

   
    def get_successors(self, state):
        successors = []
        curr_rob = state[0]
        x_i, y_i = curr_rob * 2 + 1, curr_rob * 2 + 2
        x, y = state[x_i], state[y_i]

        for direc in [(0, 1), (0, -1), (-1, 0), (1, 0)]: # up, down, left, right
            try_x, try_y = x + direc[0], y + direc[1]
            if self.test_valid(try_x, try_y, x_i, y_i, state): 
                new_state = self.make_next_state(state, try_x, try_y, x_i, y_i)
                successors.append(new_state)

        if not successors: 
            new_state = self.make_next_state(state)
            successors.append(new_state)

        return successors

    def goal_test(self, state):
        robs = []
        for i in range(1, len(state), 2):
            robs.append(tuple([state[i], state[i+1]]))
        return all(rob in self.goal_locations for rob in robs)
        

    # given a sequence of states (including robot turn), modify the maze and print it out. (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)
        
        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(.2)

            print(str(self.maze))


# Me tryiung to make it work
    # def animate_path(self, path):
    #     print(self.maze.lines)
    #     for p in path:
    #         for y, line in enumerate(reversed(self.maze.lines)):
    #             for x, char in enumerate(line):
    #                 if x == p[1] and y== p[2]: 
    #                     line = line[:x] + self.maze.robotchar(p[0]) + line[x + 1:]
    #             print(line)
    #         sleep(.3)
    #         print("\n")

