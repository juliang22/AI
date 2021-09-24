# Julian Grunauer 9/21/21
from collections import deque
from uninformed_search import SearchNode


class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.tot_chic = start_state[0]
        self.tot_fox = start_state[1]

    # Checks if the potential move is valid
    def check_valid(self, C, F):
        if C > self.tot_chic or C < 0 or F > self.tot_fox or F < 0:
            return False
        if (C >= 1 and F > C) or (self.tot_chic - C >= 1 and (self.tot_fox - F) > (self.tot_chic - C)):
            return False
        return True
    
    # Checks if the goal state has been found
    def check_goal(self, curr):
        if curr[0] == 0 and curr[1] == 0 and curr[2] == 0: return True
        return False

    # Returns valid successors to the search algorithm
    def get_successors(self, curr):
        C, F, B = curr.state[0], curr.state[1], curr.state[2]
        successors = []
        # iterates through possible move state
        for el in [(2, 0), (0, 2), (1, 0), (0, 1), (1, 1)]:
            try_c = C - el[0] if B == 1 else C + el[0]
            try_f = F - el[1] if B == 1 else F + el[1]
            # Check if new state is valid and adds to further searches
            if self.check_valid(try_c, try_f):
                successors.append(SearchNode((try_c, try_f, 0 if B==1 else 1), curr, curr.depth+1))
        return successors

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string

# A bit of test code
if __name__ == "__main__":
    test_cp = FoxProblem((3, 3, 1))
    visit = deque()
    print(test_cp.get_successors((3, 3, 1), visit))
    for el in visit:
        print(el.state)
    print(test_cp)
