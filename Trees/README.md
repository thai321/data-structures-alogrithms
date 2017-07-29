# Trees

## Tree
- A tree data structure has a root, branches, and leaves.
- The difference between a tree in nature and a tree in computer
science is that a tree data structure has its root at the top
and its leaves on the bottom.

- A second property of trees is that all of the children of one node
are independent of the children of another node.
- A third property is that each leaf node is unique.

- Another example of a tree structure that you probably use
every day is a file system. In a file system, directories, or
folders, are structured as a tree.


## Node

- A node is fundamental part of a trre. It can have a name, which
we call the "key."
- A node may also have additional information. We clal this
additional information the "payload."
- While the payload information is not central to many tree
alogirthms, it is often critcal in applicaitons that make use of
trees.

## Edge

- An edge is another fundamental part of a tree.
- An edge connects two nodes to show that there is a realationship
between them.
- Every node (except the root) is connected by exactly one incoming
edge from another node.
- Each node may have several outgoing edges.


## Root

- The root of the tree is the only node in the tree that has no incoming edges.


## Path

- A path is an ordered list of nodes that are connected by edges.
- For example:
   Mammal --> Carnivora --> Felidae --> Felis is a path.

## Children

- The set of nodes "c" that have incoming edges from the same node
to are said to be the children of that node.

## Parent

- A node is the parent of all the nodes it connects to with outgoing
edges.


## Sibling

- nodes in the tree that are children of the same parent are said
to e siblings

## SubTree

- A subtree is a set of nodes and edges comprised of a parent and
all the descendants of that parent.

## Leaf Node

- A leaf node is a node that has no children.

## Level

- The level of a node "n" is the number of edges on the path from
the root node to n

## Height

- The height of a tree is equal to the maximum level of any node
in the tree.

## Full Definition of a Tree

- A tree consists of a set of nodes and a set of edges that connect
pairs of nodes. A tree has the following properties:
    + One node of the tree is designated as the root node.
    + Every node n, except the root node, is connected by an edge
    from exactly one other node p, where p is the parent of n.
    + A unique path traverses from the root to each node.
    + If each node in the tree has a maximum of two children, we
    say that the tree is a binary tree.

## Recursive Definition of a Tree
- A tree is either empty or cinsists of a root and zero or more
subtrees, each of which is also a tree.
- The root of each subtree is connected to the root of the parent
tree by an edge.


## Tree Representation Implementation (Lists)

```py
def BinaryTree(r): # r is root node
  return [r,[],[]] # [],[] are left and right child of the node
```

```py
def insertLeft(root,newBranch): # newBranch is the value of a node
  t = root.pop(1)
  if len(t) > 1:
    root.insert(1, [newBranch,t,[]])
  else:
    root.insert(1,[newBranch,[],[]])
  return root
```
```py
def insertRight(root,newBranch):
  t = root.pop(2)
  if len(t) > 1:
    root.insert(2, [newBranch,[],t])
  else:
    root.insert(2,[newBranch,[],[]])
  return root
```

```py
def getRootVal(root):
  return root[0]
```

```py
def setRootVal(root, newVal):
  root[0] = newVal
```

```py
def getLeftChild(root):
  return root[1]
```

```py
def getRightChild(root):
  return root[2]
```

```py
r = BinaryTree(3)
```

```py
insertLeft(r,4) # [3, [4, [], []], []]

insertLeft(r,5) # [3, [5, [4, [], []], []], []]

insertRight(r,6) # [3, [5, [4, [], []], []], [6, [], []]]

insertRight(r,7) # [3, [5, [4, [], []], []], [7, [], [6, [], []]]]


l = getLeftChild(r)
print l # [5, [4, [], []], []]

setRootVal(l,9) # print r
# [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
```


## Nodes and References Implementation

```py
class BinaryTree(object):

  def __init__(self,rootObj):

    self.key = rootObj
    self.leftChild = None
    self.rightChild = None

  def insertLeft(self, newNode):
    if self.leftChild == None:
      self.leftChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRight(self, newNode):
    if self.rightChild == None:
      self.rigthChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t

  def getRightChild(self):
    return self.rightChild

  def getLeftChild(self):
    return self.leftChild

  def setRootVal(self,obj):
    self.key = obj

  def getRootVal(self):
    return self.key

r = BinaryTree('a')

r.getRootVal() # 'a'

print r.getLeftChild() # None

r.insertLeft('b')

r.getLeftChild() # <__main__.BinaryTree at 0x10689a290>

r.getLeftChild().getRootVal() # 'b'
```


## Tree Traversal
- There are three commonly used patterns to visit all the nodes in
a tree.
- The difference between these patterns is the order in which
each node is visited (a "traversal")
- The three traversals we will look at are called preorder, inorder,
and postorder.


## Preorder

- In a preorder traversal, we visit the root node first, then
recursively do a preorder traversal of the left subtree, followed
by a recursive preorder raversal of the right subtree.


## Inorder

- In an inorder traversal, we recursively do an inorder traversal on
the left subtree, visit the root node, and finnaly d a recursive
inorder traversal of the right subtree.

## Postorder

- In a postorder traversal, we recursively do a postorder traversal
of the left subtree and the right subtree followed by a visit to the
root node.



```py
# Base case is simply to check if the tree exists.
# If the tree parameter is None, then the function
# returns without taking any action

def preorder(tree): # as a method
  if tree:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())

def preorder(self):# as a class
  print(self.key)
  if self.leftChild:
    self.leftChild.preorder()
  if self.rightChild:
    self.rightChild.preorder()

def postorder(tree):
  if tree != None:
    postorder(tree.getLeftChild())
    postorder(tree.getRigthChild())
    print(tree.getRootVal())

    # In the inorder traversal we visit the left subtree,
    # followed byt he root, and finally the right subtree

def inorder(tree):
  if tree != None:
    inorder(tree.getLeftChild())
    print(tree.getRootVal())
    inorder(tree.getRigthchild())
```

## Binary Heap
- In order to make our heap work efficiently, we will take advantage
of the logrthmic nature of the binary tree to represent our heap.
- In order to guarantee logarithmic performance, we must keep our
tree balanced.

- A balanced binary tree has roughly the same number of nodes in
the left and right subtrees of the root.
- In our heap implementation we keep the tree balanced by creating
a complete binary tree.
- A complete binary tree is a tree in which each level has all of
its nodes.

- Remember that inserting an item in the middle of the list may
require O(n) operations to shift the rest of the list over to make
room for the new key.
- Therefore, to insert n keys into the heap would require a total of O(nlogn) operations.
- However, if we start with an entire list then we can build the
whole heap in O(n) operations.


```py
class BinHeap:

def __init__(self):
  self.heapList = [0]
  self.currentSize = 0

def percUp(self, i):
  while i // 2 > 0:
    if self.heapList[i] < self.heapList[i // 2]:
      tmp = self.heapList[i // 2]
      self.heapList[i // 2] = self.heapList[i]
      self.heapList[i] = tmp
    i = i // 2

def insert(self, k):
  self.heapList.append(k)
  self.currenSize = self.currentSize + 1
  self.percUp(self.currentSize)

def percDown(self, i):
  while (i * 2) <= self.currentSize:
    mc = self.minChild(i)
    if self.heapList[i] > self.heapList[mc]:
      tmp = self.heapList[i]
      self.heapList[i] = self.heapList[mc]
      self.heapList[mc] = tmp
    i = mc

def minChild(self,i):
  if i * 2  + 1 > self.currentSize:
    return i * 2
  else:
    if self.heapList[i * 2] < self.heapList[i*2+1]:
      return i * 2
    else:
      return i * 2 + 1

def delMin(self):
  retval = self.heapList[1]
  self.heapList[1] = self.heapList[self.currentSize]
  self.currentSize = self.currentSize - 1
  self.heapList.pop()
  self.percDown(1)
  return retval

def buildHeap(self,alist):
  i = len(alist)//2
  self.currentSize = len(alist)
  self.heapList = [0] + alist[:]
  while (i > 0):
    self.percDown(i)
    i = i - 1
```


## Binary Search Trees Implementation

```py
class TreeNode:

  def __init__(self,key,val,left=None,right=None,parent=None):
    self.key = key
    self.payload = val
    self.leftChild = left
    self.rightChild = right
    self.parent = parent

  def hasLeftChild(self):
    return self.leftChild

  def hasRightChild(self):
    return self.rightChild

  def isLeftChild(self):
    return self.parent and self.parent.leftChild == self

  def isRightChild(self):
    return self.parent and self.parent.rightChild == self

  def isRoot(self):
    return not self.parent

  def isLeaf(self):
    return not (self.rightChild or self.leftChild)

  def hasAnyChildren(self):
    return self.rightChild or self.leftChild

  def hasBothChildren(self):
    return self.rightChild and self.leftChild

  def replaceNodeData(self,key,value,lc,rc): # the root
    self.key = key
    self.payload = value
    self.leftChild = lc
    self.rightChild = rc
    if self.hasLeftChild():
      self.leftChild.parent = self
    if self.hasRightChild():
      self.rightChild.parent = self
```


```py
### Part I ###
class BinarySearchTree:

  def __init__(self):
    self.root = None
    self.size = 0

  def length(self):
    return self.size

  def __len__(self):
    return self.size

  def put(self,key,val):
    if self.root:
        self._put(key,val,self.root)
    else:
        self.root = TreeNode(key,val)
    self.size = self.size + 1

  def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
          self._put(key,val,currentNode.leftChild)
        else:
          currentNode.leftChild = TreeNode(key,val,parent=currentNode)
    else:
        if currentNode.hasRightChild():
           self._put(key,val,currentNode.rightChild)
        else:
           currentNode.rightChild = TreeNode(key,val,parent=currentNode)

  def __setitem__(self,k,v):
    self.put(k,v)

  def get(self,key):
    if self.root:
      res = self._get(key,self.root)
      if res:
        return res.payload
      else:
          return None
    else:
        return None

  def _get(self,key,currentNode):

    if not currentNode:
      return None
    elif currentNode.key == key:
      return currentNode
    elif key < currentNode.key:
      return self._get(key,currentNode.leftChild)
    else:
      return self._get(key,currentNode.rightChild)

  def __getitem__(self,key):
    return self.get(key)

  def __contains__(self,key):
    if self._get(key,self.root):
      return True
    else:
      return False

  def delete(self,key):

    if self.size > 1:

      nodeToRemove = self._get(key,self.root)
      if nodeToRemove:
        self.remove(nodeToRemove)
        self.size = self.size-1
      else:
        raise KeyError('Error, key not in tree')
    elif self.size == 1 and self.root.key == key:
      self.root = None
      self.size = self.size - 1
    else:
      raise KeyError('Error, key not in tree')

  def __delitem__(self,key):
    self.delete(key)

  def spliceOut(self):  # to remove the successor and fix the tree
  if self.isLeaf():
    if self.isLeftChild():

      self.parent.leftChild = None
    else:
      self.parent.rightChild = None
  elif self.hasAnyChildren():
    if self.hasLeftChild():

      if self.isLeftChild():

        self.parent.leftChild = self.leftChild
      else:

        self.parent.rightChild = self.leftChild
        self.leftChild.parent = self.parent
  else:

    if self.isLeftChild():

      self.parent.leftChild = self.rightChild
    else:
      self.parent.rightChild = self.rightChild
      self.rightChild.parent = self.parent

  def findSuccessor(self):
  #1) has a right child, find that successor in the right branch child
    succ = None
    if self.hasRightChild():    # current node has right child
      succ = self.rightChild.findMin()  # --- > find min value of that child (keep going left)
    else:
        if self.parent:   # 2) has no right child, has a parent

          if self.isLeftChild(): # is the left child of its parent
                              # --> successor will be the parent
            succ = self.parent
          else:  # is the right child of its parent, cut the right branch (self) of its parent
            self.parent.rightChild = None
            succ = self.parent.findSuccessor()   # find the successor of its parent branch
            self.parent.rightChild = self  # set the right branch (self) back
    return succ

  def findMin(self):

    current = self
    while current.hasLeftChild():
        current = current.leftChild
    return current

  def remove(self,currentNode):

    if currentNode.isLeaf(): #leaf
      if currentNode == currentNode.parent.leftChild:
        currentNode.parent.leftChild = None
      else:
        currentNode.parent.rightChild = None
    elif currentNode.hasBothChildren(): #interior

      succ = currentNode.findSuccessor()
      succ.spliceOut()    # remove the successor
      currentNode.key = succ.key      #update the remove key from successor
      currentNode.payload = succ.payload  # update the remove key from successor

    else: # this node has one child
      if currentNode.hasLeftChild():
        if currentNode.isLeftChild():
          currentNode.leftChild.parent = currentNode.parent
          currentNode.parent.leftChild = currentNode.leftChild
        elif currentNode.isRightChild():
          currentNode.leftChild.parent = currentNode.parent
          currentNode.parent.rightChild = currentNode.leftChild
        else:
                # is the root
          currentNode.replaceNodeData(currentNode.leftChild.key,
                            currentNode.leftChild.payload,
                            currentNode.leftChild.leftChild,
                            currentNode.leftChild.rightChild)
      else:

        if currentNode.isLeftChild():
          currentNode.rightChild.parent = currentNode.parent
          currentNode.parent.leftChild = currentNode.rightChild
        elif currentNode.isRightChild():
          currentNode.rightChild.parent = currentNode.parent
          currentNode.parent.rightChild = currentNode.rightChild
        else:   # is the root
          currentNode.replaceNodeData(currentNode.rightChild.key,
                            currentNode.rightChild.payload,
                            currentNode.rightChild.leftChild,
                            currentNode.rightChild.rightChild)
```

## Binary Search Tree check (BST)

- Given a binary tree, check whether it’s a binary search tree or not.

```py
tree_vals = []

def inorder(tree):
  if tree != None:
    inorder(tree.getLeftChild())
    tree_vals.append(tree.getRootVal())
    inorder(tree.getRightChild())

def sort_check(tree_vals):
  return tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)
```


```py
# another solution to keep track of the minimum and maximum values
# a node can take. And at each node we will check whether its value
# is between the min and max values it's allowed to take.
class Node:
  def __init__(self, k, val):
    self.key = k
    self.value = val
    self.left = None
    self.right = None

  def tree_max(node):
    if not node:
      return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

  def tree_min(node):
    if not node:
      return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

  def verify(node):
    if not node:
      return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
      verify(node.left) and verify(node.right)):
      return True
    else:
      return False


root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10
```


## Tree Level Order Print

```txt
Given a binary tree of integers, print it in level order. The output
will contain space between the numbers in the same level, and new

line between different levels. For example, if the tree is:
           6
1 --- 3 ---5
      2 ---4

http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Trees/Trees%20Interview%20Problems/tree_print.png


The output should be:

1
2 3
4 5 6
```

```py
import collections

class Node:
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val =  val

    import collections

d = collections.deque([1,2,3]) # can append, popLeft,...
d.append([4])
d.popleft()
d.pop()
print d



def levelOrderPrint(tree): # O(n), n is number of nodes

  if not tree:
    return

  nodes = collections.deque([tree])

  currentCount = 1
  nextCount = 0

  while len(nodes) != 0:

    currentNode = nodes.popleft()
    currentCount -= 1

    print currentNode.val,

    if currentNode.left:
      nodes.append(currentNode.left)
      nextCount += 1

    if currentNode.right:
      nodes.append(currentNode.right)
      nextCount += 1

    if currentCount == 0:
      print '\n'
      currentCount, nextCount = nextCount, currentCount

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.left = two
two.left = four
one.right = three
three.left = five
three.right = six

levelOrderPrint(one)
1

2 3

4 5 6
```


## Trim a Binary Search Tree

- Given the root of a binary search tree and 2 numbers min and max,
trim the tree such that all the numbers in the new tree are between
min and max (inclusive). The resulting tree should still be a valid
binary search tree. So, if we get this tree as input:

- http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Trees/Trees%20Interview%20Problems/bst1.png

- and we’re given min value as 5 and max value as 13, then the
resulting binary search tree should be:

- http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Trees/Trees%20Interview%20Problems/bst_trim.png


- We should remove all the nodes whose value is not between min and
max.

```py
def trimBST(tree,minVal,maxVal):

  if not tree:
    return

  tree.left = trimBST(tree.left, minVal, maxVal)
  tree.right = trimBST(tree.right, minVal, maxVal)

  if minVal <= tree.val <= maxVal:
    return tree

  if tree.val < minVal:
    return tree.right

  if tree.val > maxVal:
    return tree.left


# Use tree.left , tree.right , and tree.val as your methods to call
```

- We can do this by performing a post-order traversal of the tree. We
first process the left children, then right children, and finally
the node itself. So we form the new tree bottom up, starting from
the leaves towards the root. As a result while processing the node
itself, both its left and right subtrees are valid trimmed binary
search trees (may be NULL as well).

- At each node we’ll return a reference based on its value, which will
then be assigned to its parent’s left or right child pointer,
depending on whether the current node is left or right child of the
parent. If current node’s value is between min and max
(min<=node<=max) then there’s no action need to be taken, so we
return the reference to the node itself. If current node’s value is
less than min, then we return the reference to its right subtree,
and discard the left subtree. Because if a node’s value is less than
min, then its left children are definitely less than min since this
is a binary search tree. But its right children may or may not be
less than min we can’t be sure, so we return the reference to it.
Since we’re performing bottom-up post-order traversal, its right
subtree is already a trimmed valid binary search tree (possibly
NULL), and left subtree is definitely NULL because those nodes were
surely less than min and they were eliminated during the post-order
traversal. Remember that in post-order traversal we first process
all the children of a node, and then finally the node itself.

- Similar situation occurs when node’s value is greater than max, we
now return the reference to its left subtree. Because if a node’s
value is greater than max, then its right children are definitely
greater than max. But its left children may or may not be greater
than max. So we discard the right subtree and return the reference
to the already valid left subtree. The code is easier to understand

- The complexity of this algorithm is O(N), where N is the number of
nodes in the tree. Because we basically perform a post-order
traversal of the tree, visiting each and every node one. This is
optimal because we should visit every node at least once. This is a
very elegant question that demonstrates the effectiveness of
recursion in trees.
