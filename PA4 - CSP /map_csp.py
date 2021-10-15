from csp import CSP


def check_constraints(next_var, potential, constraints):
	for con in constraints[next_var]:
		if con not in potential: continue
		if potential[con] == potential[next_var]: return False
	return True


def degree_heuristic(leftover_vars, potential, constraints, domain):
	maxx = float('-inf')
	res = leftover_vars[0]
	for var in leftover_vars:
		con = constraints[var]
		if len(con) > maxx:
			maxx = max(maxx, len(con))
			res = var
	return res


def mrv_heuristic(leftover_vars, potential, constraints, domain):
	res = leftover_vars[0]
	minn = float('inf')
	res = leftover_vars[0]
	for var in leftover_vars:
		dom = {x for x in domain[var]}
		for con in constraints[var]:
			if potential.get(con, None) in dom:
				dom.discard(potential[con])
		if len(dom) < minn:
			minn = min(minn, len(dom))
			res = var
	print(res)
	return res
		


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

	mappy = CSP(v_names, domain, total_domain, constraints, check_constraints)
	call_count = [0]
	# sol = mappy.backtrack(call_count, mrv_heuristic)
	sol = mappy.backtrack(call_count, degree_heuristic)
	mappy.to_str(sol, call_count)
	
	