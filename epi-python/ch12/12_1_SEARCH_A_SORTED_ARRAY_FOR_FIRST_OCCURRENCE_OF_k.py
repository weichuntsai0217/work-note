from __future__ import print_function

def search_the_first_occurrence_k_using_built_in(array, k):
  from bisect import bisect_left
  i = bisect_left(array, k)
  if (i != len(array)) and k == array[i]:
    return i
  return -1

def search_the_first_occurrence_k(array, t):
  """
    The time complexity is O(logn) where n is the array length.
  """
  l = 0
  h = len(array) - 1
  while l <= h:
    m = l + (h - l) / 2
    if t < array[m]:
      h = m - 1
    elif t == array[m]:
      if (m == 0) or (t != array[m-1]):
        return m
      else:
        # m > 0 and t == array[m-1]:
        h = m - 1
    else:
      l = m + 1
  return -1
    

def get_input(case=0):
  array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
  t = None
  ans = None
  if case == 0:
    t = -15
    ans = -1
  elif case == 1:
    t = 402
    ans = -1
  elif case == 2:
    t = 110
    ans = -1
  elif case == 3:
    t = -10
    ans = 1
  elif case == 4:
    t = 108
    ans = 3
  elif case == 5:
    t = 285
    ans = 6
  elif case == 6:
    t = -14
    ans = 0
  elif case == 7:
    t = 401
    ans = len(array) - 1
  return array, t, ans
    

def main():
  print('Use search_the_first_occurrence_k_using_built_in')
  for case in xrange(8):
    array, t, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('t =', t)
    print('Output:')
    res = search_the_first_occurrence_k_using_built_in(array, t)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('Use search_the_first_occurrence_k')
  for case in xrange(8):
    array, t, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('t =', t)
    print('Output:')
    res = search_the_first_occurrence_k(array, t)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
