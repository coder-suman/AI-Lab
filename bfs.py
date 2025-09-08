from collections import deque

def bfs(graph, start):
    visited = set() 
    queue = deque([start])  
    traversal_order = []  

    while queue:
        vertex = queue.popleft()  
        if vertex not in visited:
            visited.add(vertex)  
            traversal_order.append(vertex)  

            # Enqueue all unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# Example usage
if __name__ == "__main__":
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("BFS Traversal Order:", bfs(sample_graph, 'A'))
