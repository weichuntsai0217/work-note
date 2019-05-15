from __future__ import print_function

def find_k_largest(x, k):
  """
    The time complexity is O(n * logk)
    The additional space complexity is O(k)
  """
  if k > len(x) or k < 1: return None
  import heapq
  min_heap = []
  for i in xrange(len(x)):
    heapq.heappush(min_heap, x[i])
    if len(min_heap) > k:
      heapq.heappop(min_heap)
  res = heapq.heappop(min_heap)
  return res

def find_k_largest_epi(x, k):
  """
    I don't like this solution actually.
    The time complexity for worst case is O(n^2) where n is the x length.
    EPI says that for average time complexity it is O(n) for most cases.
  """
  import random
  def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

  def partition(x, left, right, pivot_idx):
    pivot = x[pivot_idx]
    swap(x, pivot_idx, right)
    """
      If you need the final pivot idx,
      then swap pivot to the end of the array is necessary.

      If you don't need the final pivot idx and just care about the final grouped array,
      then you basic don't need to swap pivot to the end of the array like 06_1_THE_DUTCH_NATIONAL_FLAG_PROBLEM.py
    """
    final_pivot_idx = left
    """
      The key point for partition in quick sort is,
      Just swap items which should be on the left-hand side of pivot to 
      the updated position final_pivot_idx.
      For items which should be on the right-hand side of pivot,
      don't do anything.
    """
    for j in xrange(left, right): # index is from left to right -1, because index right now is the pivot value.
      if x[j] > pivot:
        swap(x, j, final_pivot_idx)
        final_pivot_idx += 1
    swap(x, right, final_pivot_idx)
    return final_pivot_idx

  left = 0
  right = len(x) - 1
  while left <= right:
    pivot_idx = random.randint(left, right)
    res_idx = partition(x, left, right, pivot_idx)
    if res_idx == (k - 1):
      return x[res_idx]
    elif res_idx > (k - 1):
      right = res_idx - 1
    else:
      left = res_idx + 1


def get_input(case=0):
  x = [3,2,1,5,4]
  k = None
  idx = None
  if case == 0:
    k = 3
    idx = 0
  elif case == 1:
    k = 4
    idx = 1
  elif case == 2:
    k = 1
    idx = 3
  elif case == 3:
    k = 5
    idx = 2
  return x, k, x[idx]
 
if __name__ == '__main__':
  print('Use find_k_largest')
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    x, k, ans = get_input(case)
    print('Input:')
    print('x =', x)
    print('k =', k)
    print('Output:')
    res = find_k_largest(x, k)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('======================')
  print('Use find_k_largest_epi')
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    x, k, ans = get_input(case)
    print('Input:')
    print('x =', x)
    print('k =', k)
    print('Output:')
    res = find_k_largest_epi(x, k)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

