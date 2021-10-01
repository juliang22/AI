from SearchSolution import SearchSolution
from heapq import heappush, heappop
from collections import defaultdict

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, path_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.path_cost = path_cost
        self.A_score = self.path_cost + self.heuristic
        self.found_goal = False

    # comparison operator, needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.A_score < other.A_score


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    return result

def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state, search_problem.goal_locations))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    while pqueue:
        curr = heappop(pqueue)
        solution.nodes_visited += 1
        visited_cost[tuple(curr.state)] = curr.A_score 

        if search_problem.goal_test(curr.state): #TODO: Have to pass in None for some reason for sensoreless, fix l8r
            solution.path = backchain(curr)
            solution.cost = curr.path_cost
            return solution

        successors = search_problem.get_successors(curr.state)
        #print(curr.state, successors)
        for succ in successors:
            new_node = AstarNode(succ, heuristic_fn(succ, search_problem.goal_locations), curr, curr.path_cost+1)
            succ = tuple(succ)
            if succ in visited_cost.keys():
                if new_node.A_score < visited_cost[succ]:
                    visited_cost[succ] = new_node.A_score
                    heappush(pqueue, new_node)
            else:
                heappush(pqueue, new_node)
    
    return solution

