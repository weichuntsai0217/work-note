"""
  Use python 3.6.8
"""
"""
  A stack should support methods:
  1. `is_empty` with O(1) time complexity
  2. `push` with O(1) time complexity
  3. `pop` with O(1) time complexity
  4. `get_top` with O(1) time complexity
  5. (optional) `is_max` with O(1) time complexity

  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).
"""

def implement_1():
  """
    Python default list is actually can be a stack.
    Use list append as push.
    Use list pop as pop.
  """
  # Implement start
  class Stack(list):
    pass
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    s.append(i)
  assert s[-1] == 2
  res = []
  for i in range(3):
    res.append(s.pop())

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('implement_1 success')
  # Test end

def implement_2():
  """
    Implement a stack by a class
  """
  # Implement start
  class Stack(object):
    def __init__(self):
      self.data = []

    def is_empty(self):
      return len(self.data) == 0

    def push(self, x):
      self.data.append(x)

    def pop(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element can be popped.')
      return self.data.pop()

    def get_top(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element exits.')
      return self.data[-1]
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    s.push(i)
  assert s.get_top() == 2
  res = []
  for i in range(3):
    res.append(s.pop())

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('implement_2 success')
  # Test end

def implement_3():
  """
    Implement a stack by a stack data and external functions.
  """
  # Implement start
  class Stack(object):
    def __init__(self):
      self.data = []

  def is_empty(s):
    return len(s.data) == 0

  def push(s, x):
    s.data.append(x)

  def pop(s):
    if is_empty(s):
      raise IndexError('The stack is empty. No element can be popped.')
    return s.data.pop()

  def get_top(s):
    if is_empty(s):
      raise IndexError('The stack is empty. No element exists.')
    return s.data[-1]
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    push(s, i)
  assert get_top(s) == 2
  res = []
  for i in range(3):
    res.append(pop(s))

  check_error = False
  try:
    pop(s)
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('implement_3 success')
  # Test end

def implement_4():
  """
    Implement a stack by a class in C/C++ style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen):
      self.top = -1
      self.maxlen = maxlen
      self.data = [None] * self.maxlen # mimic C/C++ style to allocate a fixed-length array.

    def is_empty(self):
      return self.top == -1

    def push(self, x):
      if self.is_max():
        raise IndexError('The stack is full and cannot push any item.')
      self.top += 1
      self.data[self.top] = x

    def pop(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element can be popped.')
      res = self.data[self.top]
      self.top -= 1
      return res

    def get_top(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element exists.')
      return self.data[self.top]

    def is_max(self):
      return self.top == (self.maxlen - 1)
  # Implement end

  # Test start
  s = Stack(10)
  for i in range(3):
    s.push(i)
    assert s.top == i
  assert s.get_top() == 2
  res = []
  for i in range(3):
    assert s.top == (2 - i)
    res.append(s.pop())

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('implement_4 success')
  # Test end

def implement_5():
  """
    Implement a stack by a stack data and other functions in C/C++ style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen):
      self.top = -1
      self.maxlen = maxlen
      self.data = [None] * self.maxlen # mimic C/C++ style to allocate a fixed-length array.

  def is_empty(s):
    return s.top == -1

  def is_max(s):
    return s.top == (s.maxlen - 1)

  def push(s, x):
    if is_max(s):
      raise IndexError('The stack is full and cannot push any item.')
    s.top += 1
    s.data[s.top] = x

  def pop(s):
    if is_empty(s):
      raise IndexError('The stack is empty. No element can be popped.')
    res = s.data[s.top]
    s.top -= 1
    return res

  def get_top(s):
    if is_empty(s):
      raise IndexError('The stack is empty. No element exists.')
    return s.data[s.top]
  # Implement end

  # Test start
  s = Stack(10)
  for i in range(3):
    push(s, i)
    assert s.top == i
  assert get_top(s) == 2
  res = []
  for i in range(3):
    assert s.top == (2 - i)
    res.append(pop(s))

  check_error = False
  try:
    pop(s)
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('implement_5 success')
  # Test end

def implement_6():
  """
    Implement a stack by a singly-linked list.
  """
  # Implement start
  class Stack(object):
    class Node(object):
      def __init__(self, data=None):
        self.data = data
        self.nxt = None

    def __init__(self):
      self.top = Stack.Node() # top is a dummy node, its nxt is the first node (head).

    def is_empty(self):
      return self.top.nxt is None

    def push(self, x):
      new_head = Stack.Node(x)
      new_head.nxt = self.top.nxt
      self.top.nxt = new_head
      
    def pop(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element exists.')
      res = self.top.nxt.data
      self.top.nxt = self.top.nxt.nxt
      return res

    def get_top(self):
      return self.top.nxt.data
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    s.push(i)
  assert s.get_top() == 2
  res = []
  for i in range(3):
    res.append(s.pop())

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')

  print('implement_6 success')
  # Test end

def main():
  implement_1()
  implement_2()
  implement_3()
  implement_4()
  implement_5()
  implement_6()

if __name__ == '__main__':
  main()
