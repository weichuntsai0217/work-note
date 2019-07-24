"""
  Use python 3.6.8
"""
"""
  What is a queue?
  A queue is a data structure which follows the first-in first-out policy to manage a collection of data.

  How to implement a quene?
  A queue should support methods:
  1. `is_empty` with O(1) time complexity.
  2. `enqueue` with O(1) time complexity.
  3. `dequeue` with O(1) time complexity.
  4. `get_first` with O(1) time complexity.
  5. (optional) `get_len` with O(1) time complexity.
  6. (optional) `is_max` with O(1) time complexity.
  7. (optional) `get_maxlen` with O(1) time complexity.

  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).
  3. Adnan Aziz et al., "Elements of Programming Interviews in Python - The Insiders' Guide" (2018).
"""

def use_default_module_1():
  """
    Python default module `collections.deque` is actually can be a queue.
    If `q = collections.deque()`, then 
    1. Use `len(q) == 0` as `is_empty`.
    2. Use `q.append` as `enqueue`.
    3. Use `q.popleft` as `dequeue`.
    4. Use `q[0]` as `get_first`
    5. Use `len(q)` as `get_len`
  """
  # Implement start
  import collections
  class Queue(collections.deque):
    pass
  # Implement end

  # Test start
  q = Queue()
  for i in range(3):
    q.append(i)
  assert len(q) == 3
  assert q[0] == 0

  res = []
  for i in range(3):
    res.append(q.popleft())
    assert len(q) == 2 - i
  assert res == [0, 1, 2]

  assert len(q) == 0

  check_error = False
  try:
    q.popleft()
  except IndexError:
    check_error = True
  assert check_error == True

  print('use_default_module_1 success')
  # Test end

def use_class_1():
  """
    Implement a circular queue with fixed length by a class in C/C++ style.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++

    def is_empty(self):
      return self.length == 0

    def enqueue(self, x):
      if self.is_max():
        raise IndexError('The queue is full and cannot enqueue any item.')
      self.data[self.tail] = x
      if (self.tail + 1) == self.get_maxlen():
        self.tail = 0
      else:
        self.tail += 1
      self.length += 1

    def dequeue(self):
      if self.is_empty():
        raise IndexError('The queue is empty and cannot be dequeued.')
      res = self.data[self.head]
      if (self.head + 1) == self.get_maxlen():
        self.head = 0
      else:
        self.head += 1
      self.length -= 1
      return res

    def get_first(self):
      return self.data[self.head]

    def get_len(self):
      return self.length

    def is_max(self):
      return self.get_len() == self.get_maxlen()

    def get_maxlen(self):
      return len(self.data)
  # Implement end

  # Test start
  q = Queue(4)
  assert q.get_maxlen() == 4
  for i in range(3):
    q.enqueue(i)
  assert q.get_len() == 3
  assert q.get_first() == 0

  res = []
  for i in range(3):
    res.append(q.dequeue())
    assert q.get_len() == 2 - i
  assert res == [0, 1, 2]

  assert q.get_len() == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    q.dequeue()
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    q.enqueue(i)
  assert q.head == 3
  assert q.tail == 2

  q.enqueue(3)
  assert q.data == [1, 2, 3, 0]
  check_error = False
  try:
    q.enqueue('a')
  except IndexError:
    check_error = True
  assert check_error == True

  res = []
  for i in range(2):
    res.append(q.dequeue())
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  print('use_class_1 success')
  # Test end

def use_funcs_1():
  """
    Implement a circular queue with fixed length by functions in C/C++ style.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++

  def is_empty(q):
    return q.length == 0

  def enqueue(q, x):
    if is_max(q):
      raise IndexError('The queue is full and cannot enqueue any item.')
    q.data[q.tail] = x
    if (q.tail + 1) == get_maxlen(q):
      q.tail = 0
    else:
      q.tail += 1
    q.length += 1

  def dequeue(q):
    if is_empty(q):
      raise IndexError('The queue is empty and cannot be dequeued.')
    res = q.data[q.head]
    if (q.head + 1) == get_maxlen(q):
      q.head = 0
    else:
      q.head += 1
    q.length -= 1
    return res

  def get_first(q):
    return q.data[q.head]

  def get_len(q):
    return q.length

  def is_max(q):
    return get_len(q) == get_maxlen(q)

  def get_maxlen(q):
    return len(q.data)
  # Implement end

  # Test start
  q = Queue(4)
  assert get_maxlen(q) == 4
  for i in range(3):
    enqueue(q, i)
  assert get_len(q) == 3
  assert get_first(q) == 0

  res = []
  for i in range(3):
    res.append(dequeue(q))
    assert get_len(q) == 2 - i
  assert res == [0, 1, 2]

  assert get_len(q) == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    dequeue(q)
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    enqueue(q, i)
  assert q.head == 3
  assert q.tail == 2

  enqueue(q, 3)
  assert q.data == [1, 2, 3, 0]
  check_error = False
  try:
    enqueue(q, 'a')
  except IndexError:
    check_error = True
  assert check_error == True

  res = []
  for i in range(2):
    res.append(dequeue(q))
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  print('use_funcs_1 success')
  # Test end

def use_class_2():
  """
    Implement a circular queue with dynamic length by a class in C/C++ style.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen=4):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++
      self.scale = 2

    def is_empty(self):
      return self.length == 0

    def enqueue(self, x):
      if self.is_max():
        self.allocate_mem_and_rotate_data()
      self.data[self.tail] = x
      if (self.tail + 1) == self.get_maxlen():
        self.tail = 0
      else:
        self.tail += 1
      self.length += 1

    def dequeue(self):
      if self.is_empty():
        raise IndexError('The queue is empty and cannot be dequeued.')
      res = self.data[self.head]
      if (self.head + 1) == self.get_maxlen():
        self.head = 0
      else:
        self.head += 1
      self.length -= 1
      return res

    def get_first(self):
      return self.data[self.head]

    def get_len(self):
      return self.length

    def is_max(self):
      return self.get_len() == self.get_maxlen()

    def get_maxlen(self):
      return len(self.data)

    def allocate_mem_and_rotate_data(self):
      new_data = [None] * (self.get_maxlen() * self.scale)
      src_idx = self.head
      for dst_idx in range(self.get_maxlen()):
        new_data[dst_idx] = self.data[src_idx]
        if (src_idx + 1) == self.get_maxlen():
          src_idx = 0
        else:
          src_idx += 1
      self.head = 0
      self.tail = self.get_maxlen()
      self.data = new_data
  # Implement end

  # Test start
  q = Queue()
  assert q.get_maxlen() == 4
  for i in range(3):
    q.enqueue(i)
  assert q.get_len() == 3
  assert q.get_first() == 0

  res = []
  for i in range(3):
    res.append(q.dequeue())
    assert q.get_len() == 2 - i
  assert res == [0, 1, 2]

  assert q.get_len() == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    q.dequeue()
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    q.enqueue(i)
  assert q.head == 3
  assert q.tail == 2

  q.enqueue(3)
  assert q.data == [1, 2, 3, 0]

  res = []
  for i in range(2):
    res.append(q.dequeue())
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  q.enqueue(1)
  q.enqueue(4)
  assert q.data == [4, 2, 3, 1]
  q.enqueue(5)
  assert q.data == [2, 3, 1, 4, 5, None, None, None]

  print('use_class_2 success')
  # Test end

def use_funcs_2():
  """
    Implement a circular queue with dynamic length by functions in C/C++ style.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen=4):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++
      self.scale = 2

  def is_empty(q):
    return q.length == 0

  def enqueue(q, x):
    if is_max(q):
      allocate_mem_and_rotate_data(q)
    q.data[q.tail] = x
    if (q.tail + 1) == get_maxlen(q):
      q.tail = 0
    else:
      q.tail += 1
    q.length += 1

  def dequeue(q):
    if is_empty(q):
      raise IndexError('The queue is empty and cannot be dequeued.')
    res = q.data[q.head]
    if (q.head + 1) == get_maxlen(q):
      q.head = 0
    else:
      q.head += 1
    q.length -= 1
    return res

  def get_first(q):
    return q.data[q.head]

  def get_len(q):
    return q.length

  def is_max(q):
    return get_len(q) == get_maxlen(q)

  def get_maxlen(q):
    return len(q.data)

  def allocate_mem_and_rotate_data(q):
    new_data = [None] * (get_maxlen(q) * q.scale)
    src_idx = q.head
    for dst_idx in range(get_maxlen(q)):
      new_data[dst_idx] = q.data[src_idx]
      if (src_idx + 1) == get_maxlen(q):
        src_idx = 0
      else:
        src_idx += 1
    q.head = 0
    q.tail = get_maxlen(q)
    q.data = new_data
  # Implement end

  # Test start
  q = Queue()
  assert get_maxlen(q) == 4
  for i in range(3):
    enqueue(q, i)
  assert get_len(q) == 3
  assert get_first(q) == 0

  res = []
  for i in range(3):
    res.append(dequeue(q))
    assert get_len(q) == 2 - i
  assert res == [0, 1, 2]

  assert get_len(q) == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    dequeue(q)
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    enqueue(q, i)
  assert q.head == 3
  assert q.tail == 2

  enqueue(q, 3)
  assert q.data == [1, 2, 3, 0]

  res = []
  for i in range(2):
    res.append(dequeue(q))
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  enqueue(q, 1)
  enqueue(q, 4)
  assert q.data == [4, 2, 3, 1]
  enqueue(q, 5)
  assert q.data == [2, 3, 1, 4, 5, None, None, None]

  print('use_funcs_2 success')
  # Test end

def use_class_3():
  """
    Implement a queue by using stacks based on a class.
    When the interviewer gives this test, the most important part is `enqueue` and `dequeue`,
    please feel free to skip `is_empty`, `get_first`, and `get_len`, and basically there
    is no need to limit the queue length is fixed.
  """
  # Implement start
  class Queue(object):
    def __init__(self):
      self.enq = []
      self.deq = []

    def enqueue(self, item):
      """ 
        The time complexity is O(1)
      """
      self.enq.append(item)

    def dequeue(self):
      """ 
        The amortized time complexity is O(1).
        Why O(1) ? Let's assume the queue is empty at first, then you push k items in the queue (push k times)
        then you want to pop k items. But now `self.deq` is empty so you have to pop `self.enq` k times and push
        these k items into `self.deq`, and finally you have to pop k times from `self.deq`. In the above process,
        you do 4*k times operation on k items, so each item take 4k/k = 4 times operation, that is O(4) = O(1)
      """
      if self.is_empty():
        raise IndexError('This queue is empty and dequeue failed.')
      if not self.deq:
        while self.enq:
          self.deq.append(self.enq.pop())
      return self.deq.pop()

    def get_len(self):
      return len(self.enq) + len(self.deq)

    def is_empty(self):
      return self.get_len() == 0

    def get_first(self):
      if self.is_empty():
        raise IndexError('This queue is empty and dequeue failed.')
      if not self.deq:
        while self.enq:
          self.deq.append(self.enq.pop())
      return self.deq[-1]
  # Implement end

  # Test start
  q = Queue()
  for i in range(3):
    q.enqueue(i)
  assert q.get_len() == 3
  assert q.get_first() == 0

  res = []
  for i in range(3):
    res.append(q.dequeue())
    assert q.get_len() == 2 - i
  assert res == [0, 1, 2]

  assert q.get_len() == 0

  check_error = False
  try:
    q.dequeue()
  except IndexError:
    check_error = True
  assert check_error == True

  print('use_class_3 success')
  # Test end
  
def use_funcs_3():
  """
    Implement a queue by using stacks based on functions.
    When the interviewer gives this test, the most important part is `enqueue` and `dequeue`,
    please feel free to skip `is_empty`, `get_first`, and `get_len`, and basically there
    is no need to limit the queue length is fixed.
  """
  # Implement start
  class Queue(object):
    def __init__(self):
      self.enq = []
      self.deq = []

  def enqueue(q, item):
    """ 
      The time complexity is O(1)
    """
    q.enq.append(item)

  def dequeue(q):
    """ 
      The amortized time complexity is O(1).
      Please refer to `use_class_3` for details.
    """
    if is_empty(q):
      raise IndexError('This queue is empty and dequeue failed.')
    if not q.deq:
      while q.enq:
        q.deq.append(q.enq.pop())
    return q.deq.pop()

  def get_len(q):
    return len(q.enq) + len(q.deq)

  def is_empty(q):
    return get_len(q) == 0

  def get_first(q):
    if is_empty(q):
      raise IndexError('This queue is empty and dequeue failed.')
    if not q.deq:
      while q.enq:
        q.deq.append(q.enq.pop())
    return q.deq[-1]
  # Implement end

  # Test start
  q = Queue()
  for i in range(3):
    enqueue(q, i)
  assert get_len(q) == 3
  assert get_first(q) == 0

  res = []
  for i in range(3):
    res.append(dequeue(q))
    assert get_len(q) == 2 - i
  assert res == [0, 1, 2]

  assert get_len(q) == 0

  check_error = False
  try:
    dequeue(q)
  except IndexError:
    check_error = True
  assert check_error == True

  print('use_funcs_3 success')
  # Test end

def use_class_4():
  """
    Implement a circular queue with fixed length like `collections.deque` by a class in C/C++ style.
    This means that when this circular queue is full and want to enqueues,
    it would evict the earliest (oddest) item automatically.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++

    def is_empty(self):
      return self.length == 0

    def enqueue(self, x):
      if self.is_max():
        self.dequeue()
      self.data[self.tail] = x
      if (self.tail + 1) == self.get_maxlen():
        self.tail = 0
      else:
        self.tail += 1
      self.length += 1

    def dequeue(self):
      if self.is_empty():
        raise IndexError('The queue is empty and cannot be dequeued.')
      res = self.data[self.head]
      if (self.head + 1) == self.get_maxlen():
        self.head = 0
      else:
        self.head += 1
      self.length -= 1
      return res

    def get_first(self):
      return self.data[self.head]

    def get_len(self):
      return self.length

    def is_max(self):
      return self.get_len() == self.get_maxlen()

    def get_maxlen(self):
      return len(self.data)
  # Implement end

  # Test start
  q = Queue(4)
  assert q.get_maxlen() == 4
  for i in range(3):
    q.enqueue(i)
  assert q.get_len() == 3
  assert q.get_first() == 0

  res = []
  for i in range(3):
    res.append(q.dequeue())
    assert q.get_len() == 2 - i
  assert res == [0, 1, 2]

  assert q.get_len() == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    q.dequeue()
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    q.enqueue(i)
  assert q.head == 3
  assert q.tail == 2

  q.enqueue(3)
  assert q.data == [1, 2, 3, 0]

  res = []
  for i in range(2):
    res.append(q.dequeue())
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  for i in range(4, 7):
    q.enqueue(i)
  assert q.data == [5, 6, 3, 4]
  assert q.head == 2
  assert q.tail == 2
  assert q.get_len() == 4

  for i in range(7, 9):
    q.enqueue(i)
  assert q.data == [5, 6, 7, 8]
  assert q.head == 0
  assert q.tail == 0
  assert q.get_len() == 4

  res = []
  for i in range(q.get_len()):
    res.append(q.dequeue())
  assert res == [5,6,7,8]

  print('use_class_4 success')
  # Test end

def use_funcs_4():
  """
    Implement a circular queue with fixed length like `collections.deque` by functions in C/C++ style.
    This means that when this circular queue enqueues and this queue is full,
    it would evict the earliest (oddest) item automatically.
  """
  # Implement start
  class Queue(object):
    def __init__(self, maxlen):
      self.head = 0
      self.tail = 0
      self.length = 0
      self.data = [None] * maxlen # mimic memory allocation like C/C++

  def is_empty(q):
    return q.length == 0

  def enqueue(q, x):
    if is_max(q):
      dequeue(q)
    q.data[q.tail] = x
    if (q.tail + 1) == get_maxlen(q):
      q.tail = 0
    else:
      q.tail += 1
    q.length += 1

  def dequeue(q):
    if is_empty(q):
      raise IndexError('The queue is empty and cannot be dequeued.')
    res = q.data[q.head]
    if (q.head + 1) == get_maxlen(q):
      q.head = 0
    else:
      q.head += 1
    q.length -= 1
    return res

  def get_first(q):
    return q.data[q.head]

  def get_len(q):
    return q.length

  def is_max(q):
    return get_len(q) == get_maxlen(q)

  def get_maxlen(q):
    return len(q.data)
  # Implement end

  # Test start
  q = Queue(4)
  assert get_maxlen(q) == 4
  for i in range(3):
    enqueue(q, i)
  assert get_len(q) == 3
  assert get_first(q) == 0

  res = []
  for i in range(3):
    res.append(dequeue(q))
    assert get_len(q) == 2 - i
  assert res == [0, 1, 2]

  assert get_len(q) == 0
  assert q.head == 3
  assert q.tail == 3

  check_error = False
  try:
    dequeue(q)
  except IndexError:
    check_error = True
  assert check_error == True

  for i in range(3):
    enqueue(q, i)
  assert q.head == 3
  assert q.tail == 2

  enqueue(q, 3)
  assert q.data == [1, 2, 3, 0]

  res = []
  for i in range(2):
    res.append(dequeue(q))
  assert res == [0, 1]
  assert q.head == 1
  assert q.tail == 3

  for i in range(4, 7):
    enqueue(q, i)
  assert q.data == [5, 6, 3, 4]
  assert q.head == 2
  assert q.tail == 2
  assert get_len(q) == 4

  for i in range(7, 9):
    enqueue(q, i)
  assert q.data == [5, 6, 7, 8]
  assert q.head == 0
  assert q.tail == 0
  assert get_len(q) == 4

  res = []
  for i in range(get_len(q)):
    res.append(dequeue(q))
  assert res == [5,6,7,8]

  print('use_funcs_4 success')
  # Test end

def main():
  use_default_module_1()
  use_class_1()
  use_funcs_1()
  use_class_2()
  use_funcs_2()
  use_class_3()
  use_funcs_3()
  use_class_4()
  use_funcs_4()

if __name__ == '__main__':
  main()

