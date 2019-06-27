from __future__ import print_function
import heapq

def get_max_avg_by_top_3(records):
  """
    The time complexity is O(n * log3) = O(n) where n is the array length.
    The additional space complexity is O(3m) = O(m) where m is the number of distinct students.
  """
  table = {}
  max_sum = 0 # the sum of scores from some studnet's top 3 scores.
  max_idx = None
  for [idx, score] in records:
    if idx not in table:
      table[idx] = []
    heapq.heappush(table[idx], score)
    if len(table[idx]) > 3:
      heapq.heappop(table[idx])
  for idx in table:
    if len(table[idx]) == 3:
      cur_sum = sum(table[idx])
      if cur_sum > max_sum: # higher sum means higher average, and we don't need to calculate the average.
        max_sum = cur_sum
        max_idx = idx
  return max_idx

def get_input(case=0):
  import random
  records = [
    ['john', 1],
    ['john', 2],
    ['john', 3],
    ['john', 4],
    ['mary', 5],
    ['mary', 6],
    ['mary', 7],
    ['mary', 8],
    ['bob', 9],
    ['bob', 10],
    ['bob', 11],
    ['bob', 12],
    ['allen', 60],
    ['allen', 60],
  ]
  ans = 'bob'
  if case == 0:
    pass
  return sorted(records, key=lambda x: random.random()), ans


def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    print('Input:')
    records, ans = get_input(case)
    print('records =', records)
    res = get_max_avg_by_top_3(records)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
