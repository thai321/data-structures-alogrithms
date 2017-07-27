class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

def cycle_check(node): # (not work for all cases)
  header = node   # only works for a complete cycle, not a cycle
  current = header.nextnode     # track in the middle of the list
  while current != None :
    if current == header:
      return True
    current = current.nextnode
  return False

def cycle_check(node):  # works for all cycle track
  marker1 = marker2 = node

  while (marker2 != None) and (marker2.nextnode != None):
    marker1 = marker1.nextnode
    marker2 = marker2.nextnode.nextnode

    if marker1 == marker2:
      return True
  return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


cycle_check(a) # true for cycle_check(b) and cycle_check(c)


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

cycle_check(x) # False for cycle_check(y) and cycle_check(z)
