from collections import deque
from uninformed_search import SearchNode


class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.tot_chic = start_state[0]
        self.tot_fox = start_state[1]
        # you might want to add other things to the problem, like the total number of chickens (which you can figure out based on start_state

    def check_valid(self, C, F):
        if C > self.tot_chic or C < 0 or F > self.tot_fox or F < 0:
            return False
        if (C >= 1 and F > C) or (self.tot_chic - C >= 1 and self.tot_fox - F > self.tot_chic - C):
            return False
        return True
    
    def check_goal(self, curr):
        if curr[0] == 0 and curr[1] == 0 and curr[2] == 0: return True
        return False

    # get successor states for the given state
    # you write this part. I also had a helper function that tested if states were safe before adding to successor list
    # I also had a goal test method. You should write one.
    def get_successors(self, curr):
        C, F, B = curr.state[0], curr.state[1], curr.state[2]
        successors = []
        for el in [(0, 2), (0, 1), (1, 1), (2, 0), (1, 0)]:
            try_c = C - el[0] if B == 1 else C + el[0]
            try_f = F - el[1] if B == 1 else F + el[1]

            # Check if new state is valid and add to further searches
            if self.check_valid(try_c, try_f):
                successors.append(SearchNode((try_c, try_f, 0 if B==1 else 1), curr))
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
