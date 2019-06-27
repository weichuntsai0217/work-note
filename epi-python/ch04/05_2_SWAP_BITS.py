from __future__ import print_function

def swap_bits(x, i, j):
  """
    Time complexity is O(1)
  """
  if (x >> i & 1) != (x >> j & 1):
    mask = (1 << i) | (1 << j)
    return x ^ mask
  return x

def get_input(big=False, same_digit=None):
  if big:
    x = int('0101110101001001', 2)
    i = 3
    j = 13
    ans = int('0111110101000001', 2)
    if same_digit == 0:
      i = 2
      j = 13
      ans = x
    elif same_digit == 1:
      i = 3
      j = 12
      ans = x
    return x, i, j, ans
  else:
    x = int('01001001', 2)
    i = 1
    j = 6
    ans = int('00001011', 2)
    if same_digit == 0:
      i = 1
      j = 4
      ans = x
    elif same_digit == 1:
      i = 3 
      j = 6
      ans = x
    return x, i, j, ans

def main():
  for (arg1, arg2) in [(False, None), (False, 0), (False, 1), (True, None), (True, 0), (True, 1)]:
    x, i, j, ans = get_input(arg1, arg2)
    res = swap_bits(x, i, j)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
