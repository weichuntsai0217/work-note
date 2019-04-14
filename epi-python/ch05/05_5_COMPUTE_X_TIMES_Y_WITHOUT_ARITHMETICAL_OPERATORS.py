from __future__ import print_function

def multiply(x, y):
  """
    Time complexity is O(n^2) where n is the width of the number (ex: 64-bit digits)
  """
  if  x == 0 or y == 0: return 0
  res = 0
  while y != 0:
    if y & 1 != 0:
      res = addition(res , x)
    x <<= 1
    y >>= 1
  return res

def addition(a, b):
  """
    Time complexity is O(n) where n is the width of the number (ex: 64-bit digits)
  """
  tmp_a = a
  tmp_b = b
  k = 1
  ca = 0 # carry in the current digit
  res = 0
  while tmp_a != 0 or tmp_b != 0:
    ak = a & k
    bk = b & k
    res |= (ak ^ bk ^ ca)
    ca = ((ak & bk) | (ak & ca) | (bk & ca)) << 1 # update ca for the next digit.
    tmp_a >>= 1
    tmp_b >>= 1
    k <<= 1

  return res | ca # make sure the result is correct when carry happens in the highest digit

def get_input(big=False):
  if big:
    return 7, 7, 49
  return 5, 6, 30

def main():
  for arg in [False, True]:
    x, y, ans = get_input(arg)
    res = multiply(x, y)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
