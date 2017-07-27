class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

def reverse(head): # version 1
  prev = head
  current = head.nextnode
  prev.nextnode = None

  while current != None:
    temp = current.nextnode # next node
    current.nextnode = prev  # set current node to previous node

    prev = current   # update previous to current node
    current = temp   # current node to next node

def reverse(head):
  current = head
  previous = None
  nextNode = None

  while current:
    nextNode = current.nextnode

    current.nextnode = previous
    previous = current
    current = nextNode

  return previous # head now

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.nextnode.value # 2
print b.nextnode.value # 3
print c.nextnode.value # 4

d.nextnode.value  # should be None, 'NoneType' object has no attribute value

reverse(a)

print d.nextnode.value # 3
print c.nextnode.value # 2
print b.nextnode.value # 1


print a.nextnode.value # This will give an error
                      # since it now points to None
