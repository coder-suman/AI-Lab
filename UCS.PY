class SimpleCostProblem:
    def __init__(self, initial, goal, graph):
        self._initial = initial
        self._goal = goal
        self._graph = graph  # adjacency list {node: [(neighbor, cost), ...]}

    def initial_state(self):
        return self._initial

    def is_goal(self, state):
        return state == self._goal

    def expand(self, state):
        return self._graph.get(state, [])

def uniform_cost_search(problem):
    frontier = [(0, [problem.initial_state()])]  # list of (cost, path)
    explored = set()

    while frontier:
        # Find path with minimum cost
        frontier.sort(key=lambda x: x[0])
        cost, path = frontier.pop(0)
        state = path[-1]

        if problem.is_goal(state):
            return path

        if state not in explored:
            explored.add(state)
            for neighbor, step_cost in problem.expand(state):
                if neighbor not in explored:
                    new_cost = cost + step_cost
                    new_path = path + [neighbor]
                    frontier.append((new_cost, new_path))

    return "failure"

def main():
    print("Enter the number of edges in the graph:")
    edges_count = int(input())

    graph = {}

    print("Enter edges in the format: from_node to_node cost")
    for _ in range(edges_count):
        line = input().strip().split()
        if len(line) != 3:
            print("Invalid input, please enter exactly three values: from_node to_node cost")
            return
        from_node, to_node, cost_str = line
        cost = float(cost_str)

        if from_node not in graph:
            graph[from_node] = []
        graph[from_node].append((to_node, cost))

    print("Enter the start node:")
    start = input().strip()

    print("Enter the goal node:")
    goal = input().strip()

    problem = SimpleCostProblem(start, goal, graph)
    result = uniform_cost_search(problem)

    if result == "failure":
        print("No path found from", start, "to", goal)
    else:
        print("Path found:", " -> ".join(result))

if __name__ == "__main__":
    main()
