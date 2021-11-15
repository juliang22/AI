from BrokenSensorProblem import BrokenSensorProblem
from Maze import Maze


def sensorless_heuristic(state, goal=None):
	return len(state)


if __name__ == "__main__":
	# Maze 1
	# test_maze1 = Maze("maze1.maz")
	# test_mp1 = BrokenSensorProblem(test_maze1)
	# test_mp1.filtering()

	# Maze 2
	# test_maze2 = Maze("maze2.maz")
	# test_mp2 = BrokenSensorProblem(test_maze2)
	# test_mp2.filtering()

	# Maze 3
	test_maze2 = Maze("maze3.maz")
	test_mp2 = BrokenSensorProblem(test_maze2)
	test_mp2.filtering()

