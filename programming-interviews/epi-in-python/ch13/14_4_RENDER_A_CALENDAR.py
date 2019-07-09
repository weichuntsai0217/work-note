from __future__ import print_function

def get_max_concurrent_event(array):
  """
    The time complexity is O(n * logn) where n is the array length.
    The additional space complexity is O(n)
  """
  points = []
  for itr in array:
    points.append((itr[0], 0)) # the 2nd element in tuple is is_start, 0 for True, 1 for False
    points.append((itr[1], 1))
  points.sort()

  max_num_events = 0
  cur_num_events = 0
  for p in points:
    if p[1] == 0:
      cur_num_events += 1
      max_num_events = max(max_num_events, cur_num_events)
    else:
      cur_num_events -= 1
  return max_num_events
  
def get_input(case=0):
  array = [
    (4, 5),
    (9, 17),
    (2, 7),
    (8, 9),
    (12, 15),
    (1, 5),
    (6, 10),
    (11, 13),
    (14, 15),
  ]
  ans = 3
  if case == 0:
    pass
  elif case == 1:
    array.append((8, 9))
    ans = 4
  return array, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = get_max_concurrent_event(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()






