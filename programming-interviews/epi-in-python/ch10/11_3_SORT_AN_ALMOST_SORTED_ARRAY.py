from __future__ import print_function
import heapq

def sort_k_sorted_array(array, k):
  """
    For test convience, I save the output in res.
    The time complexity is O(n * logk) where n is the array length.
    The additional space complexity is O(k) because of maintaining a min_heap.
  """
  res = []
  min_heap = []
  itr = iter(array)
  for i in xrange(k):
    heapq.heappush(min_heap, itr.next())

  while True:
    try:
      x = itr.next()
      res.append(heapq.heappushpop(min_heap, x))
    except StopIteration:
      break
  
  while min_heap:
    res.append(heapq.heappop(min_heap))

  return res
  
def get_input(case=0):
  array = None
  k = None
  ans = None
  if case == 0:
    array = [3,-1,2,6,4,5,8]
    k = 2
    ans = sorted(array)
  return array, k, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, k, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('k =', 2)
    res = sort_k_sorted_array(array, k)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
