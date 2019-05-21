from __future__ import print_function
import heapq

def get_k_most_queries(strings, k):
  """
    The time complexity is O(n + m*logk) where n is the number of strings, m is the number of distinct strings, and k
    is the input k.
    The additional space complexity is O(m)
    EPI also says you can do a little twist on 12_8_FIND_THE_kth_LARGEST_ELEMENT.py to get a solution with
    average time complexity is O(n) but the worst time complexity is O(n^2) and EPI argues that
    the worst case happens rarely.
  """
  table = {}
  for s in strings:
    if s not in table:
      table[s] = 0
    table[s] += 1
  res = []
  for key in table:
    heapq.heappush(res, (table[key], key))
    if len(res) > k:
      heapq.heappop(res)
  return map(lambda x: x[1], res)

def get_input(case=0):
  import random
  strings = sorted(['a']*10 + ['b']*9 + ['c']*8 + ['d']*7 + ['e']*6 + ['f']*5, key=lambda x: random.random())
  k = 3
  ans = ['a', 'b', 'c']
  if case == 0:
    pass
  return strings, k, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    strings, k, ans = get_input(case)
    print('Input:')
    print('strings =', strings)
    print('k =', k)
    res = sorted(get_k_most_queries(strings, k))
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()


