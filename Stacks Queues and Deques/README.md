# Stacks Queues and Deques

## `Stack Implementation`
```python
class Stack(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)

"""
s = Stack()
s.isEmpty() #True
s.push(1)

s = Stack()
s.push('two')
s.peek()# 'two'
s.push(True)
s.size()# 3
s.isEmpty()# False
s.pop()# True
s.isEmpty()# False
s.pop()# 1
s.isEmpty()# True
"""
```

## `Queue Implementation`
```python
class Queue(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


q = Queue()
q.isEmpty()# True
q.enqueue(1)
q.enqueue(2)
q.size()# 2
q.dequeue()# 1
```

## `Deque Implementation`
```python
class Deque(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0, item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

d = Deque()
d.addFront("hello")
d.addRear('world')
d.size() # 2
print d.removeFront() + ' ' + d.removeRear() #hello world
d.size() # 0
d.isEmpty() # True
```

## `Balanced Parentheses Check`
Given a string of opening and closing parentheses, check whether it’s balanced.
<p>We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
<p>Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
<p>As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
<p>For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.

```python
set('([{') # {'(', '[', '{'}
set([('(', ')'), ('[', ']'), ('{', '}')])
# {('(', ')'), ('[', ']'), ('{', '}')}

def balance_check(s):

  if len(s)%2 != 0:
    return False

  opening =  set('([{')

  matches = set([('(', ')'), ('[', ']'), ('{', '}')])

  stack = []

  for paren in s:
    if paren in opening:
        stack.append(paren)
    else:

      if len(stack) == 0: # there is no opening parenthese for
        return False    # this 'paren' close parenthese

      last_open = stack.pop()
      if (last_open, paren) not in matches:
        return False
  return len(stack) == 0
  # false if the opening parenthese never close

balance_check('[]') # True
balance_check('[](){([[[]]])}') # True
balance_check('()(){]}') # False
```

## `Implement a Queue - Using Two Stacks`
```python
stack1 = []
stack2 = []

class Queue2Stacks1(object):

  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, element):
    self.stack1.append(element)

  def dequeue(self):
    while self.stack1 != [] :
      self.stack2.append(self.stack1.pop())
    return self.stack2.pop()

class Queue2Stacks2(object):

  def __init__(self):
    self.instack = []
    self.outstack = []

  def enqueue(self, element):
    self.instack.append(element)

  def dequeue(self):

    if not self.outstack:
      while self.instack:
        self.outstack.append(self.instack.pop())
    return self.outstack.pop()

"""
q = Queue2Stacks()

for i in xrange(5):
  q.enqueue(i)

for i in xrange(5):
  print q.dequeue()
# 0 1 2 3 4
"""
```
