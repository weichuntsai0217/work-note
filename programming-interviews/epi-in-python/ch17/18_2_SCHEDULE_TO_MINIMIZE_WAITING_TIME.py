from __future__ import print_function

def get_min_waiting_time(queries):
  """
    Time complexity is O(n*logn) becaue of sorting
  """
  queries = sorted(queries)
  total_wait_time = 0
  for i in xrange(len(queries) - 1):
    total_wait_time += (len(queries) - i - 1) * queries[i]
  return total_wait_time

def get_input(hard=False):
  if hard:
    return [2, 5, 1, 3, 7, 9, 4], 57
  return [2, 5, 1, 3], 10

def main():
  for arg in [False, True]:
    queries, ans = get_input(arg)
    res = get_min_waiting_time(queries)
    print(res)
    print('Test success' if res == ans else 'Test failure')
if __name__ == '__main__':
  main()
