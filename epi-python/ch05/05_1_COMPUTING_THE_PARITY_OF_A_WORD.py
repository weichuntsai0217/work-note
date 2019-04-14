from __future__ import print_function

def parity(x):
  """
    The problem has assumed that the x is at most 64 bits.
    Time complexity O(logn), where n is the width of x (number of bits)
  """
  x ^= x >> 32
  x ^= x >> 16
  x ^= x >> 8
  x ^= x >> 4
  x ^= x >> 2
  x ^= x >> 1
  return x & 1


def get_input(even=False):
  if even:
    return int('1000100010001000100010001000100010001000100010001000100010001000', 2), 0
  return int(  '1011101110111011101110111011101110111011101110111011101110111010', 2), 1

def main():
  for arg in [False, True]:
    x, ans = get_input(arg)
    res = parity(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
