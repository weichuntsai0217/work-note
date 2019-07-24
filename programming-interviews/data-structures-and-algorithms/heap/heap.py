"""
  Use python 3.6.8
"""
"""
  # What is a heap?
  A heap is a complete (ref 2.) binary tree which satisfies a heap property. 
  There are 2 kind of heap properties, that is max heap property and min heap property.
  The max heap property satisfies that the key at each node is greater than
  or equal to the keys stored at its children.
  The min heap property satisfies that the key at each node is less than
  or equal to the keys stored at its children.

  # What is a priority queue?
  A priority queue is a data structure in which each element has a "priority" associated with it.
  A heap is a great way to implement a priority queue. 

  # How to implement a heap?
  A heap should support methods:
  (assume `n` is the length of the heap nodes)
  * `heapify` with O(log(n)) time complexity.
  * `build_heap` with O(n) time complexity.
  * `heap_sort` with O(n * log(n)) time complexity.
  * `get_first` with O(1) time complexity, this is for `priority queue` usage.
  * `pop_first` with O(log(n)) time complexity, this is for `priority queue` usage.
  * `increase` with O(log(n)) time complexity, this is for `priority queue` usage.
  * `insert` with O(log(n)) time complexity, this is for `priority queue` usage.
  

  # References
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Adnan Aziz et al., "Elements of Programming Interviews in Python - The Insiders' Guide" (2018).

  # Notes
  ## Building a heap using insertion (problem 6-1 on page 166 of ref. 1)
  We can build a heap by repeatedly calling `insert` to insert the elements into the heap. However,
  1. this procedure can not always create the same heap as `build_heap`.
     For a demo, please refer to the code in `problem_6_1_demo`
  2. the time complexity is O(n * log(n)), not O(n) in `build_heap`.

  ## Ambiguity term comparison (full, perfect, complete)
  Here is a quick summary
  * "full binary tree" in ref. 1 and ref. 2 are the same
  * "complete binary tree" in ref. 1 is perfect binary tree in ref. 2.
  * "perfect binary tree" is not mentioned in ref. 1.
  Original descriptions from ref. 1 and ref 2. are as follows:
  * "full binary tree" in ref. 1 and ref. 2 are the same:
    - page 430 of ref. 1: a full binary tree is a binary tree in which every nonleaf node has two children.
    - page 119 of ref. 2: a full binary tree is a binary tree in which every node other than the leaves has two children
  * "perfect binary tree" in ref. 1 and ref. 2 are different:
    - we don't find out this term in ref. 1.
    - page 119 of ref. 2: a perfect binary tree is full binary tree in which all leaves are at the same depth, and in
      which every parent has two children
  * "complete binary tree" in ref. 1 and ref. 2 are different:
    - page 1179 of ref. 1: A complete k-ary tree is a k-ary tree in which all leaves have the same depth and all
      internal nodes have degree k.
    - page 119 of ref. 2: a complete binary tree is a binary tree in which every level, except possibly the last,
      is completely filled, and all nodes are as far left as possible (in the last level).
"""

def use_default_module_1():
  """
    Python default module `heapq` is actually a collection of min-heap functions.
    The heap data itself is just an array and we call it `nodes`.
    1. Use `heapq.heapify(nodes)` as a min-heap version of `build_heap(nodes)`.
    2. Use `heapq.heappush(nodes, key)` as a min-heap version of `insert(nodes, key)`.
    3. Use `heapq.heappop(nodes)` as a min-heap version of `pop_first(nodes)`.
    4. Use `heapq.heappushpop(nodes)` as a min-heap version of doing `insert` then doing `pop_first`
    5. Use `heapq.heapreplace(nodes)` as a min-heap version of doing `pop_first` then doing `insert`
    6. Use `nodes[0]` as a min-heap version of `get_first(nodes)`
    
    There are two functions in `heapq` which are useful:
    (assume `array` is not a heap data but an array with any ordering, `k` is an non-negative integer,
     and `n` be the length of the `array`)
    1. Use `heapq.nlargest(k, array)` to get the k largest elements in `array`, the time complexity is O(n * log(k)).
    2. Use `heapq.nsmallest(k, array)` to get the k smallest elements in `array`, the time complexity is O(n * log(k)).
  """
  # Implement start
  import heapq
  def heap_sorted(array):
    """
      Here I don't mutate the original array.
    """
    h = []
    for i in array:
      heapq.heappush(h, i)
    return [ heapq.heappop(h) for i in range(len(h)) ]
  # Implement end

  # Test start
  nodes = [5, 4, 1, 0, 3, 2]
  heapq.heapify(nodes)
  assert nodes == [0, 3, 1, 4, 5, 2]

  nodes = [5, 4, 1, 0, 3, 2]
  for i in range(6):
    heapq.heapify(nodes)
    assert nodes == [0, 3, 1, 4, 5, 2]

  nodes = [5, 4, 1, 0, 3, 2]
  res = heap_sorted(nodes)
  assert res == list(range(6))

  heap_src = [10, 40, 20, 50, 60, 30] # this is already a heap.

  nodes = heap_src[:]
  heapq.heappush(nodes, 70)
  assert nodes == [10, 40, 20, 50, 60, 30, 70]

  nodes = heap_src[:]
  heapq.heappush(nodes, 0)
  assert nodes == [0, 40, 10, 50, 60, 30, 20]


  nodes = heap_src[:]
  heapq.heappush(nodes, 15)
  assert nodes == [10, 40, 15, 50, 60, 30, 20]

  nodes = []
  for key in [40, 30, 20, 50, 10, 60]:
    heapq.heappush(nodes, key)
  assert nodes == [10, 20, 30, 50, 40, 60]

  nodes = heap_src[:]
  assert nodes[0] == 10
  assert nodes == heap_src

  nodes = heap_src[:]
  res = heapq.heappop(nodes)
  assert res == 10
  assert nodes == [20, 40, 30, 50, 60] 

  res = heapq.heappop(nodes)
  assert res == 20
  assert nodes == [30, 40, 60, 50] 
  print('use_default_module_1 success')

  array = [4, 1, 3, 2, 0, 5]
  """
    For `heapq.nlargest` and `heapq.nsmallest`, you don't need to input a heap data,
    any array with any ordering is OK.
  """
  assert heapq.nlargest(3, array) == [5, 4, 3]
  assert heapq.nsmallest(3, array) == [0, 1, 2]

  # Test end

def use_class_1():
  """
    Here we implement a collection of max-heap functions based on chapter 6 of ref. 1.
    The heap data itself is just an array and we call it `nodes`.
    All functions are wrapped in a `Heap` class.
  """
  # Implement start
  class Heap(object):
    @staticmethod
    def left(i): # i >= 0
      return 2 * i + 1

    @staticmethod
    def right(i): # i >= 0
      return 2 * i + 2

    @staticmethod
    def parent(i):
      return int((i - 1) / 2) # int would round down a float into an integer.

    @staticmethod
    def first_leaf(nodes):
      return int(len(nodes) / 2)

    @staticmethod
    def last_parent(nodes):
      return Heap.first_leaf(nodes) - 1

    @staticmethod
    def heapify(nodes, i, heap_len=None):
      """
        The time complexity is O(log(n)) where n is the length of heap nodes.
        When `heapify` is called, `heapify` assumes that the binary trees rooted at `left(i)` and `right(i)`
        are max-heaps, but that `nodes[i]` might be smaller than its children, thus violating the max-heap property.
        `heapify` lets the value at position `i` "float down" (like doing bubble sort down to bottom) in the max-heap 
        so that the subtree rooted at index i obeys the max-heap property.
      """
      if not isinstance(heap_len, int):
        heap_len = len(nodes)
      l = Heap.left(i)
      r = Heap.right(i)
      largest = i
      if l < heap_len and nodes[l] > nodes[largest]:
        largest = l
      if r < heap_len and nodes[r] > nodes[largest]:
        largest = r
      if largest != i:
        nodes[i], nodes[largest] = nodes[largest], nodes[i]
        Heap.heapify(nodes, largest, heap_len)

    @staticmethod
    def build_heap(nodes):
      """
        The time complexity is O(n) where n is the length of heap nodes.
        For the proof of this time complexity, please refer to page 159 of ref. 1. 
      """
      for i in range(Heap.last_parent(nodes), -1, -1):
        Heap.heapify(nodes, i)

    @staticmethod
    def heap_sort(nodes):
      """
        The time complexity is O(n * log(n)) where n is the length of heap nodes.
      """
      Heap.build_heap(nodes)
      heap_len = len(nodes)
      for i in range(len(nodes) - 1, 0, -1):
        nodes[i], nodes[0] = nodes[0], nodes[i]
        heap_len = heap_len - 1
        Heap.heapify(nodes, 0, heap_len)

    @staticmethod
    def get_first(nodes):
      """
        The time complexity is O(1).
        "first" means priority one.
      """
      return nodes[0]

    @staticmethod
    def pop_first(nodes): # first means priority one
      """
        The time complexity is O(log(n)) where n is the length of heap nodes.
        "first" means priority one.
      """
      nodes[0], nodes[-1] = nodes[-1], nodes[0]
      res = nodes.pop()
      Heap.heapify(nodes, 0)
      return res

    @staticmethod
    def increase(nodes, i, key):
      """
        The time complexity is O(log(n)) where n is the length of heap nodes.
        `increase` increases the value at position `i` into `key`.
        and lets this value "float up" (like doing bubble sort up to top) in the max-heap.
      """
      if key < nodes[i]:
        raise ValueError('New key is smaller than current key.')
      nodes[i] = key
      while i > 0 and nodes[Heap.parent(i)] < nodes[i]:
        nodes[i], nodes[Heap.parent(i)] = nodes[Heap.parent(i)], nodes[i]
        i = Heap.parent(i)

    @staticmethod
    def insert(nodes, key):
      """
        The time complexity is O(log(n)) where n is the length of heap nodes.
      """
      nodes.append(-float('inf'))
      Heap.increase(nodes, len(nodes) - 1, key)
  # Implement end

  # Test start
  nodes = [0, 5, 4, 3, 2, 1]
  for i in range(6):
    Heap.heapify(nodes, i)
    assert nodes == [5, 3, 4, 0, 2, 1]

  nodes = [0, 2, 3, 1, 5, 4]
  Heap.build_heap(nodes)
  assert nodes == [5, 2, 4, 1, 0, 3]

  nodes = [5, 2, 4, 1, 0, 3]
  Heap.heap_sort(nodes)
  assert nodes == list(range(6))

  heap_src = [60, 50, 30, 40, 20, 10] # already a heap
  
  nodes = heap_src[:]
  Heap.increase(nodes, 5, 70)
  assert nodes == [70, 50, 60, 40, 20, 30]
  
  nodes = heap_src[:]
  Heap.increase(nodes, 0, 70)
  assert nodes == [70, 50, 30, 40, 20, 10]

  nodes = heap_src[:]
  Heap.increase(nodes, 1, 70)
  assert nodes == [70, 60, 30, 40, 20, 10]

  nodes = heap_src[:]
  Heap.increase(nodes, 4, 55)
  assert nodes == [60, 55, 30, 40, 50, 10]

  nodes = heap_src[:]
  Heap.insert(nodes, 0)
  assert nodes == [60, 50, 30, 40, 20, 10, 0]

  nodes = heap_src[:]
  Heap.insert(nodes, 70)
  assert nodes == [70, 50, 60, 40, 20, 10, 30]

  nodes = heap_src[:]
  Heap.insert(nodes, 55)
  assert nodes == [60, 50, 55, 40, 20, 10, 30]

  nodes = []
  for key in [40, 30, 20, 50, 10, 60]:
    Heap.insert(nodes, key)
  assert nodes == [60, 40, 50, 30, 10, 20]

  nodes = heap_src[:]
  assert Heap.get_first(nodes) == 60
  assert nodes == heap_src

  nodes = heap_src[:]
  res = Heap.pop_first(nodes)
  assert res == 60
  assert nodes == [50, 40, 30, 10, 20] 

  res = Heap.pop_first(nodes)
  assert res == 50
  assert nodes == [40, 20, 30, 10] 


  def problem_6_1_demo():
    a = [3, 2, 1, 4, 5]
    Heap.build_heap(a)
    assert a == [5, 4, 1, 3, 2]

    b = [3, 2, 1, 4, 5]
    res = []
    for x in b:
      Heap.insert(res, x)
    assert res == [5, 4, 1, 2, 3]
    assert res != b # the result is not the same

  problem_6_1_demo()

  print('use_class_1 success')
  # Test end


def main():
  use_default_module_1()
  use_class_1()

if __name__ == '__main__':
  main()
