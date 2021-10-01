from SensorlessProblem import SensorlessProblem
from Maze import Maze

from astar_search import astar_search

def sensorless_heuristic(state, goal=None):
	return len(state)


if __name__ == "__main__":

	# Maze 1
	# test_maze1 = Maze("maze1.maz")
	# test_mp1 = SensorlessProblem(test_maze1)
	# result = astar_search(test_mp1, sensorless_heuristic)
	# print(result)
	# test_mp1.animate_path(result.path)

	# Maze 3
	# test_maze3 = Maze("maze3.maz")
	# test_mp3 = SensorlessProblem(test_maze3)
	# result = astar_search(test_mp3, sensorless_heuristic)
	# print(result)
	# test_mp3.animate_path(result.path)

	# Maze 5
	# test_maze5 = Maze("maze5.maz")
	# test_mp5 = SensorlessProblem(test_maze5)
	# result = astar_search(test_mp5, sensorless_heuristic)
	# print(result)
	# test_mp5.animate_path(result.path)

	# Maze 7
	test_maze7 = Maze("maze7.maz")
	test_mp7 = SensorlessProblem(test_maze7)
	result = astar_search(test_mp7, sensorless_heuristic)
	print(result)
	#test_mp7.animate_path(result.path)