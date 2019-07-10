"""
  Use python 3.6.8
"""
"""
  What is a stack?
  A stack is a data structure which follows the last-in, first-out policy to manage a collection of data.

  How to implement a stack?
  A stack should support methods:
  1. `is_empty` with O(1) time complexity
  2. `push` with O(1) time complexity
  3. `pop` with O(1) time complexity
  4. `get_top` with O(1) time complexity
  5. (optional) `get_len` with O(1) time complexity
  6. (optional) `is_max` with O(1) time complexity
  7. (optional) `get_maxlen` with O(1) time complexity

  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).
"""

def use_built_in_1():
  """
    Python built-in list is actually can be a stack.
    If `s = list()`, then
    1. Use `len(s) == 0` as `is_empty`.
    2. Use `s.append` as `push`.
    3. Use `s.pop` as `pop`.
    4. Use `s[-1]` as `get_top`.
    5. Use `len(s)` as `get_len`.
  """
  # Implement start
  class Stack(list):
    pass
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    s.append(i)
  assert len(s) == 3
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
    
  print('use_built_in_1 success')
  # Test end

def use_class_1():
  """
    Implement a stack with fixed length by a class in C/C++ array style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen):
      self.top = -1
      self.data = [None] * maxlen # mimic C/C++ style to allocate a fixed-length array.

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

    def get_len(self):
      return self.top + 1

    def is_max(self):
      return self.get_len() == self.get_maxlen()

    def get_maxlen(self):
      return len(self.data)
  # Implement end

  # Test start
  s = Stack(10)
  assert s.get_maxlen() == 10
  for i in range(3):
    s.push(i)
    assert s.top == i
  assert s.get_len() == 3
  assert s.get_top() == 2
  res = []
  for i in range(3):
    res.append(s.pop())
    assert s.get_len() == (2 - i)

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('use_class_1 success')
  # Test end

def use_funcs_1():
  """
    Implement a stack with fixed length by a stack data and other functions in C/C++ array style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen):
      self.top = -1
      self.data = [None] * maxlen # mimic C/C++ style to allocate a fixed-length array.

  def is_empty(s):
    return s.top == -1

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

  def get_len(s):
    return s.top + 1

  def is_max(s):
    return get_len(s) == get_maxlen(s)

  def get_maxlen(s):
    return len(s.data)
  # Implement end

  # Test start
  s = Stack(10)
  assert get_maxlen(s) == 10
  for i in range(3):
    push(s, i)
    assert s.top == i
  assert get_len(s) == 3
  assert get_top(s) == 2
  res = []
  for i in range(3):
    res.append(pop(s))
    assert get_len(s) == 2 - i

  check_error = False
  try:
    pop(s)
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  print('use_funcs_1 success')
  # Test end

def use_class_2():
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
      self.length = 0

    def is_empty(self):
      return self.top.nxt is None

    def push(self, x):
      new_head = Stack.Node(x)
      new_head.nxt = self.top.nxt
      self.top.nxt = new_head
      self.length += 1
      
    def pop(self):
      if self.is_empty():
        raise IndexError('The stack is empty. No element exists.')
      res = self.top.nxt.data
      self.top.nxt = self.top.nxt.nxt
      self.length -= 1
      return res

    def get_top(self):
      return self.top.nxt.data

    def get_len(self):
      return self.length
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    s.push(i)
  assert s.get_len() == 3
  assert s.get_top() == 2
  res = []
  for i in range(3):
    res.append(s.pop())
    assert s.get_len() == 2 - i

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')

  print('use_class_2 success')
  # Test end

def use_funcs_2():
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
      self.length = 0

  def is_empty(s):
    return s.top.nxt is None

  def push(s, x):
    new_head = Stack.Node(x)
    new_head.nxt = s.top.nxt
    s.top.nxt = new_head
    s.length += 1
    
  def pop(s):
    if is_empty(s):
      raise IndexError('The stack is empty. No element exists.')
    res = s.top.nxt.data
    s.top.nxt = s.top.nxt.nxt
    s.length -= 1
    return res

  def get_top(s):
    return s.top.nxt.data

  def get_len(s):
    return s.length
  # Implement end

  # Test start
  s = Stack()
  for i in range(3):
    push(s, i)
  assert get_len(s) == 3
  assert get_top(s) == 2
  res = []
  for i in range(3):
    res.append(pop(s))
    assert get_len(s) == 2 - i

  check_error = False
  try:
    pop(s)
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')

  print('use_funcs_2 success')
  # Test end

def use_class_3():
  """
    Implement a stack with dynamic length by a class in C/C++ array style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen=4):
      self.top = -1
      self.data = [None] * maxlen # mimic C/C++ style to allocate a fixed-length array.
      self.scale = 2

    def is_empty(self):
      return self.top == -1

    def push(self, x):
      if self.is_max():
        self.allocate_mem()
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

    def get_len(self):
      return self.top + 1

    def is_max(self):
      return self.get_len() == self.get_maxlen()

    def get_maxlen(self):
      return len(self.data)

    def allocate_mem(self):
      new_data = [None] * (self.get_maxlen() * self.scale)
      for i in range(self.get_maxlen()):
        new_data[i] = self.data[i]
      self.data = new_data

  # Implement end

  # Test start
  s = Stack()
  assert s.get_maxlen() == 4
  for i in range(3):
    s.push(i)
    assert s.top == i
  assert s.get_len() == 3
  assert s.get_top() == 2
  res = []
  for i in range(3):
    res.append(s.pop())
    assert s.get_len() == (2 - i)

  check_error = False
  try:
    s.pop()
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  for i in range(6):
    s.push(i)
    assert s.top == i
  assert s.get_maxlen() == 8
  assert s.get_len() == 6
  assert s.get_top() == 5

  print('use_class_3 success')
  # Test end

def use_funcs_3():
  """
    Implement a stack with dynamic length by functions in C/C++ array style.
  """
  # Implement start
  class Stack(object):
    def __init__(self, maxlen=4):
      self.top = -1
      self.data = [None] * maxlen # mimic C/C++ style to allocate a fixed-length array.
      self.scale = 2

  def is_empty(s):
    return s.top == -1

  def push(s, x):
    if is_max(s):
      allocate_mem(s)
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

  def get_len(s):
    return s.top + 1

  def is_max(s):
    return get_len(s) == get_maxlen(s)

  def get_maxlen(s):
    return len(s.data)

  def allocate_mem(s):
    new_data = [None] * (get_maxlen(s) * s.scale)
    for i in range(get_maxlen(s)):
      new_data[i] = s.data[i]
    s.data = new_data
  # Implement end

  # Test start
  s = Stack()
  assert get_maxlen(s) == 4
  for i in range(3):
    push(s, i)
    assert s.top == i
  assert get_len(s) == 3
  assert get_top(s) == 2
  res = []
  for i in range(3):
    res.append(pop(s))
    assert get_len(s) == (2 - i)

  check_error = False
  try:
    pop(s)
  except IndexError:
    check_error = True
  assert res == [2, 1, 0]
  if not check_error:
    raise RuntimeError('The exception test is not successful.')
    
  for i in range(6):
    push(s, i)
    assert s.top == i
  assert get_maxlen(s) == 8
  assert get_len(s) == 6
  assert get_top(s) == 5

  print('use_funcs_3 success')
  # Test end

def main():
  use_built_in_1()
  use_class_1()
  use_funcs_1()
  use_class_2()
  use_funcs_2()
  use_class_3()
  use_funcs_3()

if __name__ == '__main__':
  main()
