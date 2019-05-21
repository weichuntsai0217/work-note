from __future__ import print_function

def get_closest_pair(strings):
  """
    (What I do is more than the problem's requirement,
     if you just want to return the min distance, the code could be less.)
    The time complexity is O(n) where n is the length of strings.
    The additional space complexity is O(d) where d is the number of distinct words in strings.
  """
  table = {}
  for i in xrange(len(strings)):
    s = strings[i]
    if s in table:
      (last_min_dis, last_min_start, last_pair_end) = table[s]
      if last_pair_end == None:
        table[s] = (i - last_min_start, last_min_start, i)
      else:
        min_dis = last_min_dis
        min_start = last_min_start
        if (i - last_pair_end) < last_min_dis:
          min_dis = i - last_pair_end
          min_start = last_pair_end
        table[s] = (min_dis, min_start, i)
    else:
      table[s] = (float('inf'), i, None)
  res = None
  for key in table:
    if res:
      if table[key][0] < res[3]:
        res = (key, table[key][1], table[key][1] + table[key][0], table[key][0])
    else:
      res = (key, table[key][1], table[key][1] + table[key][0], table[key][0])
  return res

def get_input(case=0):
  strings = [
    'All', 'work', 'and', 'no',
    'play', 'makes', 'for', 'no',
    'work', 'no', 'fun', 'and', 'no',
    'results',
  ]
  ans = ('no', 7, 9, 2)
  if case == 0:
    pass
  return strings, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    strings, ans = get_input(case)
    print('Input:')
    print('strings =', strings)
    res = get_closest_pair(strings)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

