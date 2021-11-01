# CS76: AI - 21F - PA5 - Sudoku Solver - Julian Grunauer 10/31/21
import random
from collections import defaultdict

class SAT:
	def __init__(self, filename):
		# Initializes clauses to a list
		read = open(filename)
		self.rules = [line.split() for line in read]
		read.close()

	# Checks if the current clause is satisfied in the model
	def is_satisfied(self, model, line_rule):
		for rule in line_rule:
			neg = True if rule[0] == '-' else False
			if (neg and not model[int(rule[1:])]) or (not neg and model[int(rule)]):
				return True
		return False

	# Checks to see if every clause is satisfied by the model
	def is_solved(self, model):
		for line_rule in self.rules:
			if not self.is_satisfied(model, line_rule): 
				return False
		return True

	# Finds the best next variable to flip in either GSAT or WALKSAT algorithm
	def bestchoice(self, model, to_visit, visited=None):
		scores = defaultdict(lambda: 0)
		maxx = float('-inf')
		potentials = []
		for i in to_visit:
			model[i] = not model[i]

			# Calculates scores for each line
			for line_rule in self.rules: 
				if self.is_satisfied(model, line_rule):
					scores[i] += 1

			# Makes a list of variables that satisfy the most clauses if flipped
			if scores[i] > maxx:
				maxx = scores[i]
				potentials = [i]
			elif scores[i] == maxx:
				potentials.append(i)
			model[i] = not model[i]

		print('Current amount of clauses satisfied: ', maxx)

		# If GSAT, choose a random variable from the list of variables that satisfy the most clauses if flipped
		if not visited: return random.choice(potentials)

		# If WALKSAT, choose the variable that has been flipped the least out of the variables that satisfy the most amount of clauses when flipped
		else:
			minn = float('inf')
			chosen = None
			for pot in potentials:
				if visited[pot] < minn:
					minn = visited[pot]
					chosen = pot
			visited[chosen] += 1
			return chosen

	# Initializes the model with variables seen in list of clauses
	def eligible_clauses(self):
		model = {}
		for line_rule in self.rules:
			for rule in line_rule:
				var = rule[1:] if rule[0] == '-' else rule
				if model.get(var): continue
				else: model[int(var)] = random.choice([0,1]) == 0
		return model

	# Main function - runs either GSAT or WALKSAT algorithm
	def find_solution(self, max_iterations, threshold, sat_type):
		import time
		start_time = time.time()
		model = self.eligible_clauses()
		visited = defaultdict(lambda: 0) # Keeps track of how many times each variable has been flipped
		for flips in range(max_iterations):

			if self.is_solved(model):
				print(f'Total amount of flips: {flips}')
				print(f'Total amount of time: {round(time.time() - start_time, 2)} seconds')
				return model
			
			# Randomizes flips based off of a threshhold
			elif random.random() > threshold:
				switch = random.choice(list(model.keys()))
				model[switch] = not model[switch]

			# Flips the value chosen by bestchoice function using all variables
			if sat_type == 'GSAT':
				switch = self.bestchoice(model, model.keys())
				model[switch] = not model[switch]

			# Flips the value chosen by bestchoice function using variables in unsatisfied clauses
			else:
				# Picks a random clause that isn't satisfied by the model
				candidates = []
				for line_rule in self.rules:
					if not self.is_satisfied(model, line_rule):
						candidates.append([int(x) if x[0] != '-' else int(x[1:]) for x in line_rule])
				chosen = random.choice(candidates)

				switch = self.bestchoice(model, chosen, visited)
				model[switch] = not model[switch]

		# If solution is not found
		print(f'Solution not found in {max_iterations} flips')
		return False
	