# CS76: AI - 21F - PA4 - CSP Map/Circuitboard Solver - Julian Grunauer - 10/19/21
from csp import CSP
from heuristics import lcv_heuristic, degree_heuristic, mrv_heuristic, AC3

# Function to check valid domains
def check_constraints(next_var, potential, constraints, d):
	for con in constraints[next_var]:
		if con not in potential: continue
		if potential[con] == potential[next_var]: return False
	return True

# Problem set up
if __name__ == '__main__':
	v_names = ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY']	
	domain = {}
	total_domain = ['Red', 'Green', 'Blue', 'Yellow']
	for v in v_names:
		domain[v] = ['Red', 'Green', 'Blue', 'Yellow']
	constraints = {
    'AK': [],
    'AL': ['MS', 'TN', 'GA', 'FL'],
    'AR': ['MO', 'TN', 'MS', 'LA', 'TX', 'OK'],
    'AZ': ['CA', 'NV', 'UT', 'CO', 'NM'],
    'CA': ['OR', 'NV', 'AZ'],
    'CO': ['WY', 'NE', 'KS', 'OK', 'NM', 'AZ', 'UT'],
    'CT': ['NY', 'MA', 'RI'],
    'DC': ['MD', 'VA'],
    'DE': ['MD', 'PA', 'NJ'],
    'FL': ['AL', 'GA'],
    'GA': ['FL', 'AL', 'TN', 'NC', 'SC'],
    'HI': [],
    'IA': ['MN', 'WI', 'IL', 'MO', 'NE', 'SD'],
    'ID': ['MT', 'WY', 'UT', 'NV', 'OR', 'WA'],
    'IL': ['IN', 'KY', 'MO', 'IA', 'WI'],
    'IN': ['MI', 'OH', 'KY', 'IL'],
    'KS': ['NE', 'MO', 'OK', 'CO'],
    'KY': ['IN', 'OH', 'WV', 'VA', 'TN', 'MO', 'IL'],
    'LA': ['TX', 'AR', 'MS'],
    'MA': ['RI', 'CT', 'NY', 'NH', 'VT'],
    'MD': ['VA', 'WV', 'PA', 'DC', 'DE'],
    'ME': ['NH'],
    'MI': ['WI', 'IN', 'OH'],
    'MN': ['WI', 'IA', 'SD', 'ND'],
    'MO': ['IA', 'IL', 'KY', 'TN', 'AR', 'OK', 'KS', 'NE'],
    'MS': ['LA', 'AR', 'TN', 'AL'],
    'MT': ['ND', 'SD', 'WY', 'ID'],
    'NC': ['VA', 'TN', 'GA', 'SC'],
    'ND': ['MN', 'SD', 'MT'],
    'NE': ['SD', 'IA', 'MO', 'KS', 'CO', 'WY'],
    'NH': ['VT', 'ME', 'MA'],
    'NJ': ['DE', 'PA', 'NY'],
    'NM': ['AZ', 'UT', 'CO', 'OK', 'TX'],
    'NV': ['ID', 'UT', 'AZ', 'CA', 'OR'],
    'NY': ['NJ', 'PA', 'VT', 'MA', 'CT'],
    'OH': ['PA', 'WV', 'KY', 'IN', 'MI'],
    'OK': ['KS', 'MO', 'AR', 'TX', 'NM', 'CO'],
    'OR': ['CA', 'NV', 'ID', 'WA'],
    'PA': ['NY', 'NJ', 'DE', 'MD', 'WV', 'OH'],
    'RI': ['CT', 'MA'],
    'SC': ['GA', 'NC'],
    'SD': ['ND', 'MN', 'IA', 'NE', 'WY', 'MT'],
    'TN': ['KY', 'VA', 'NC', 'GA', 'AL', 'MS', 'AR', 'MO'],
    'TX': ['NM', 'OK', 'AR', 'LA'],
    'UT': ['ID', 'WY', 'CO', 'NM', 'AZ', 'NV'],
    'VA': ['NC', 'TN', 'KY', 'WV', 'MD', 'DC'],
    'VT': ['NY', 'NH', 'MA'],
    'WA': ['ID', 'OR'],
    'WI': ['MI', 'MN', 'IA', 'IL'],
    'WV': ['OH', 'PA', 'MD', 'VA', 'KY'],
    'WY': ['MT', 'SD', 'NE', 'CO', 'UT', 'ID'],
}

	call_count = [0] # Variable to track amount of time the recursive backtracking function is called

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
	# lcv_test = CSP(v_names, domain, total_domain, constraints, check_constraints, None, lcv_heuristic)
	# sol = lcv_test.backtrack(call_count)
	# lcv_test.to_str(sol, call_count)

	# Testing Inference
	AC3_test = CSP(v_names, domain, total_domain, constraints, check_constraints, AC3)
	sol = AC3_test.backtrack(call_count)
	AC3_test.to_str(sol, call_count)
	
	