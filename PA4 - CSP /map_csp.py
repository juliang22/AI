from csp import CSP
from heuristics import lcv_heuristic, degree_heuristic, mrv_heuristic, AC3

def check_constraints(next_var, potential, constraints, d):
	for con in constraints[next_var]:
		if con not in potential: continue
		if potential[con] == potential[next_var]: return False
	return True

if __name__ == '__main__':
	v_names = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
	domain = {}
	total_domain = ['Red', 'Green', 'Blue']
	for v in v_names:
		domain[v] = ['Red', 'Green', 'Blue']
	constraints = {
		'Western Australia': ['Northern Territory', 'South Australia'],
		'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
		'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
		'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
		'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
		'Victoria': ['Tasmania', 'New South Wales', 'South Australia'],
		'Tasmania': ['Victoria']
	}

	call_count = [0]


	
	# Testing without heuristics or inference techniques
	# normal = CSP(v_names, domain, total_domain, constraints, check_constraints)
	# sol = normal.backtrack(call_count)
	# normal.to_str(sol, call_count)

	# Testing MRV Heuristic
	# mrv_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, mrv_heuristic)
	# sol = mrv_test.backtrack(call_count)
	# mrv_test.to_str(sol, call_count)

	# Testing Degree Heuristic
	# degree_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, degree_heuristic)
	# sol = degree_test.backtrack(call_count)
	# degree_test.to_str(sol, call_count)

	# Testing LCV Heuristic 
	# TODO: FIX 
	lcv_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, lcv_heuristic)
	sol = lcv_test.backtrack(call_count)
	lcv_test.to_str(sol, call_count)

	# Testing Inference
	# AC3_test = CSP(v_names, domain, total_domain, constraints, check_constraints, AC3)
	# sol = AC3_test.backtrack(call_count)
	# AC3_test.to_str(sol, call_count)
	
	