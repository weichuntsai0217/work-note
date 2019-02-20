from __future__ import print_function

def get_max_trap_water(heights):
  """
    Time complexity is O(n) where n is the length of heights.
  """
  max_water = 0
  max_pair = [0, 0]
  i = 0
  j = len(heights) - 1
  while i < j:
    water = min(heights[i], heights[j]) * (j - i)
    if water > max_water:
      max_water = water
      max_pair = [i, j] # this line is not necessary, because we only need to return max_water.
    if heights[i] < heights[j]:
      i += 1
    elif heights[i] > heights[j]:
      j -= 1
    else:
      i += 1
      j -= 1
  return max_water

def get_input(hard=False):
  if hard:
    return [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1], 48 # [4, 16]
  return [1, 2, 1], 2 # [0, 2]

def main():
  for arg in [False, True]:
    heights, ans = get_input(arg)
    res = get_max_trap_water(heights)
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
