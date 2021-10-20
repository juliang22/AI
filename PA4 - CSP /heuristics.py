# CS76: AI - 21F - PA4 - CSP Map/Circuitboard Solver - Julian Grunauer - 10/19/21
from collections import defaultdict

def lcv_heuristic(next_var, leftover_vars, potential, constraints, domain):
	d_copy = domain[next_var].copy()
	for con in constraints[next_var]:
		if potential.get(con, None) and potential[con] in d_copy:
			d_copy.remove(potential[con])
	
	maxx = float('-inf')
	res = d_copy[0]
	for dom in d_copy:
		total = 0
		for con in constraints[next_var]:
			con_dom = set(domain[con]) - {dom}
			for cons_cons in constraints[con]:
				if potential.get(cons_cons, None):
					con_dom -= {potential[cons_cons]}
			total += len(con_dom)

		if total > maxx:
			maxx = len(con_dom)
			res = dom
	return res
			

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
	for var in leftover_vars:
		dom = {x for x in domain[var]}
		for con in constraints[var]:
			if potential.get(con, None) in dom:
				dom.discard(potential[con])
		if len(dom) < minn:
			minn = min(minn, len(dom))
			res = var
	return res


def AC3(d, c):
	new_c = c.copy()
	if_updated = defaultdict(lambda: [])
	for val, cons in new_c.items():
		for con in cons:
			d1, d2 = d[val], d[con]
			if len(d1) == 1: 
				d[con] = list(set(d2) - set(d1))
				if len(d[con]) == 0:
					return None
			if len(d2) == 1:
				d[val] = list(set(d1) - set(d2))
				if len(d[val]) == 0:
					return None
	return True