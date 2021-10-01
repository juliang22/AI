from SensorlessProblem import SensorlessProblem
from Maze import Maze

from astar_search import astar_search

def sensorless_heuristic(state, goal=None):
	return len(state)


if __name__ == "__main__":
	# test_maze1 = Maze("maze1.maz")
	# test_mp1 = SensorlessProblem(test_maze1)
	# result = astar_search(test_mp1, sensorless_heuristic)
	# print(result)
	# test_mp1.animate_path(result.path)

	test_maze3 = Maze("maze3.maz")
	test_mp3 = SensorlessProblem(test_maze3)
	result = astar_search(test_mp3, sensorless_heuristic)
	print(result)
	test_mp3.animate_path(result.path)