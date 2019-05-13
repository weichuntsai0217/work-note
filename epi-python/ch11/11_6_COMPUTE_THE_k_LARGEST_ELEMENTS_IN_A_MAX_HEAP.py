from __future__ import print_function
import heapq

def get_left_child(idx):
  return 2 * idx + 1

def get_right_child(idx):
  return 2 * idx + 2

def get_k_largest(max_heap, k): # data in max_heap are all negative, because python does not have a real max_heap.
  """
    The time complexity is O(k * logk)
    The additional space complexity is O(k)
  """
  res = []
  idx = 0
  helper = [(max_heap[0], 0)]
  for i in xrange(k):
    x = heapq.heappop(helper)
    res.append(x[0])
    idx = x[1]
    left = get_left_child(idx)
    right = get_right_child(idx)
    if left < len(max_heap):
      heapq.heappush(helper, (max_heap[left], left))
    if right < len(max_heap):
      heapq.heappush(helper, (max_heap[right], right))
  return res

def get_input(case=0):
  import random
  max_heap = None
  k = None
  ans = None
  if case == 0:
    max_heap = [-561,-314,-401,-28,-156,-359,-271,-11,-3]
    k = 4
    ans = sorted(max_heap)[:k]
  elif case == 1:
    max_heap = [-int(random.random()*100) for i in xrange(23)]
    heapq.heapify(max_heap)
    k = 6
    ans = sorted(max_heap)[:k]
  return max_heap, k, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    max_heap, k, ans = get_input(case)
    print('Input:')
    print('max_heap =', max_heap)
    print('k =', k)
    res = get_k_largest(max_heap, k)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
