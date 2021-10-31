# CS76: AI - 21F - PA5 - Sudoku Solver - Julian Grunauer 10/11/21
import random
from collections import defaultdict

class SAT:
	def __init__(self, filename):
		read = open(filename)
		self.rules = [line.split() for line in read]
		read.close()

	def is_satisfied(self, model, line_rule):
		for rule in line_rule:
			neg = True if rule[0] == '-' else False
			if (neg and not model[int(rule[1:])]) or (not neg and model[int(rule)]):
				return True
		return False

	
	def is_solved(self, model):
		for line_rule in self.rules:
			if not self.is_satisfied(model, line_rule): 
				return False
		return True

	
	def bestchoice(self, model, to_visit, visited=None):
		scores = defaultdict(lambda: 0)
		maxx = float('-inf')
		potentials = []
		for i in to_visit:
			model[i] = not model[i]
			for line_rule in self.rules:
				if self.is_satisfied(model, line_rule):
					scores[i] += 1
			if scores[i] > maxx:
				maxx = scores[i]
				potentials = [i]
			elif scores[i] == maxx:
				potentials.append(i)
			model[i] = not model[i]
		print('m', maxx)
		if not visited: return random.choice(potentials)
		else:
			least_chosen = {}
			for pot in potentials:
				least_chosen[pot] = visited[pot]
			return min(least_chosen, key=least_chosen.get)

	def eligible_clauses(self):
		model = {}
		for line_rule in self.rules:
			for rule in line_rule:
				var = rule[1:] if rule[0] == '-' else rule
				if model.get(var): continue
				else: model[int(var)] = random.choice([0,1]) == 0
		return model

	def find_solution(self, max_iterations, threshold, sat_type):
		import time
		start_time = time.time()
		model = self.eligible_clauses()
		visited = defaultdict(lambda: 0)
		for flips in range(max_iterations):
			if self.is_solved(model):
				print(f'Total amount of flips: {flips}')
				print(f'Total amount of time: {round(time.time() - start_time, 2)} seconds')
				return model
			elif random.random() > threshold:
				switch = random.choice(list(model.keys()))
				model[switch] = not model[switch]

			if sat_type == 'GSAT':
				switch = self.bestchoice(model, model.keys())
				model[switch] = not model[switch]
			else:
				candidates = []
				for line_rule in self.rules:
					if not self.is_satisfied(model, line_rule):
						candidates.append([int(x) if x[0] != '-' else int(x[1:]) for x in line_rule])
				chosen = random.choice(candidates)
				switch = self.bestchoice(model, chosen, visited)
				visited[switch] += 1
				model[switch] = not model[switch]
		print(f'Solution not found in {max_iterations} flips')
		return False


	

	