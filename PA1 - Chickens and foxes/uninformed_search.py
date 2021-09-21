
from collections import deque
from SearchSolution import SearchSolution


class SearchNode:
    # each search node except the root has a parent node and all search nodes wrap a state object
    def __init__(self, state, parent=[], visited=False):
        self.state = state
        self.parent = parent
        self.depth = 0

# you might write other helper functions, too. For example, I like to separate out backchaining, and the dfs path checking functions
def backtrack(goal_state):
    path = [goal_state.state]
    curr = goal_state
    while curr.parent:
        path.append(curr.parent.state)
        curr = curr.parent
    return path


def bfs_search(search_problem):
    root = SearchNode(search_problem.start_state)
    to_visit = deque([root])
    visited = set()
    while to_visit:
        curr = to_visit.popleft()
        visited.add(curr.state)
        # updates to_visit and checks if returned state is goal_state
        successors = search_problem.get_successors(curr)
        for potential in successors:
            if potential.state not in visited:
                if search_problem.check_goal(potential.state):
                    visited.add(potential.state)
                    return SearchSolution(search_problem, "BFS", backtrack(potential)[::-1], len(visited))
                to_visit.append(potential)
    return SearchSolution(search_problem, "BFS", [], len(visited))

# Don't forget that your dfs function should be recursive and do path checking, rather than memoizing (no visited set!) to be memory efficient
# We pass the solution along to each new recursive call to dfs_search so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, node=None, solution=None,  depth_limit=100):
    # if no node objects given, create a new search from starting start, else 
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    else:
        solution.num_nodes += 1

    # for IDFS: limits the depth
    if solution.num_nodes >= depth_limit:
        return
    # Base case: checks if we are at the ending state and returns solution if it is
    if search_problem.check_goal(node.state):
        node.parent.append(node.state)
        solution.path = node.parent
        solution.num_nodes += 1
        return solution

    # Gets successors loops through them performing a search on each first item
    successors = search_problem.get_successors(node)
    for potential in successors:
        # keeps track of the path from current node to starting state
        potential.parent = node.parent.copy()
        potential.parent.append(node.state)
        #if there aren't any cycles (repeat states), then keep searching
        if potential.state not in node.parent:
            done = dfs_search(search_problem, potential, solution)
            if done: return done
    # return that the solution couldn't be found if we get to the point where the node no longer has a parent (therefore is start state)
    if len(node.parent) == 0: return SearchSolution(search_problem, "DFS", [], solution.num_nodes+1)


def ids_search(search_problem, depth_limit=100):
    for i in range(depth_limit):
        done = dfs_search(search_problem, None, None, i)
        if done: 
            done.search_method ="IDS"
            return done
    return SearchSolution(search_problem, "IDS")
