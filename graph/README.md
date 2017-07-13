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


## Breadth First Search (BFS)


## Knight's Tour Problem

## Depth First Search (DFS)

```python3
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
