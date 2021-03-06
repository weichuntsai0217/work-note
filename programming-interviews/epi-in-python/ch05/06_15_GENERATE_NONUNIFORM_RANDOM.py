from __future__ import print_function

def bsearch_interval_python_built_in(array, t):
  """
    For different problem scenario, please do different error handling.
  """
  from bisect import bisect_left
  if t >= array[-1] or t < array[0]:
    """
      t should not be the last element (that is 1.0) of the array or
      greater than the last element (that is 1.0) of the array or
      less than the 1st element(that is 0.0) of the array
      because t is in [0, 1) in this problem.
    """
    raise ValueError('The input target `t` is greater than or equal to our array upper limit. Or it is less than the lower limit of the array')
  i = bisect_left(array, t)
  if t == array[i]:
    return i
  else:
    return i - 1 # because bisect_left always picks the index which lets the new element on the left to the old elements

def gen_nonuniform_random_using_python_built_in(ns, ps): # ns is numbers, ps is probabilities
  """
    Time complexity is O(n) (but the search part is faster than gen_nonuniform_random)
    Additional space complexity is O(n)
  """
  import random
  tmp = random.random() # gen [0, 1)
  accu_ps = [0]
  for i in xrange(len(ps)):
    accu_ps.append(accu_ps[-1] + ps[i])
  return ns[bsearch_interval_python_built_in(accu_ps, tmp)]

def binary_search(x, target):
  def _bs(x, target, lo, hi):
    mid = (lo + hi) / 2
    if target > x[mid]:
      if (hi - mid) == 1:
        return mid
      return _bs(x, target, mid, hi)
    elif target < x[mid]:
      if (mid - lo) == 1:
        return lo
      return _bs(x, target, lo, mid)
    else:
      return mid
  return _bs(x, target, 0, len(x) - 1)


def gen_nonuniform_random_using_binary_search(ns, ps): # ns is numbers, ps is probabilities
  """
    Time complexity is O(n) (but the search part is faster than gen_nonuniform_random)
    Additional space complexity is O(n)
  """
  import random
  tmp = random.random() # gen [0, 1)
  accu_ps = [0]
  for i in xrange(len(ps)):
    accu_ps.append(accu_ps[-1] + ps[i])
  return ns[binary_search(accu_ps, tmp)]

def gen_nonuniform_random(ns, ps): # ns is numbers, ps is probabilities
  """
    Time complexity is O(n)
    Additional space complexity is O(1)
  """
  import random
  tmp = random.random() # gen [0, 1)
  start_p = 0
  for i in xrange(len(ps)):
    end_p = start_p + ps[i]
    if (tmp >= start_p) and (tmp < end_p):
      return ns[i]
    start_p += ps[i]

def get_input():
  ns = [3, 5, 7, 11]
  ps = [9./18., 6./18., 2./18., 1./18.]
  return ns, ps

def main():
  ns, ps = get_input()
  counts = {}
  print('Use normal search')
  for i in xrange(1000000):
    x = gen_nonuniform_random(ns, ps)
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
  print(counts)


  counts = {}
  print('Use binary search')
  for i in xrange(1000000):
    x = gen_nonuniform_random_using_binary_search(ns, ps)
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
  print(counts)

  counts = {}
  print('Use binary search built-in')
  for i in xrange(1000000):
    x = gen_nonuniform_random_using_python_built_in(ns, ps)
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
  print(counts)

if __name__ == '__main__':
  main()
