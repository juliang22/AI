from MazeworldProblem import MazeworldProblem
from Maze import Maze

# from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

def heuristic(state, goals):
    mini = float('inf')
    for g in goals:
        mini = min(mini, (g[0] - state[0])**2 + (g[1] - state[1])**2)
    return mini

# Test problems
# test_maze3 = Maze("maze3.maz")
# test_mp = MazeworldProblem(test_maze3, [[1, 4], [1, 3], [1, 2]])
# result = astar_search(test_mp, heuristic)
# print(result)
# test_mp.animate_path(result.path)

# test_maze4 = Maze("maze4.maz")
# test_mp4 = MazeworldProblem(test_maze4, [[29, 0], [25,5]], [0,20])
# result = astar_search(test_mp4, heuristic)
# print(result)
# test_mp4.animate_path(result.path)

test_maze4 = Maze("maze2.maz")
test_mp4 = MazeworldProblem(test_maze4, [[2, 2]], [1,0])
result = astar_search(test_mp4, heuristic)
print(result)
test_mp4.animate_path(result.path)

#print(test_mp.start_state)
#print(test_mp.get_successors([4,5]))
#print(heuristic(test_mp.start_state, test_mp.goal_locations))


# # this should do a bit better:
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# Your additional tests here:
