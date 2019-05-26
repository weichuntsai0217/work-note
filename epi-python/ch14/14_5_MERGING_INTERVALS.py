from __future__ import print_function

def is_overlap(a, b):
  return a[1] >= b[0] and a[0] <= b[1]

def merging_intervals(array, added_item):
  """
    The time complexity is O(n) where n is the array length.
    The additional space complexity is O(1)
  """
  res = []
  mg_item = [added_item[0], added_item[1]]
  i = 0
  while i < len(array):
    """
      If added_item is at the right of the array and not overlap with the last interval of array,
      I need i finally equal to len(array).
      That's why I use "while" loop instead of a "for" loop
    """
    itr = array[i]
    if is_overlap(mg_item, itr):
      mg_item = [
        min(mg_item[0], itr[0]),
        max(mg_item[1], itr[1])
      ]
    elif mg_item[1] < itr[0]:
      break
    elif mg_item[0] > itr[1]:
      res.append(itr)
    i += 1
  res.append(mg_item)
  while i < len(array):
    res.append(array[i])
    i += 1
  return res
  
def get_input(case=0):
  array = [[-4,-1],[0,2],[3,6],[7,9],[11,12],[14,17]]
  added_item = [1,8]
  ans = [[-4,-1],[0,9],[11,12],[14,17]]
  if case == 0:
    pass
  elif case == 1:
    added_item = [20, 21]
    ans = [[-4,-1],[0,2],[3,6],[7,9],[11,12],[14,17], [20, 21]]
  elif case == 2:
    added_item = [8, 12]
    ans = [[-4,-1],[0,2],[3,6],[7,12],[14,17]]
  return array, added_item, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    array, added_item, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('added_item =', added_item)
    res = merging_intervals(array, added_item)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()





