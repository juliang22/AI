
# Julian Grunauer 9/21/21
from collections import deque
from SearchSolution import SearchSolution

class SearchNode:
    # each search node except the root has a parent node and all search nodes wrap a state object
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

# Backtracking algorithms to make the path for bfs algorithm
def backtrack(goal_state):
    path = [goal_state.state]
    curr = goal_state
    while curr.parent:
        path.append(curr.parent.state)
        curr = curr.parent
    return path[::-1]

def check_cycle(curr):
    higher_node = curr.parent
    while higher_node:
        if higher_node and curr.state == higher_node.state: 
            return False
        higher_node = higher_node.parent
    return True

# Bfs searching algorithm which searches for the goal state level by level
def bfs_search(search_problem):
    root = SearchNode(search_problem.start_state)
    to_visit = deque([root])
    visited = set()
    # Iterates through frontier while there is still nodes to explore and goal state hasn't been reached
    while to_visit:
        curr = to_visit.popleft()
        visited.add(curr.state)
        # Finds valid successor states
        successors = search_problem.get_successors(curr)
        # Check if goal state has been reached
        if search_problem.check_goal(curr.state):
            visited.add(curr.state)
            return SearchSolution(search_problem, "BFS", backtrack(curr), len(visited))
        for potential in successors:
            if potential.state not in visited:
                # Appends node to frontier 
                to_visit.append(potential)
    # Returns empty path if goal state is not found
    return SearchSolution(search_problem, "BFS", [], len(visited))

# DFS search algorithm that explores each path by depth
def dfs_search(search_problem, node=None, solution=None, depth_limit=100):
    # if no node objects given, create a new search from starting start, else 
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS", [], 1)
    else:
        solution.num_nodes += 1

    # Base case: checks if we are at the ending state and returns solution if it is
    if search_problem.check_goal(node.state):
        solution.path = backtrack(node)
        return solution

    # Gets successors then loop through them performing a search on each first item (IDS: limits the depth)
    successors = search_problem.get_successors(node) if node.depth < depth_limit else []
    for potential in successors:
        if check_cycle(potential): # If there aren't any cycles (repeat states), then keep searching
            # If done is not None, then base case has been hit and we can return up the stack
            done = dfs_search(search_problem, potential, solution, depth_limit)
            if done: return done
    # Returns empty path if goal state is not 
    if not node.parent: 
        return SearchSolution(search_problem, "DFS", [], solution.num_nodes)

# IDS search algorithm which runs DFS multiple times at different maximum levels 
def ids_search(search_problem, depth_limit=100):
    # Loops up to depth_limit until goal state is found
    solution = SearchSolution(search_problem, "IDS", [], 1)
    for i in range(depth_limit):
        dfs_search(search_problem, SearchNode(search_problem.start_state), solution, i)
        # Return solution if solution is found and path is not empty
        if solution.path: 
            break
    # Returns empty path if goal state is not found
    return solution

# EXTRA CREDIT: Memoized DFS: uses a set to track visited states instead of pathchecking
def dfs_memoized(search_problem):
    root = SearchNode(search_problem.start_state)
    to_visit = [root]
    visited = set()
    # Iterates through frontier while there is still nodes to explore and goal state hasn't been reached
    while to_visit:
        curr = to_visit.pop()
        visited.add(curr.state)
        # Finds valid successor states
        successors = search_problem.get_successors(curr)
        for potential in successors:
            if potential.state not in visited:
                # Check if goal state has been reached
                if search_problem.check_goal(potential.state):
                    visited.add(potential.state)
                    return SearchSolution(search_problem, "Memoized DFS", backtrack(potential), len(visited))
                # Appends node to frontier 
                to_visit.append(potential)
    # Returns empty path if goal state is not found
    return SearchSolution(search_problem, "Memoized DFS", [], len(visited))