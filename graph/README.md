# Graph

## Adjacency List implementation

## Word Ladder problem
- Transform the word "FOOL" into the word "SAGE".
- In a word ladder puzzle you must make the change occur gradualy by changing one letter at a time.
- At each step you must transform one word into another word, you are not allowed to transform a word into a non-word
>- `Example`:
  FOOL -> POOL -> POLL -> POLE -> PALE -> SALE -> SAGE

- `Solve` this problem using a graph algorithm.
  - Represent the relationships between the words as a graph
  - Use the graph algorithm known as breadth first search to find an efficient path from the starting word to the ending word.
- Figure out how to turn a large collection of words into a graph.
- What we would like is to have an edge from one word to another if the two words are only different by a single letter.
- Then any path from one word to another is a solution to the word ladder puzzle

- Suppose that we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the letters in the label has been replaced by an underscore.
- We can implement the scheme we have just described by using a dictionary.
- The labels on the buckets we have just described are the keys in our dictionary.
- The value stored for that key is a list of words.
- Once we have the dictionary built we can create the graph.
- We start our graph by creating a vertex for each word in the graph.
- Then we create edges between all the vertices we find for words found under the same key in the dictionary


## Knight's Tour Problem

## Adjacency List Implementation
```python
class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {}

  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, nbr):
    return self.connectedTo[nbr]

  def __str__(self):
    return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices += 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self, n):
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None

  def addEdge(self, f, t, cost=0): # f: from , t: to
    if f not in self.vertList:
      self.addVertex(f)
    if t not in self.vertList:
      self.addVertex(t)

    self.vertList[f].addNeighbor(self.vertList[t], cost)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values()) # list of Vertex

  def __contain__(self, n):
    return n in self.vertList
"""
g = Graph()
for i in range(6): # 0-5 --> 6 vertices
  g.addVertex(i)

print g.vertList

g.addEdge(0, 1, 2)  # edge [0,1] with weight = 2

for vertex in g:
  print vertex
  print vertex.getConnections()
  print '\n'
"""
```

## Graph Implementation

```python
from enum import Enum
from collections import OrderedDict # a dictionary, remember the keys order

class State(Enum):
  unvisited  = 1
  visited = 2
  visiting = 3

class Node:
  def __init__(self, num):
    self.num = num
    self.visit_state = State.unvisited
    self.adjacent = OrderedDict() # key = node, value = weight

  def __str__(arg):
    return str(self.num)

class Graph:
  def __init__(self):
    self.nodes = OrderedDict()

  def add_node(self, num):
    node = Node(num)
    self.nodes[num] = node
    return node

  def add_edge(self, source, dest, weight=0):
    if source not in self.nodes:
      self.add_node(source)
    if dest not in self.nodes:
      self.add_node(dest)

    self.nodes[source].adjacent[self.nodes[dest]] = weight

"""
g = Graph()
g.add_edge(0,1, 5) # edge [0,1]
print (g.nodes) # node 0 and node 1

g.add_edge(1,2,3) # edge [1,2]
print (g.nodes) # node 0, node 1, and node 2
"""
```

## Depth First Search (DFS)

```python
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


def dfs_recursive(graph, start, visited=None): # using recursive
  if visited is None:
      visited = set()

  visited.add(start)

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

print (list(dfs_paths(graph, 'A', 'F')))
#[['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
```

## Breadth First Search (BFS)
```python
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs_set(graph, start): # using set
  visited = set()
  queue = [start]

  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      visited.add(vertex)
      queue.extend(graph[vertex] - visited)

  return visited
print (bfs_set(graph, 'A')) # {'A', 'E', 'F', 'D', 'B', 'C'}

def bfs_paths(graph, start, goal): # return all the possible paths
  queue = [(start, [start])]      # return the shorest path first
  while queue:
    (vertex, path) = queue.pop(0)
    for next in graph[vertex] - set(path):
      if next == goal:
        yield path + [next]
      else:
        queue.append((next, path + [next]))

print (list(bfs_paths(graph, 'A', 'F')))
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
  try:
    return next(bfs_paths(graph, start, goal))
  except StopIteration:
    return None

print (shortest_path(graph, 'A', 'F'))
# ['A', 'C', 'F']
```
