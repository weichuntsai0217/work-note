from __future__ import print_function

def find_longest_subarray_with_distinct_entries(array):
  """
    The time complexity is O(n) where n is the length of array.
    The additional space complexity is O(d) where d is the number of distinct element in the array.
  """
  if not array: return (None, None)
  if len(array) == 1: return (0, 1)
  # the 1st number is the start index of the subarray, and the 2nd number is the length of the subarray
  start = 0
  res_start = 0
  res_end = 1
  table = {}
  for end in xrange(len(array)):
    if array[end] in table:
      if table[array[end]] >= start:
        if (end - start) > (res_end - res_start):
          res_start = start
          res_end = end
        start = table[array[end]] + 1
    if (end + 1) == len(array):
      if (end - start + 1) > (res_end - res_start):
        res_start = start
        res_end = end + 1
    table[array[end]] = end
  return (res_start, res_end - res_start)


def get_input(case=0):
  array = list('fsfetwenwe')
  ans = (1, 5)
  if case == 0:
    pass
  elif case == 1:
    array = list('fsfetwenwpqrs')
    ans = (6, 7)
  elif case == 2:
    array = list('fsfetwenwpqrss')
    ans = (6, 7)
  elif case == 3:
    array = list('fsfetsenwpqrss')
    ans = (4, 8)
  elif case == 4:
    array = list('asfetwenwpqrss')
    ans = (6, 7)
  elif case == 5:
    array = list('aaaaa')
    ans = (0, 1)
  elif case == 6:
    array = list('abcdef')
    ans = (0, 6)
  return array, ans

def main():
  for case in xrange(7):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = find_longest_subarray_with_distinct_entries(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

