class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

def nth_to_last_node(n, head): #  version 1 works, not the edge cases
  current = head # slow, but fast

  while current:
    temp = current
    value = temp.value
    i = 0
    while temp and i <= n:
      temp = temp.nextnode
      i += 1
    if (i == n) and temp == None:
      return value
    else:
      current = current.nextnode
  return None

def nth_to_last_node(n, head): # fast version
  left_pointer = head
  right_pointer = head

  for i in xrange(n - 1):   # do n times
    if not right_pointer.nextnode:
      raise LookupError('Error: n is larger than the linked list')

    right_pointer = right_pointer.nextnode

  while right_pointer.nextnode:
    left_pointer = left_pointer.nextnode
    right_pointer = right_pointer.nextnode

  return left_pointer.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

nth_to_last_node(2,a) # 4
