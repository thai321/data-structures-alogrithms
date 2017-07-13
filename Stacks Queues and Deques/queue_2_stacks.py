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
