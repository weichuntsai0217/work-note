from __future__ import print_function
import heapq

def get_online_median(it):
  """
    The time complexity is for each Iteration in while loop is O(logn) where n is the data seen so far.
    The additional space complexity is O(n).
  """
  min_heap = [] # record the larger half
  max_heap = [] # record the smaller half
  output = []

  while True:
    try:
      x = it.next()
      if not len(min_heap):
        heapq.heappush(min_heap, x)
      else:
        if x >= min_heap[0]:
          heapq.heappush(min_heap, x)
          if (len(min_heap) - len(max_heap)) > 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        else:
          heapq.heappush(max_heap, -x)
          if (len(max_heap) - len(min_heap)) > 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
      
      if len(min_heap) > len(max_heap):
        output.append(min_heap[0])
      elif len(min_heap) < len(max_heap):
        output.append(-max_heap[0])
      else:
        output.append((min_heap[0] - max_heap[0]) / 2.)
        
    except StopIteration:
      break

  return output

def get_input(case=0):
  it = None
  ans = None
  if case == 0:
    src = [1, 0, 3, 5, 2, 0, 1]
    it = iter(src)
    ans = [1, 0.5, 1, 2, 2, 1.5, 1.0]
  return src, it, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    src, it, ans = get_input(case)
    print('Input:')
    print('src =', src)
    res = get_online_median(it)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
