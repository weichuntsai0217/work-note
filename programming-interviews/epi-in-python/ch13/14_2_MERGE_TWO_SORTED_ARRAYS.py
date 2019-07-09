from __future__ import print_function

def merge_two_sorted_arrays(array_0, array_1, m, n):
  """
    The time complexity is O(m + n)
    The additional space complexity is O(1)
  """
  write_idx = m + n - 1
  i = m - 1
  j = n - 1
  while i >= 0 and j >= 0:
    if array_0[i] > array_1[j]:
      array_0[write_idx] = array_0[i]
      i -= 1
    else:
      array_0[write_idx] = array_1[j]
      j -= 1
    write_idx -= 1
  while j >= 0:
    array_0[write_idx] = array_1[j]
    j -= 1
    write_idx -= 1
  
def get_input(case=0):
  array_0 = [5, 13, 17] + [None]*5
  m = 3
  array_1 = [3, 7, 11, 19]
  n = 4
  ans = [3, 5, 7, 11, 13, 17, 19, None]
  if case == 0:
    pass
  elif case == 1:
    array_0[0] = 1
    array_0[2] = 20
    ans = [1, 3, 7, 11, 13, 19, 20, None]
  elif case == 2:
    array_0 = [1, 2, 3] + [None]*5
    array_1 = [4, 5, 6, 7]
    ans = [1, 2, 3, 4, 5, 6, 7, None]
  elif case == 3:
    array_0 = [5, 6, 7] + [None]*5
    array_1 = [1, 2, 3, 4]
    ans = [1, 2, 3, 4, 5, 6, 7, None]
  return array_0, array_1, m, n, ans

def main():
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    array_0, array_1, m, n, ans = get_input(case)
    print('Input:')
    print('array_0 =', array_0)
    print('array_1 =', array_1)
    merge_two_sorted_arrays(array_0, array_1, m, n)
    print('Output:')
    print('res =', array_0)
    print('ans =', ans)
    print('Test success' if array_0 == ans else 'Test failure')

if __name__ == '__main__':
  main()


