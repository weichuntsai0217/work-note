"""
  Use python 3.6.8
"""
"""
  # What is sorting?
  Sorting is a way to reorder a collection of elements from the smallest to the largest.

  # What is a stable sorting?
  We say a sorting algorithm is stable if after sorting,
  elements with the same value appear in the output array in the same order as they do in the input array.
  For example, if the input array is:
  `[(2, 'a'), (1, 'b'), (2, 'c')]`
  and we sort it by the value at index 0 of each element, then:
  if the output is [(1, 'b'), (2, 'a'), (2, 'c')], then we say the sort is stable.
  if the output is [(1, 'b'), (2, 'c'), (2, 'a')], then we say the sort is not stable.

  # Summary of sorting algorithms
  * Selection sort
    - Selection sort is to select the smallest element in the subarray and move it to the start of this subarray.
    - The implement here is `selection_sort` which follows the exercise 2.2-2 on page 29 of ref. 1.
  * Bubble sort
    - Bubble sort is to keep swapping the smaller element in adjacent pairs to the start of the array.
      The smaller element is like a bubble, it continues to float up to the start of the array.
    - The implement here is `bubble_sort` which follows the problem 2-2 on page 40 of ref. 1.
  * Insertion sort
    - Insertion sort is to insert an element into a sorted sequence.
    - The implement here is `insertion_sort` which follows the code on page 18 of ref. 1.
  * Merge sort
    - Merge sort is to divide the input array into subarrays and then merge them.
    - The implement here is `merge_sort` which follows the code on page 31 and 34 of ref. 1.
  * Heap sort
    - Heap sort is to convert an array into a heap data structure and then sort it.
    - The implement here is `heap_sort`. Most code in `heap_sort` follows the code in chapter 6 of ref. 1,
      but I change `heapify` by using a while loop to reduce the space complexity.
  * Quick sort
    - Quick sort is to divide the array by partition until the base case.
    - The implement heare is `quick_sort` which follows the code on page 171 of ref. 1.

  # Comparison for sorting algorithms
  ----------------------------------------------------------------------------------------------------------
  Algorithm      Best        Average     Worst       Memory Stable Note
  -------------- ----------- ----------- ----------- ------ ------ -----------------------------------------
  Selection sort O(n^2)      O(n^2)      O(n^2)      O(1)   No

  Bubble sort    O(n^2)      O(n^2)      O(n^2)      O(1)   Yes    The "Best" case in wikipedia is O(n) and
                                                                   is not consistent with our implement,
                                                                   because we just implement a basic version
                                                                   of bubble sort without a `swapped` flag.

  Insertion sort O(n)        O(n^2)      O(n^2)      O(1)   Yes

  Merge sort     O(n*log(n)) O(n*log(n)) O(n*log(n)) O(n)   Yes

  Heap sort      O(n)        O(n*log(n)) O(n*log(n)) O(1)   No

  Quick sort     O(n*log(n)) O(n*log(n)) n^2         O(n)   No
  ----------------------------------------------------------------------------------------------------------
  We compare time/space complexities of all implements of this file in the above table.
  "Best" means "best time complexity".
  "Average" means "average time complexity".
  "Worst" means "worst time complexity".
  "Memory" means "worst space complexity".
  For examples of worst, average, or best time complexities, please refer to the comment in each implement.

  # References
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Wikipedia for sorting algorithms: https://en.wikipedia.org/wiki/Sorting_algorithm

"""
from functools import total_ordering

def selection_sort(array):
  """
    Best case: [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]
    Average case: 
    Worst case: [4, 3, 2, 1, 0]
    Unstable case: [(0, 'z'), (2, 'a'), (2, 'b'), (1, 'c')] when sorted by the 1st(index=0) entry of each element.
  """
  for i in range(len(array) - 1):
    min_idx = i
    for j in range(i+1, len(array)):
      if array[j] < array[min_idx]:
        min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

def bubble_sort(array):
  """
    Best case: [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]
    Average case: 
    Worst case: [4, 3, 2, 1, 0]
  """
  for i in range(len(array) - 1):
    """
      elements from 0 to `i - 1` (inclusive) are kept sorted except the 1st turn of this loop.
    """
    for j in range(len(array) - 1, i, -1):
      """
      `i` is the final position of the smallest element of the subarray from `i` to `len(array) - 1` (inclusive)
      """
      if array[j - 1] > array[j]:
        array[j - 1], array[j] = array[j], array[j - 1]

def insertion_sort(array):
  """
    Best case: [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]
    Average case: 
    Worst case: [4, 3, 2, 1, 0]
  """
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i > -1 and array[i] > key:
      array[i+1] = array[i]
      i -= 1
    array[i+1] = key

def merge_sort(array, p, r, inf=float('inf')):
  """
    Best case: [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]
    Average case: 
    Worst case: [4, 3, 2, 1, 0]
  """
  """
    `inf` does not appear in the code of ref. 1, because ref. 1 focuses on showing basic principles
    and does not consider the case when elements in an array are not integers/floats but some
    complicated objects which implement their comparison operators (`__lt__`, `__eq__`, etc.).
  """
  def merge(src, p, q, r, inf=float('inf')):
    """
      The first subarray is from p ~ q (inclusive)
      and the second subarray is from q + 1 ~ r (inclusive)
      The space complexity including the output is O(r - p + 1).
    """
    left = src[p:q+1]
    left.append(inf) # use 'inf' as a sentinel to make edge case much easier
    right = src[q+1:r+1]
    right.append(inf) # use 'inf' as a sentinel to make edge case much easier
    i = 0
    j = 0
    for k in range(p, r+1):
      if left[i] <= right[j]:
        src[k] = left[i]
        i += 1
      else:
        src[k] = right[j]
        j += 1

  if p < r:
    q = int((p + r) / 2)
    merge_sort(array, p, q, inf)
    merge_sort(array, q+1, r, inf)
    merge(array, p, q, r, inf)

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
    # This is the original version of `MAX-HEAPIFY` on page 154 of ref. 1
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
    """
    # I change the implement from ref. 1's version into a while loop version to reduce the space complexity.
    if not isinstance(heap_len, int):
      heap_len = len(nodes)
    while i < heap_len:
      l = Heap.left(i)
      r = Heap.right(i)
      largest = i
      if l < heap_len and nodes[l] > nodes[largest]:
        largest = l
      if r < heap_len and nodes[r] > nodes[largest]:
        largest = r
      if largest != i:
        nodes[i], nodes[largest] = nodes[largest], nodes[i]
        i = largest
      else:
        break

  @staticmethod
  def build_heap(nodes):
    for i in range(Heap.last_parent(nodes), -1, -1):
      Heap.heapify(nodes, i)

  @staticmethod
  def heap_sort(nodes):
    """
      Best case: [0, 0, 0, 0, 0]
      Average case: 
      Worst case: [4, 3, 2, 1, 0]
      Unstable case: [(0, 'z'), (2, 'a'), (2, 'b'), (1, 'c')] when sorted by the 1st(index=0) entry of each element.
    """
    Heap.build_heap(nodes)
    heap_len = len(nodes)
    for i in range(len(nodes) - 1, 0, -1):
      nodes[i], nodes[0] = nodes[0], nodes[i]
      heap_len = heap_len - 1
      Heap.heapify(nodes, 0, heap_len)

def quick_sort(array, p, r): # the subarray we want to sort is from p ~ r (inclusive)
  """
    Best case: 
    Average case: 
    Worst case: [0, 1, 2, 3, 4]
    Unstable case: [(0, 'z'), (2, 'a'), (2, 'b'), (1, 'c')] when sorted by the 1st(index=0) entry of each element.
  """
  def partition(array, p, r): # the subarray we want to partition is from p ~ r (inclusive)
    x = array[r] # always choose the last item of the subarray as pivot
    i = p - 1
    for j in range(p, r):
      if array[j] <= x:
        i += 1
        array[i], array[j] = array[j], array[i] # python's way to swap
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1
  if p < r:
    q = partition(array, p, r)
    quick_sort(array, p, q-1)
    quick_sort(array, q+1, r)

# Test utils start

@total_ordering
class MyItem(object):
  def __init__(self, data: tuple):
    self.data = data

  def __eq__(self, other):
    return self.data[0] == other.data[0]

  def __lt__(self, other):
    return self.data[0] < other.data[0]

  def perfect_equal(self, other):
    return self.data[0] == other.data[0] and self.data[1] == other.data[1]

  def __repr__(self):
    return str(self.data)

def is_stable(res, ans):
  for i in range(len(res)):
    if isinstance(res[i], MyItem):
      if not res[i].perfect_equal(ans[i]):
        return False
    else:
      if res[i] != ans[i]:
        return False
  return True

def get_inputs(case):
  array = []
  not_stable_list = []
  complicated_input = [2, 2, 5, 3, 4, 4, 8, 7, 0, 9, 6, 1, 4, 0]
  if case == 0:
    pass
  elif case == 1:
    array = [0]
  elif case == 2:
    array = [0, 1]
  elif case == 3:
    array = [1, 0]
  elif  case == 4:
    array = [0, 1, 1, 2]
  elif case == 5:
    array =[2, 10, 5, 3, 4, 8, 7, 0, 9, 6, 1]
  elif case == 6:
    array = complicated_input
  elif case == 7:
    zero_names = ['d', 'e']
    zero_idx = 0
    two_names = ['f', 'g']
    two_idx = 0
    four_names = ['a', 'b', 'c']
    four_idx = 0
    for x in complicated_input:
      if x == 0:
        array.append(MyItem((x, zero_names[zero_idx])))
        zero_idx += 1
      elif x == 2:
        array.append(MyItem((x, two_names[two_idx])))
        two_idx += 1
      elif x == 4:
        array.append(MyItem((x, four_names[four_idx])))
        four_idx += 1
      else:
        array.append(MyItem((x, 'z')))
  elif case == 8:
    array = [MyItem((0, 'z')), MyItem((2, 'a')), MyItem((2, 'b')), MyItem((1, 'c'))]
  if case in [7, 8]:
    not_stable_list = ['selection_sort', 'heap_sort', 'quick_sort']
  ans = sorted(array)
  return array, ans, not_stable_list

# Test utils end
  

def main():
  def add_args_for_merge_sort(args, case):
    if (case == 7) or (case == 8):
      args.append(MyItem((float('inf'), 'z')))
  sorts = [
    (selection_sort, 1, None), # not stable
    (bubble_sort, 1, None),
    (insertion_sort, 1, None),
    (merge_sort, 3, add_args_for_merge_sort),
    (Heap.heap_sort, 1, None), # not stable
    (quick_sort, 3, None), # not stable
  ]
  start = 0
  end = 9
  for func, num_args, add_args in sorts:
    fn_name = func.__name__
    # print('{} ==='.format(fn_name))
    for case in range(start, end):
      array, ans, not_stable_list = get_inputs(case)
      args = [array, 0, len(array) - 1][:num_args]
      if add_args:
        add_args(args, case)
      # print('---')
      # print('before:', array)
      func(*args)
      # print('after :', array)
      # print('ans   :', ans)
      assert array == ans
      if fn_name in not_stable_list:
        assert is_stable(array, ans) == False
      else:
        assert is_stable(array, ans) == True
    print('{} success'.format(fn_name))

if __name__ == '__main__':
  main()
