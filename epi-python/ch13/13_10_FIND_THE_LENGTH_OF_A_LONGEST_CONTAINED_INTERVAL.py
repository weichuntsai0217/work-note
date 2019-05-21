from __future__ import print_function

def find_longest_contained_interval_epi(array):
  """
    The time complexity is O(n) where n is the array length
    The additional space complexity is O(n) where n is the array length
  """
  if len(array) <= 1: return len(array)
  res = 1
  unprocess = {}
  for item in array:
    unprocess[item] = True
  
  while unprocess:
    a = iter(unprocess).next()
    del unprocess[a]

    upper_bound = a + 1
    while upper_bound in unprocess:
      del unprocess[upper_bound]
      upper_bound += 1

    lower_bound = a - 1
    while lower_bound in unprocess:
      del unprocess[lower_bound]
      lower_bound -= 1

    res = max(res, upper_bound - lower_bound - 1)
  return res

def find_longest_contained_interval(array):
  """
    The time complexity is O(n) where n is the array length.
    The additional space complexity is O(n) where n is the array length.
  """
  if len(array) <= 1: return len(array)
  res = 1
  is_old = {}
  s_to_e_map = {} # mapping start to end, start < end
  e_to_s_map = {} # mapping end to start, start < end
  for item in array:
    if item not in is_old:
      is_old[item] = True
      if (item not in s_to_e_map) and (item not in e_to_s_map):
        if ((item + 1) in s_to_e_map) and ((item - 1) not in e_to_s_map):
          e = s_to_e_map[item + 1]
          del s_to_e_map[item + 1]
          del e_to_s_map[e]
          s_to_e_map[item] = e
          e_to_s_map[e] = item
          res = max(res, e - item + 1)
        elif ((item + 1) not in s_to_e_map) and ((item - 1) in e_to_s_map):
          s = e_to_s_map[item - 1]
          del e_to_s_map[item - 1]
          del s_to_e_map[s]
          e_to_s_map[item] = s
          s_to_e_map[s] = item
          res = max(res, item - s + 1)
        elif ((item + 1) not in s_to_e_map) and ((item - 1) not in e_to_s_map):
          s_to_e_map[item] = item
          e_to_s_map[item] = item
        elif ((item + 1) in s_to_e_map) and ((item - 1) in e_to_s_map):
          start = e_to_s_map[item - 1]
          end = s_to_e_map[item + 1]
          del e_to_s_map[item - 1]
          del s_to_e_map[start]
          del s_to_e_map[item + 1]
          del e_to_s_map[end]
          s_to_e_map[start] = end
          e_to_s_map[end] = start
          res = max(res, end - start + 1)
  return res

def get_input(case=0):
  array = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8] 
  ans = 6
  if case == 0:
    pass
  return array, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = find_longest_contained_interval_epi(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

