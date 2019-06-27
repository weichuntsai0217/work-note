from __future__ import print_function

def has_two_sum(nums, target):
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

def has_three_sum(nums, target):
  """
    Time complexity is O(n^2) where n is the number of nums
  """
  nums = sorted(nums)
  for i in nums:
    if has_two_sum(nums, target - i):
      return True
  return False

def get_input(hard=False):
  if hard:
    return [11, 2, 5, 7, 3], 21, True
  return [11, 2, 5, 7, 3], 100, False

def main():
  for arg in [False, True]:
    nums, target, ans = get_input(arg)
    print('Test success' if has_three_sum(nums, target) == ans else 'Test failure')

if __name__ == '__main__':
  main()
