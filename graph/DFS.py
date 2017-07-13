# python3
# Depth First Search

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_set(graph, start): # using set
  visited = set()
  stack = [start]

  while stack:
    vertex = stack.pop()
    # print (vertex)
    if vertex not in visited:
      visited.add(vertex)

      stack.extend(graph[vertex] - visited)
  return visited

print(dfs_set(graph, 'A')) # {'A', 'D', 'E', 'C', 'B', 'F'}
"""
Stack: [A]
pop A --> Stack: [], visited: [A]
stack.extend(graph[A] - visited) = [B, C] - [A] = [B, C] --> Stack: [B, C]

Stack: [B, C]
pop C --> Stack: [B], visited: [A, C] , graph[C] = [A, F]
[A, F] - [A, C] = [F] --> Stack: [B, F]

Stack: [B, F]
pop F --> Stack: [B], visited: [A, C, F] , graph[F] = [C, E]
[C, E] - [A, C, F] = [E] --> Stack: [B, E]

Stack: [B, E]
pop E --> Stack: [B], visited: [A, C, F, E], graph[E] = [B, F]
[B, F] - [A, C, F, E] = [B] --> Stack: [B, B]

Stack: [B, B]
pop B --> Stack: [B], visited: [A, C, F, E, B]. graph[B] = [A, D, E]
[A, D, E] - [A, C, F, E, B] = [D] --> Stack: [B, D]

Stack: [B, D]
pop D --> Stack: [B], visited: [A, C, F, E, B, D], graph[D] = [B]
[B] - [A, C, F, E, B, D] = [] --> Stack: [B]

Stack: [B]
pop B --> Stack: [], since B in visited: [A, C, F, E, B, D]
return visited = [A, C, F, E, B, D]
"""

def dfs_recursive(graph, start, visited=None): # using recursive
  if visited is None:
    visited = set()
  visited.add(start)
  # print (start)
  for nxt in graph[start] - visited: # build up the visited set
    dfs_recursive(graph, nxt, visited)

  return visited

print (dfs_recursive(graph, 'A')) #{'A', 'B', 'C', 'D', 'E', 'F'}

def dfs_paths(graph, start, goal): # show all paths between 2 nodes
  stack = [ (start, [start]) ] # contain a vertex and path = array of vertices
  while stack:
    (vertex, path) = stack.pop()  # build up the path
    for nxt in graph[vertex] - set(path):
      if nxt == goal:
        yield path + [goal]
      else:
        stack.append( (nxt, path + [nxt]) )

print (list(dfs_paths(graph, 'A', 'F'))) #[['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
