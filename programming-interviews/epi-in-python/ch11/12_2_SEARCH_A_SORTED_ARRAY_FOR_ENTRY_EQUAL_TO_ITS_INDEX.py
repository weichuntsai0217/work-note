from __future__ import print_function

def search_a_sorted_array_for_entry_equal_to_its_index(array):
  """
    This problem's input assumption is that only distinct integers in the input array.
    Each element in the array are all integers (no float numbers) and because distinct,
    The difference of adjacent elements is at least 1.
    The time complexity is O(logn) where n is the array length.
  """
  l = 0
  h = len(array) - 1
  while l <= h:
    m = l + (h - l)/2
    if array[m] < m:
      l = m + 1
    elif array[m] == m:
      return m
    else:
      h = m - 1
     
  return -1

def get_input(case=0):
  array = None
  ans = None
  if case == 0:
    array = [-2,0,2,3,6,7,9]
    ans = [2, 3]
  elif case == 1:
    array = [-2,0,2,4,6,7,9]
    ans = [2]
  return array, ans
    

def main():
  for case in xrange(2):
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('Output:')
    res = search_a_sorted_array_for_entry_equal_to_its_index(array)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res in ans else 'Test failure')


if __name__ == '__main__':
  main()
