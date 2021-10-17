from collections import defaultdict

def lcv_heuristic(next_var, leftover_vars, potential, constraints, domain):
	dom = {x for x in domain[next_var]}
	for con in constraints[next_var]:
		if potential.get(con, None) in dom:
			dom.discard(potential[con])

	for pot_dom in dom:
		maxx = float('-inf')
		for con in constraints[next_var]:
			if con not in potential:
				summ = 0
				for other_con in constraints[con]:
					other_dom = domain[other_con]
					# if other_con == con: continue
					if pot_dom in other_dom: other_dom.remove(pot_dom)
					if potential.get(other_con, None) in other_dom:
						other_dom.discard(potential[con])
					summ += len(other_dom)
				if summ > maxx:
					maxx = max(maxx, summ)
					res = pot_dom
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


def mrv_heuristic(leftover_vars, potential, constraints, domain, t):
	res = leftover_vars[0]
	minn = float('inf')
	for var in leftover_vars:
		dom = {x for x in domain[var]}
		for con in constraints[var]:
			if potential.get(con, None) in dom:
				# dom.discard(potential[con])
				print(t[potential[con]])
				dom = dom - set(t[potential[con]])
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