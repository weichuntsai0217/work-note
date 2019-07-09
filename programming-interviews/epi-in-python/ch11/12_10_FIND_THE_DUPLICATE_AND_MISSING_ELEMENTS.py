from __future__ import print_function

def find_duplicate_and_missing(x):
  """
    The time complexity is O(n)
    The space complexity is O(1)
  """
  dup_mis_xor = 0
  for i in xrange(len(x)):
    dup_mis_xor ^= (i ^ x[i])
  
  least_diff_bit = dup_mis_xor & (~(dup_mis_xor - 1))
  dup_or_miss = 0
  for i in xrange(len(x)):
    if i & least_diff_bit:
      dup_or_miss ^= i
    if x[i] & least_diff_bit:
      dup_or_miss ^= x[i]

  for item in x:
    if dup_or_miss == item:
      return dup_or_miss, dup_mis_xor ^ dup_or_miss
  return dup_mis_xor ^ dup_or_miss, dup_or_miss

def get_input(case=0):
  import random
  x = None
  duplicate = None
  missing = None
  if case == 0:
    x = [0, 1, 2, 2, 3]
    duplicate = 2
    missing = 4
  elif case == 1:
    x = [1, 2, 3, 4, 4]
    duplicate = 4
    missing = 0
  elif case == 2:
    x = [0, 1, 3, 3, 4]
    duplicate = 3
    missing = 2
  elif case == 3:
    x = [0, 1, 1, 2, 4]
    duplicate = 1
    missing = 3
  return sorted(x, key=lambda x: random.random()), duplicate, missing
 
if __name__ == '__main__':
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    x, ans_dup, ans_mis = get_input(case)
    print('Input:')
    print('x =', x)
    print('Output:')
    res_dup, res_mis = find_duplicate_and_missing(x)
    print('res_dup =', res_dup)
    print('res_mis =', res_mis)
    print('ans_dup =', ans_dup)
    print('ans_mis =', ans_mis)
    print('Test success' if res_dup == ans_dup and res_mis == ans_mis else 'Test failure')

