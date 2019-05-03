from __future__ import print_function

def can_view_sunset(heights):
  """
    The problem forces you to iterate buildings from east to west.
    If index = 0 is the west side and index = len(heights) - 1 is the east side,
    then you have to run from index = len(heights) - 1.
    The time complexity is O(n) where n is the length of heights.
    The additional space complexity is O(n) including the return value.
  """
  if not heights: return []
  last_idx = len(heights) - 1
  stack = [(last_idx, heights[last_idx])] # each element in stack is  (index, height)
  for i in xrange(last_idx - 1, -1, -1):
    while stack and heights[i] >= stack[-1][1]:
      stack.pop()
    stack.append((i, heights[i]))
  return stack

def get_input(case=0):
  if case == 0:
    return [10], [(0, 10)]
  elif case == 1:
    return [10,40,70,20,50,80,30,60,90], [(8, 90), (5, 80), (2, 70), (1, 40), (0, 10)]
  elif case == 2:
    return [10,20,30,40,50], [(4, 50), (3, 40), (2, 30), (1, 20), (0, 10)]
  elif case == 3:
    return [50, 40, 30, 20, 10], [(0, 50)]

def main():
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    print('Input:')
    heights, ans = get_input(case)
    print('heights =', heights)
    res = can_view_sunset(heights)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
