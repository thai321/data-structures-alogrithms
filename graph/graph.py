# python3
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
