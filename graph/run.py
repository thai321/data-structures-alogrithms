from adjacency_list import Graph

g = Graph()
for i in range(6): # 0-5 --> 6 vertices
  g.addVertex(i)

print g.vertList

g.addEdge(0, 1, 2)  # edge [0,1] with weight = 2

for vertex in g:
  print vertex
  print vertex.getConnections()
  print '\n'
