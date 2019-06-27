from __future__ import print_function
import heapq

def merge_lists(ls):
  """
    The time complexity is O(n*logk) where n is the total number of elements in input sequences and k is the number of
      sequences.
    The additional space complexity is O(k).
  """
  its = [iter(x) for x in ls]
  min_heap = []
  res = []
  
  for seq_id in xrange(len(its)):
    try:
      x = its[seq_id].next()
      heapq.heappush(min_heap, (x, seq_id)) # if you pass a tuple, heapq uses the tuple[0] as priority.
    except:
      pass
  
  while min_heap: # n times
    (val, seq_id) = heapq.heappop(min_heap) # logk
    res.append(val)
    try:
      x = its[seq_id].next()
      heapq.heappush(min_heap, (x, seq_id)) # logk
    except:
      pass

  return res

def sort_an_inc_dec_array(array):
  """
    The time complexity is O(n * logn) where n is the number of elements in the array.
  """
  return sorted(array)

def sort_an_inc_dec_array_quick(array):
  """
    The input array contains at least 3 elements to satisfy the k-increasing-decreasing condition.
    The time complexity is O(n*log2k) = O(n*logk) where k is the number of increasing-decreasing cycles
    and n is the number of total elements in the input array.
    The additional space complexity is O(k) excluding the output sorted array.
  """
  is_decreasing = False
  ls = []
  start_idx = 0
  for i in xrange(1, len(array) + 1):
    if (
      (i == len(array)) or
      (is_decreasing and array[i-1] < array[i]) or
      (not is_decreasing and array[i-1] > array[i])
    ):
      tmp = array[start_idx:i]
      if is_decreasing: tmp.reverse()
      ls.append(tmp)
      is_decreasing = not is_decreasing
      start_idx = i
      
  return merge_lists(ls)

def get_input(case=0):
  array = None
  ans = None
  if case == 0:
    array = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    ans = sorted(array)
  return array, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = sort_an_inc_dec_array_quick(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
