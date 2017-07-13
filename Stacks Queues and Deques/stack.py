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
