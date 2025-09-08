def dfs (graph,start,goal,visited=None,path=None):
  if visited is None:
    visited = set()
  if path is None:
    path = []
  visited.add(start)
  path.append(start)
  if start == goal:
    return path
  for neighbor in graph[start]:
    if neighbor not in visited:
      new_path = dfs(graph,neighbor,goal,visited.copy(),path.copy())
      if new_path:
        return new_path
  return None
  #main function
graph = {}
edges = int(input("Enter the number of edges :"))
print("Enter ede=ges (format : u v):")
for _ in range(edges):
  u,v = input().split()
  if u not in graph:
    graph[u] = []
  if v not in graph:
    graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
start = input("Enter the start node :")
goal = input("Enter the goal node :")
  # path = dfs(graph,start,goal)

print("\nGraph :",graph)
print("Start node:",start)
print("Goal node :",goal)

path = dfs(graph,start,goal)
if path:
  print("DFS path:",path)
else:
  print("No path found from0",start,"to",goal)
