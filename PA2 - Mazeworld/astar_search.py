from SearchSolution import SearchSolution
from heapq import heappush, heappop
from collections import defaultdict

class AstarNode:
    def __init__(self, state, heuristic, parent=None, path_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.path_cost = path_cost
        self.A_score = self.path_cost + self.heuristic

    # comparison operator, needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.A_score < other.A_score

# Tracks the end state back to the start state to find the optimal path
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    return result

# General A* algorithm to work with multiple types of problems
def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state, search_problem.goal_locations))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {} # Keep track of visited states to optimize algorithm if the same state is reached twice
    while pqueue: 
        curr = heappop(pqueue)
        solution.nodes_visited += 1
        visited_cost[tuple(curr.state)] = curr.A_score 

        # If goal has been reached, return solution
        if search_problem.goal_test(curr.state): 
            solution.path = backchain(curr)
            solution.cost = curr.path_cost
            return solution

        # Find successors to current state and add new valid nodes to the frontier
        successors = search_problem.get_successors(curr.state) 
        for succ in successors:
            new_node = AstarNode(succ, heuristic_fn(succ, search_problem.goal_locations), curr, curr.path_cost+1)
            succ = tuple(succ)
            if succ in visited_cost.keys():
                if new_node.A_score < visited_cost[succ]:
                    visited_cost[succ] = new_node.A_score
                    heappush(pqueue, new_node)
            else:
                visited_cost[succ] = new_node.A_score
                heappush(pqueue, new_node)
    
    return solution