from __future__ import print_function

def find_closest_with_same_weight(x):
  """
    Focus on 64-bit integer is OK.
    Time complexity is O(n) where n is the integer width (here n is 64).
  """
  for i in xrange(63): # Assume the 63th bit is sign bit, this is an acceptable assumption for 2's complement system
    if ((x >> i) & 1) != ((x >> (i+1)) & 1):
      x ^= ((1 << i) | (1 << (i+1)))
      return x

  raise ValueError('x is all 0 or 1')

def get_input(big=False):
  if big:
    return int('11011111', 2), int('11101111', 2)
  return int('110', 2), int('101', 2)

def main():
  for arg in [False, True]:
    x, ans = get_input(arg)
    res = find_closest_with_same_weight(x)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
