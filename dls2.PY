class SimpleProblem:
    def __init__(self, initial, goal, graph):
        self._initial = initial
        self._goal = goal
        self._graph = graph  # adjacency list {node: [neighbors]}
    
    def initial_state(self):
        return self._initial
    
    def is_goal(self, state):
        return state == self._goal
    
    def expand(self, state):
        return self._graph.get(state, [])

def depth_limited_search(problem, depth_limit):
    def recursive_dls(state, depth):
        if problem.is_goal(state):
            return [state]
        elif depth == 0:
            return "cutoff"
        else:
            cutoff_occurred = False
            for child in problem.expand(state):
                result = recursive_dls(child, depth - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "failure":
                    return [state] + result
            return "cutoff" if cutoff_occurred else "failure"

    return recursive_dls(problem.initial_state(), depth_limit)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': ['H','I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

problem = SimpleProblem('A', 'I', graph)
result = depth_limited_search(problem, depth_limit=3)
print(result)  # Expected output: ['A', 'B', 'E', 'F'] or ['A', 'C', 'F'] depending on traversal order
