from __future__ import print_function

class Heap(object):
  @staticmethod
  def left(i): # i >= 0
    return 2 * i + 1

  @staticmethod
  def right(i): # i >= 0
    return 2 * i + 2

  @staticmethod
  def parent(i):
    return int((i - 1) / 2) # int would round down a positive float automatically.

  @staticmethod
  def first_leaf(length):
    return int(length / 2)

  @staticmethod
  def last_parent(length):
    return Heap.first_leaf(length) - 1

  @staticmethod
  def heapify(nodes, i, comp): # if comp(node_a, node_b) return True, it means we should exchange node_a and node_b
    left = Heap.left(i)
    right = Heap.right(i)
    smallest = i
    if left < len(nodes) and comp(nodes[smallest], nodes[left]):
      smallest = left
    if right < len(nodes) and comp(nodes[smallest], nodes[right]):
      smallest = right
    if smallest != i:
      tmp = nodes[i]
      nodes[i] = nodes[smallest]
      nodes[smallest] = tmp
      Heap.heapify(nodes, smallest, comp)

  @staticmethod
  def build_heap(nodes, comp):
    """
      Time complexity is O(n) based on Page 159 of Thomas H Cormen_2009_Introduction to Algorithms 3rd 
    """
    start = Heap.last_parent(len(nodes))
    for i in xrange(start, -1, -1):
      Heap.heapify(nodes, i, comp)


  def __init__(self, nodes=None, comp=lambda a, b: a > b):
    """
      `nodes` is like `[{'v': 10}, {'v': 20}]`
      `comp` is a function with 2 args which can compare 2 nodes a and b and decide which one is less.
      if `comp(a, b)` returns True then it means a < b. `comp` can define if the heap is a min-heap or a max-heap.
    """
    self.comp = comp
    self.nodes = nodes if isinstance(nodes, list) else []
    Heap.build_heap(self.nodes, self.comp)

  def get_first_item(self): # first means priority one
    return self.nodes[0]

  def pop_first_item(self): # first means priority one
    tmp = self.nodes[0]
    self.nodes[0] = self.nodes[-1]
    self.nodes[-1] = tmp
    res = self.nodes.pop(-1)
    Heap.heapify(self.nodes, 0, self.comp)
    return res

  def increase_item(self, i, set_item):
    """
      `increase_item` means make the item closer to root. That is increase its priority.
      `set_item` must be consistent with self.comp
    """
    set_item(self.nodes, i)
    while i > 0 and self.comp(self.nodes[Heap.parent(i)], self.nodes[i]):
      prt = Heap.parent(i)
      tmp = self.nodes[prt]
      self.nodes[prt] = self.nodes[i]
      self.nodes[i] = tmp
      i = prt
      
  def insert(self, node, set_item=lambda nodes, i: None):
    self.nodes.append(node)
    self.increase_item(len(self.nodes)-1, set_item)

def heap_sort(nodes, comp=lambda a, b: a > b):
    """
      Time complexity is O(n * logn)
      Default is ascending mode.
    """
    res = []
    heap = Heap(nodes, comp)

    while len(heap.nodes) > 0:
      last_idx = len(heap.nodes) - 1
      tmp = heap.nodes[0]
      heap.nodes[0] = heap.nodes[last_idx]
      heap.nodes[last_idx] = tmp
      res.append(heap.nodes.pop(last_idx))
      Heap.heapify(heap.nodes, 0, comp)

    return res

def get_input():
  return [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def show_heap_tree(heap_nodes):
  level_start = 0
  level_end = 1
  level = 0
  res = []
  while level_start < len(heap_nodes):
    tmp = []
    real_end = level_end if level_end <= len(heap_nodes) else len(heap_nodes)
    for i in xrange(level_start, real_end):
      tmp.append(heap_nodes[i])
    res.append(tmp)
    level_start += (2**level)
    level += 1
    level_end += (2**level)
  print('heap tree:')
  for item in res:
    print(item)

def main():
  data = Heap(get_input())
  print('heap data:', data.nodes)
  show_heap_tree(data.nodes)

  res = heap_sort(get_input())
  print('ascending order:', res)

  res = heap_sort(get_input(), lambda a, b: a < b)
  print('descending order:', res)

  data = Heap(get_input())
  def set_item(nodes, i):
    nodes[i] = 0
  data.increase_item(5, set_item)
  show_heap_tree(data.nodes)

  print(data.pop_first_item())
  show_heap_tree(data.nodes)

  print('insert ===')
  data.insert(0)
  show_heap_tree(data.nodes)

if __name__ == '__main__':
  main()
