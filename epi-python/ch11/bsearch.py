from __future__ import print_function
from bisect import bisect_left

def bsearch(array, t):
  l = 0
  u = len(array) - 1
  while l <= u:
    m = l + (u - l) / 2 # why not m = ( l + u )/2 ? because we want to prevent overflow.
    if t < array[m]:
      u = m - 1
    elif t == array[m]:
      return m
    else:
      l = m + 1
  return -1 # the target not found

def bsearch_python_built_in(array, t):
  i = bisect_left(array, t)
  if i != len(array) and t == array[i]:
    return i
  return -1

def get_input(case=0):
  array = [ x * 10 for x in range(1, 21)]
  t = None
  ans = None
  if case == 0:
    t = 210
    ans = -1
  elif case == 1:
    t = 0
    ans = -1
  elif case == 2:
    t = 35.5
    ans = -1
  elif case == 3:
    t = 70
    ans = 6
  elif case == 4:
    t = 10
    ans = 0
  elif case == 5:
    t = 200
    ans = 19
  return array, t, ans

def main():
  print('Use bsearch')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    array, t, ans = get_input(case)
    res = bsearch(array, t)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('Use bsearch_python_built_in')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    array, t, ans = get_input(case)
    res = bsearch_python_built_in(array, t)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

