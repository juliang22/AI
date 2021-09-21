class SearchSolution:
    def __init__(self, problem, search_method, path=[], num_nodes=0):
        self.problem_name = str(problem)
        self.search_method = search_method
        self.path = path
        self.num_nodes = num_nodes

    def __str__(self):
        string = "----\n"
        string += "{:s}\n"
        string += "Attempted with search method: {:s}\n"

        if len(self.path) > 0:

            string += "Number of nodes visited: {:d}\n"
            string += "Solution length: {:d}\n"
            string += "Path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                                   self.num_nodes, len(self.path), str(self.path))
        else:
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(
                self.problem_name, self.search_method, self.num_nodes)

        return string
