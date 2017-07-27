# Linked Lists

## Single Linked List
```py
class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
a.value # 1
a.nextnode.value # 2
```


## Double Linked List

```py
class DoublyLinkedListNode(object):

  def __init__(self, value):
    self.value = value
    self.next_node = None
    self.prev_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b  #header
b.prev_node = a

b.next_node = c #trailer
c.pre_node = b

```


## Singly Linked List Cycle Check
- Given a singly linked list, write a function which takes in the first node
in a singly linked list and returns a boolean indicating if the linked list
contains a "cycle".

- A cycle is when a node's next point actually points back to a previous node
in the list. This is also sometimes known as a circularly linked list.

```py
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
```

## Linked List Reversal

- Write a function to reverse a Linked List in place. The function
will take in the head of the list as input and return the new head
of the list.

- You are given the example Linked List Node class

```py
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

print a.nextnode.value # This will give an error since it now points to None
```


## Linked List Nth to Last Node

- Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:

```py
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
```
