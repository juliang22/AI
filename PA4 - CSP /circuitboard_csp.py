# CS76: AI - 21F - PA4 - CSP Map/Circuitboard Solver - Julian Grunauer - 10/19/21
from csp import CSP
from collections import defaultdict
from heuristics import lcv_heuristic, degree_heuristic, mrv_heuristic, AC3

# Function to check if domain is a valid choice
def check_constraints(next_var, potential, constraints, d):
	for con in constraints[next_var]:
		if con not in potential: continue
		# Initializing 4 corners of potential variable domain and that variables neighbors domain
		con_tl, new_tl  = d[potential[con]][0], d[potential[next_var]][0]
		con_tr, new_tr = d[potential[con]][1], d[potential[next_var]][1]
		con_h, new_h = d[potential[con]][2]-1, d[potential[next_var]][2]-1

		con_bl, new_bl = (d[potential[con]][0][0], d[potential[con]][0][1]+con_h), (d[potential[next_var]][0][0], d[potential[next_var]][0][1]+new_h)
		con_br, new_br = (d[potential[con]][1][0], d[potential[con]][1][1]+con_h), (d[potential[next_var]][1][0], d[potential[next_var]][1][1]+new_h)

		# Checks to see if any of the values are the same or intersect on a 2D grid
		if (len({con_tl, con_tr, con_bl, con_br} - {new_tl, new_tr, new_bl, new_br}) < 4): return False
		upper = [max(con_tl[0], new_tl[0]), min(con_tr[0], new_tr[0])]
		lower = [max(con_tl[1], new_tl[1]), min(con_br[1], new_br[1])]
		if upper[0] <= upper[1] and lower[0] <= lower[1]: return False 

	return True

# Problem set up
if __name__ == '__main__':
	v_names = ['A', 'B', 'C', 'E']
	sizes = {
		'A': (3, 2),
		'B': (5, 2),
		'C': (2, 3),
		'E': (7, 1)
	}
	board_size = (10, 3)

	domain = defaultdict(lambda: [])
	for k, v in sizes.items():
		for j in range(board_size[1]):
			s = 0
			e = v[0]-1
			h = v[1]	
			for i in range(board_size[0]):
				if s >= 0 and e < board_size[0] and j + h <= board_size[1]:
					domain[k].append([(i,j), (e, j),h])
				s += 1
				e += 1

	total_domain = [pair for v in domain.values() for pair in v]
	constraints = {x: list(set(domain) - set(x)) for x in v_names}


	call_count = [0] # Variable to track amount of time the recursive backtracking function is called

	# Testing without heuristics or inference techniques 
	normal = CSP(v_names, domain, total_domain, constraints, check_constraints)
	sol = normal.backtrack(call_count)
	normal.to_str(sol, call_count)
	
	# Testing MRV Heuristic
	# TODO: Not fully functioning
	# mrv_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, mrv_heuristic)
	# sol = mrv_test.backtrack(call_count)
	# mrv_test.to_str(sol, call_count)

	# Testing Degree Heuristic
	# degree_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, degree_heuristic)
	# sol = degree_test.backtrack(call_count)
	# degree_test.to_str(sol, call_count)

	# Testing LCV Heuristic 
	# TODO: Not fully functioning
	# lcv_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, lcv_heuristic)
	# sol = lcv_test.backtrack(call_count)
	# lcv_test.to_str(sol, call_count)


	# Testing Inference
	# AC3_test = CSP(v_names, domain, total_domain, constraints, check_constraints, AC3)
	# sol = AC3_test.backtrack(call_count)
	# AC3_test.to_str(sol, call_count)


	print("Grid starts from top-left corner and array represents coordinates in the form 'top-left', 'top-right', 'downward height'")


