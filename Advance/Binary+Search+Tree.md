
### Sorted arrays
- Inserting a new item is quite slow // O(N)
- Searching is quite fast with binary search // O(logN)
- Removing an item is slow // O(N)

### Linked Lists
- Inserting a new item is very fast // O(1)
- Searching is sequental // O(N)
- Removing an item is fast because of the references // O(1)

-->  Binary Search Trees are going to make all of these operations quite fast, with **O(log N)** time complexity !!! ~ predictable


```python
class Node(object):
  def __init__(self, data):
    self.data = data;
    self.leftChild = None;
    self.rightChild = None;
```


```python
class BinarySearchTree(object):
  def __init__(self):
    self.root = None;
    
  def insert(self, data):
    if not self.root:
      self.root = Node(data);
    else:
      self.insertNode(data, self.root);
  
  # O(log N) if the tree is balanced!!!!!!! --> it can reduced to O(N) --> AVL RBT are needed!!!!
  def insertNode(self, data, node):
    if data < node.data:
      if node.leftChild:
        self.insertNode(data, node.leftChild)
      else :
        node.leftChild = Node(data)
    else:
      if node.rightChild:
        self.insertNode(data, node.rightChild);
      else:
        node.rightChild = Node(data);
        
  def removeNode(self, data, node):
    if not node:
      return node;
    
    if data < node.data:
      node.leftChild = self.removeNode(data, node.leftChild);
    elif data > node.data:
      node.rightChild = self.removeNode(data, node.rightChild);
    else:
      if not node.leftChild and not node.rightChild:
        print("Removing a leaf node...");
        del node;
        return None;
      
      if not node.leftChild:
        print("Removing a node with single right child...");
        tempNode = node.rightChild;
        del node;
        return tempNode;
      elif not node.rightChild:
        print("Removing a node with single left child...");
        tempNode = node.leftChild;
        del node;
        return tempNode;
      
      print("Removing node with two children...");
      tempNode = self.getPredecessor(node.leftChild);
      node.data = tempNode.data;
      node.leftChild = self.removeNode(tempNode.data, node.leftChild);
    
    return node;
      
  def getPredecessor(self, node):
    if node.rightChild:
      return self.getPredecessor(node.rightChild);
    return node;
      
  def remove(self, data):
    if self.root:
      self.root = self.removeNode(data, self.root);
  
  def getMinValue(self):
    if self.root:
      return self.getMin(self.root);
  def getMin(self, node):
    if node.leftChild:
      return self.getMin(node.leftChild);
    return node.data
  
  def getMaxValue(self):
    if self.root:
      return self.getMax(self.root);
  def getMax(self, node):
    if node.rightChild:
      return self.getMax(node.rightChild);
    return node.data
  
  def traverse(self):
    if self.root:
      self.traverseInOrder(self.root);
  def traverseInOrder(self, node):
    
    if node.leftChild:
      self.traverseInOrder(node.leftChild);
    
    print("%s " % node.data);
    
    if node.rightChild:
      self.traverseInOrder(node.rightChild);
```


```python
bst = BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(13);
bst.insert(14);
bst.insert(6);

print(bst.getMinValue());
print(bst.getMaxValue());
```

    5
    14



```python
bst.traverse();
```

    5 
    6 
    10 
    13 
    14 



```python
bst.remove(5)
bst.traverse();
```

    Removing a node with single right child...
    6 
    10 
    13 
    14 



```python
bst.remove(10)
bst.traverse()
```

    Removing node with two children...
    Removing a leaf node...
    6 
    13 
    14 



```python

```
