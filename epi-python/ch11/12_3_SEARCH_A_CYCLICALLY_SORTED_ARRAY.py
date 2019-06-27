from __future__ import print_function

def get_the_smallest_in_cyc_sorted_array(array):
  """
    The time complexity is O(logn) where n is the array length.
  """
  l = 0
  h = len(array) - 1
  while l < h:
    m = l + (h - l) / 2
    if array[m] > array[h]:
      """
        In this case, m cannot be the start of the sorted array (the start of the sorted array should be the smallest.)
        so we use l = m + 1 to exclude current m
        Also, this case is valid when:
        1. the start of the sorted array is at index h
        or
        2. the start of the sorted array is at index which is right to m.
      """
      l = m + 1
    else:
      """
        This case is valid when:
        1. the start of the sorted array is at index 0
        or
        2. the start of the sorted array is at index m or at the index which is left to m
      """
      h = m
      
  return l

def shift_list(array, s):
  """
    s can be 0, positive or negtive integer.
    positive for shifting right.
    negative for shifting left.
    0 for no shift.
  """
  s %= len(array)
  s = len(array) - s
  return array[s:] + array[:s]

def get_input(case=0):
  array = [103, 203, 220, 234, 279, 368, 378, 478, 550, 631]
  ans = None
  if case == 0:
    ans = 0
  elif case == 1:
    ans = 9
  elif case == 2:
    ans = 4
  elif case == 3:
    ans = 7
  elif case == 4:
    ans = 3
  array = shift_list(array, ans)
  return array, ans
    

def main():
  for case in xrange(5):
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('Output:')
    res = get_the_smallest_in_cyc_sorted_array(array)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()

