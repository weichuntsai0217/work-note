from __future__ import print_function

def compute_intersection_of_two_sorted_arrays(array_0, array_1):
  """
    The time complexity is O(m + n) where m, n is the length of array_0 and array_1 respectively.
    The additional space complexity is O(1)
  """
  res = []
  i = 0
  j = 0
  while i < len(array_0) and j < len(array_1):
    if array_0[i] == array_1[j]:
      if not res:
        res.append(array_0[i])
      elif res[-1] != array_0[i]:
        res.append(array_0[i])
      i += 1
      j += 1
    elif array_0[i] < array_1[j]:
        i += 1
    else: # array_0[i] > array_1[j]
        j += 1
  return res
  
def get_input(case=0):
  array_0 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
  array_1 = [5, 5, 6, 8, 8, 9, 10, 10]
  ans = [5, 6, 8]
  if case == 0:
    pass
  elif case == 1:
    array_0.append(13)
    array_1.append(13)
    ans.append(13)
  return array_0, array_1, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    array_0, array_1, ans = get_input(case)
    print('Input:')
    print('array_0 =', array_0)
    print('array_1 =', array_1)
    res = compute_intersection_of_two_sorted_arrays(array_0, array_1)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

