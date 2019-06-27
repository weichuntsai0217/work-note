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

def get_input(case=0):
  x = None
  ans = None
  if case == 0:
    x = [2, 0, 1]
    ans = [2, 1, 0]
  elif case == 1:
    x = [0, 1, 2]
    ans = [0, 2, 1]
  elif case == 2:
    x = [2, 1, 0]
    ans = []
  elif case == 3:
    x = [1, 0, 3, 2]
    ans = [1, 2, 0, 3]
  elif case == 4:
    x = [3, 2, 1, 0]
    ans = []
  elif case == 5:
    x = [1, 3, 5, 4, 0]
    ans = [1, 4, 0, 3, 5]
  elif case == 6:
    x = [1, 3, 4, 5, 0]
    ans = [1, 3, 5, 0, 4]

  return x, ans

def main():
  for case in xrange(7):
    x, ans = get_input(case)
    res = get_next_permutation(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
