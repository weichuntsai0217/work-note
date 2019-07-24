"""
  Use python 3.6.8
"""
"""
  This file discusses how to handle duplicate items in heap,
  even though the scenarios are not as complicated as those in real life.
"""

def scenario_1():
  """
    Get k largest items in a sorted array with duplicates.
    In this case, you don't even use heap.
  """
  def get_k_largest_for_a_sorted_array(k, array):
    """
      The time complexity is O(n) where n is the array length.
      The space complexity without the output is O(1).
    """
    res = [array[len(array) -1]] if array else []
    k -= 1
    for i in range(len(array) - 2, 0, -1):
      if array[i] != array[i-1]:
        res.append(array[i-1])
        k -= 1
      if k == 0:
        break
    return res
  array = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6]

  k = 3
  assert get_k_largest_for_a_sorted_array(k, array) == [6, 5, 4]

  k = 4
  assert get_k_largest_for_a_sorted_array(k, array) == [6, 5, 4, 3]

  k = 6
  assert get_k_largest_for_a_sorted_array(k, array) == [6, 5, 4, 3, 2, 1]

  k = 7
  assert get_k_largest_for_a_sorted_array(k, array) == [6, 5, 4, 3, 2, 1]

  array = []
  k = 8
  assert get_k_largest_for_a_sorted_array(k, array) == []

  print('scenario_1 success')

def scenario_2():
  """
    Get k largest items in an unsorted array with duplicates.
    In this case, the best I can do is cache items we've seen.
  """
  import random
  def get_k_largest_for_an_unsorted_array(k, array):
    """
      The time complexity is O(n * log(k)) where n is the array length.
      The space complexity without the output is O(m) where m is the number of distinct elements in the array.
    """
    import heapq
    if not array: return []
    min_heap = []
    seen = set()
    for x in array:
      if x not in seen:
        seen.add(x)
        heapq.heappush(min_heap, x)
        if len(min_heap) == k + 1:
          heapq.heappop(min_heap)
    return sorted(min_heap, reverse=True) # k * log(k)

  array = []
  k = 8
  assert get_k_largest_for_an_unsorted_array(k, array) == []

  array = sorted([1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6], key=lambda x: random.random())

  k = 3
  assert get_k_largest_for_an_unsorted_array(k, array) == [6, 5, 4]

  k = 4
  assert get_k_largest_for_an_unsorted_array(k, array) == [6, 5, 4, 3]

  k = 6
  assert get_k_largest_for_an_unsorted_array(k, array) == [6, 5, 4, 3, 2, 1]

  k = 7
  assert get_k_largest_for_an_unsorted_array(k, array) == [6, 5, 4, 3, 2, 1]

  print('scenario_2 success')

def scenario_3():
  """
    Sometime you need to distinguish items with the same key, but they are pushed in
    the heap at different time/order.
    You can consider push the element like this:
      x = (key, order, obj)
  """
  import heapq

  class Student(object):
    def __init__(self, name, grade):
      self.name = name
      self.grade = grade

  s_1 = Student('mary', 20)
  s_2 = Student('john', 20)
  items = []
  heapq.heappush(items, (s_1.grade, 0, s_1))
  heapq.heappush(items, (s_2.grade, 1, s_2))
  assert items[0][2].name == 'mary'
  assert items[1][2].name == 'john'
  print('scenario_3 success')

def main():
  scenario_1()
  scenario_2()
  scenario_3()

if __name__ == '__main__':
  main()
