class CSP():
	def __init__(self, v_names, d_names, total_domains, c_names, constraint_checker, inference = None, heuristic = None,):
		self.inference = inference
		self.heuristic = heuristic
		self.c_check = constraint_checker

		self.v_list = v_names # list of variable names
		self.total_domains = total_domains # list of all possible domains

		self.v = [i for i in range(len(self.v_list))]
		self.v_names = {} # Map of variable name to index
		for i, v in enumerate(v_names):
			self.v_names[v] = i
		
		self.d_names = d_names # Map of variable name to domain name
		self.d = {} # Map of variable index to domain index
		for k, v in d_names.items():
			self.d[self.v_names[k]] = [self.total_domains.index(i) for i in v]

		self.c_names = c_names # Map of variable name to constraint name
		self.c = {} # Map of variable index to constraint index
		for k, v in c_names.items():
			self.c[self.v_names[k]] = [self.v_names[i] for i in v]

	
	def to_str(self, mapped,call_count):
		if not mapped: 
			print("Solution could not be found :(")
			exit()
		print('Solution:')
		for val, dom in mapped.items():
			print(f'{self.v_list[val]} is {self.total_domains[dom]}')
		print(f'Explored {call_count} possible states')



	def backtrack(self, call_count, potential = {}):
		# Goal check if we've reached the end 
		if len(potential) == len(self.v_list): return potential
		
		# List of variables that have yet to be assigned
		leftover_vars = [v for v in self.v if v not in potential]
		if self.heuristic and self.heuristic.__name__ != 'lcv_heuristic':
			next_var = self.heuristic(leftover_vars, potential, self.c, self.d, self.total_domains)
		else:
			next_var = leftover_vars[0]

		for val in self.d[next_var]:
			call_count[0] += 1

			if self.heuristic and self.heuristic.__name__ == 'lcv_heuristic':
				potential[next_var] = self.heuristic(next_var, leftover_vars, potential, self.c, self.d)
			else:
				potential[next_var] = val

			if self.c_check(next_var, potential, self.c, self.total_domains): 
				# If inference function is available
				if self.inference:
					pre_inference_dom = self.d.copy()
					self.d[next_var] = [val]
					if not self.inference(self.d, self.c): 
						self.d = pre_inference_dom
						continue

				res = self.backtrack(call_count) 
				if res is not None: return res

				if self.inference: self.d = pre_inference_dom 
			
			potential.pop(next_var)

		return None

	

			

