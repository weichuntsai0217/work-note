from __future__ import print_function

def find_max_subarray_sum(int_list):
  """
    Time complexity: O(N^2)
    Space complexity: O(N)
  """
  if not isinstance(int_list, list) or len(int_list) == 0: return None
  cache = { -1: 0 }
  for index, item in enumerate(int_list):
    cache[index] = cache[index - 1] + item

  max_sum = int_list[0]
  for i in xrange(len(int_list)):
    for j in xrange(i + 1, len(int_list)):
      tmp = cache[j] - cache[i - 1]
      max_sum = max_sum if tmp <= max_sum else tmp
  return max_sum

def find_max_subarray_sum_quick(int_list):
  """
    Time complexity: O(N)
    Space complexity: O(1)
  """
  if not isinstance(int_list, list) or len(int_list) == 0: return None
  cur_sum = 0
  min_sum = 0
  max_sum = 0
  for i, item in enumerate(int_list):
    cur_sum += item
    if cur_sum < min_sum:
      min_sum = cur_sum
    if cur_sum - min_sum > max_sum:
      max_sum = cur_sum - min_sum
  return max_sum

def get_input(is_smaller=False):
  if is_smaller:
    return [-1, 40, 523, 12, -335, -385, -124, 481, -31]
  return [904, 40, 523, 12, -335, -385, -124, 481, -31]

def main():
  print('Use O(N^2) Algorithm')
  print(find_max_subarray_sum(get_input()) == 1479)
  print(find_max_subarray_sum(get_input(True)) == 575)

  print('====================')

  print('Use O(N) Algorithm')
  print(find_max_subarray_sum_quick(get_input()) == 1479)
  print(find_max_subarray_sum_quick(get_input(True)) == 575)
  

if __name__ == '__main__':
  main()
