from __future__ import print_function

def has_two_sum(nums, target): # assume nums has been sorted.
  """
    Time complexity is O(n), where n is the number of nums.
  """
  i = 0
  j = len(nums) - 1
  while i <= j:
    if nums[i] + nums[j] == target:
      return True
    elif nums[i] + nums[j] < target:
      i += 1
    else:
      j -= 1
  return False

def get_input(hard=False):
  if hard:
    return [-2, 1, 2, 4, 7, 11], 6, True
  return [-2, 1, 2, 4, 7, 11], 100, False

def main():
  for arg in [False, True]:
    nums, target, ans = get_input(arg)
    print('Test success' if has_two_sum(nums, target) == ans else 'Test failure')


if __name__ == '__main__':
  main()
