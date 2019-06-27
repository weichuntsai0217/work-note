from __future__ import print_function

def get_min_working_time_assign(tasks):
  """
    Time complexity is O(n*logn) because of sorting.
  """
  # The number of tasks must be even.
  tasks = sorted(tasks)
  assign = []
  for i in xrange(len(tasks)/2):
    tail = len(tasks) - i - 1
    assign.append((tasks[i], tasks[tail]))
  return assign

def get_input(hard=False):
  if hard: return [5, 2, 1, 6, 4, 4], [(1, 6), (2, 5), (4, 4)]
  return [1, 8, 9, 10], [(1, 10), (8, 9)]

def main():
  for arg in [False, True]:
    tasks, ans = get_input(arg)
    print('Test success' if get_min_working_time_assign(tasks) == ans else 'Test failure')

if __name__ == '__main__':
  main()
