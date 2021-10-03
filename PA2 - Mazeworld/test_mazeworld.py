from MazeworldProblem import MazeworldProblem
from Maze import Maze

from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state, goals):
    return 0

# Finds the min amount of steps to the robot's goal (not including walls)
def manhattan_heuristic(state, goals):
    x_i, y_i = state[0] * 2 + 1, state[0] * 2 + 2
    g_x, g_y = goals[state[0] * 2], goals[state[0] * 2 + 1]
    return abs(g_x - state[x_i]) + (g_y - state[y_i])


    



# Test problems
if __name__ == "__main__":
    # Maze 1 
    # test_maze1 = Maze("maze1.maz")
    # test_mp = MazeworldProblem(test_maze1, (2, 2))
    # result = astar_search(test_mp, manhattan_heuristic)
    # print(result)
    # test_mp.animate_path(result.path)

    # Maze 2
    # test_maze2 = Maze("maze2.maz")
    # test_mp = MazeworldProblem(test_maze2, (2,2))
    # result = astar_search(test_mp, manhattan_heuristic)
    # print(result)
    # test_mp.animate_path(result.path)

    # Maze 3
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    result = astar_search(test_mp, manhattan_heuristic)
    print(result)
    result2 = astar_search(test_mp, null_heuristic)
    print(result2)
    #test_mp.animate_path(result.path)

    # Maze 4
    # test_maze4 = Maze("maze4.maz")
    # test_mp4 = MazeworldProblem(test_maze4, (10, 0, 11, 0, 0, 5))
    # result = astar_search(test_mp4, manhattan_heuristic)
    # print(result)
    # test_mp4.animate_path(result.path)

    # Maze 5
    # test_maze5 = Maze("maze5.maz")
    # test_mp5 = MazeworldProblem(test_maze5, (1, 4, 2, 4))
    # result = astar_search(test_mp5, manhattan_heuristic)
    # print(result)
    # test_mp5.animate_path(result.path) 

    # Maze 6
    # test_maze4 = Maze("maze6.maz")
    # test_mp4 = MazeworldProblem(test_maze4, (6, 1, 6,0, 6,2))
    # result = astar_search(test_mp4, euclidean_heuristic)
    # print(result)
    # test_mp4.animate_path(result.path)

    # Maze 7: Corridor
    # test_maze7 = Maze("maze7.maz")
    # test_mp7 = MazeworldProblem(test_maze7, (30, 2, 2, 2))
    # result = astar_search(test_mp7, manhattan_heuristic)
    # print(result)
    # test_mp7.animate_path(result.path) 
