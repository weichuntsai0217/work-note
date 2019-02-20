from __future__ import print_function

def get_min_set_to_cover(intervals):
  """
    Time complexity is O(n * logn) because of sorting
  """
  intervals = sorted(intervals, key=lambda x: x[0])
  # print(intervals)
  sets = [intervals[0]]
  start = sets[0]
  for i in xrange(1, len(intervals)):
    cur = intervals[i]
    if cur[0] <= start[1]:
      start[0] = cur[0]
    else:
      start = cur
      sets.append(start)
  # print(sets) 
  return [item[0] for item in sets]



def get_input(hard=False):
  if hard:
    return [[1,2],[2,3],[2,3],[3,4],[3,4],[4,5]], [2, 4]
    # return [[0, 3], [3, 4], [2, 6], [6, 9], [4, 5], [8, 10]], [3, 4, 8]
  return [[0, 3], [3, 4], [2, 6], [6, 9]], [3, 6]

def main():
  for arg in [False, True]:
    intervals, ans = get_input(arg)
    res = get_min_set_to_cover(intervals)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
