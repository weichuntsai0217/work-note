from __future__ import print_function

def swap(x, i, j):
  temp = x[i]
  x[i] = x[j]
  x[j] = temp

def reverse(x, start):
  mid = (len(x) - start)/2 + start
  invariant = start + len(x) - 1
  for i in xrange(start, mid):
    swap(x, i, invariant - i)

def pick_next_bigger_and_swap(x, start):
  # The subarray at the rigth of the index "start" is a descending array
  i = start + 1
  while i < len(x):
    if x[i] < x[start]: # find the item which is the least upper bound of x[start]
      swap(x, start, i - 1)
      return
    if i == (len(x) - 1): # the item which is the least upper bound of x[start] is at the end of the subarray.
      swap(x, start, i)
      return
    i += 1

def get_next_permutation(x): # in-place change and all items in x are distinct. for simplicity we still return x
  """
    Time complexity is O(n)
    Additional space complexity is O(1)
  """
  if not x or len(x) == 1: return []
  end = len(x) - 1
  start = end - 1
  while start >= 0:
    if x[start] < x[end]:
      pick_next_bigger_and_swap(x, start)
      reverse(x, start+1)
      return x
    else:
      end = start
      start -= 1
  return [] # the permutation is in descending order which is the biggest order.

