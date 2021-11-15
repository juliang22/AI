from Maze import Maze
from time import sleep
import random

class BrokenSensorProblem:

    # Initializes variables
    def __init__(self, maze):
        self.maze = maze
        self.size = maze.width*maze.height
        self.probs = [[1/self.size] * self.maze.width for i in range(self.maze.height)]
        self.res = None

        #self.update_model()
        self.animate_path(self.maze.robotloc)

    def __str__(self):
        string =  "Broken sensor robot problem: "
        return string

    def get_color(self):
        true_color = self.maze.lines[self.maze.robotloc[0]][self.maze.robotloc[1]]
        selected_color = true_color if random.random() < .88 else random.choice(['r','g','b','y'])
        truth = True if selected_color == true_color else False
        print(f'Selected color {selected_color} {"is" if truth else "is not"} correct.')
        return selected_color
    

    # Animate path once node is found
    def animate_path(self, move):
        for y, line in enumerate(self.maze.lines):
            if y == 0: print('Colors:                           Probs: ')
            p_line = ""
            for x, char in enumerate(line):
                if [y,x] != move: 
                    p_line += f"{'{0:>5}'.format(round(self.probs[x][y]*100,2))}% "

                if [y,x] == move: 
                    line = line[:x] + line[x].upper() + line[x + 1:]
                    p_line += f"{'~{0:>5}'.format(round(self.probs[x][y]*100,2))}%~ "

            print(line, '                       ', p_line)
        sleep(.3)

    
    def update_model(self):
        color = self.get_color()
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                color_at_loc = self.maze.lines[y][x]
                self.probs[x][y] *= 0.88 if color == color_at_loc else 0.04
        
        # normalize each probability
        summ = sum(sum(self.probs,[]))
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                self.probs[y][x] /= summ
              
        
    def transition(self):
        transition = [[0] * self.maze.width for i in range(self.maze.height)]
        for y in range(self.maze.height):   
            for x in range(self.maze.width):
                for try_x, try_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = try_x + x, try_y + y
                    curr = self.probs[y][x] * .25
                    if self.maze.test_valid(new_x, new_y):
                        transition[new_y][new_x] += curr
                    else:
                        transition[y][x] += curr
        self.probs = transition
    

    def found(self):
        maxx = float('-inf')
        highest_prob = None
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.probs[y][x] > maxx:
                    maxx = self.probs[y][x]
                    highest_prob = [y,x]

        if highest_prob == self.maze.robotloc:
            self.res = self.maze.robotloc
            print(f'Maze found robot location with probability of: {round(maxx*100,2)}%')
            return True

        return False

    
    def filtering(self):
        num_moves = 0
        while not self.found():
            print(num_moves, '\n')
            num_moves += 1
            self.transition()
            move = self.maze.move()
            self.update_model()
            self.animate_path(move)

        return self.res

