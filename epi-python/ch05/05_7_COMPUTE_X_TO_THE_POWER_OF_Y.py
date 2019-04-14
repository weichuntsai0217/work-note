from __future__ import print_function

def power(x, y):
  """
    Time complexity is O(n) where n is the integer width (ex: 64-bit)
  """
  if y == 0: return 1
  if y < 0:
    y = -y
    x = 1.0 / x
  res = 1.
  mask = 1
  cache = x
  while mask <= y:
    if (mask & y) != 0:
      res *= cache
    cache *= cache
    mask <<= 1
  return res

def get_input(big=False, negative=False):
  if big:
    if negative:
      return 5, -12, 1. / 244140625, 1e-9
    return 5, 12, 244140625, 0
    
  else:
    if negative:
      return 3, -5, 1. / 243, 1e-6
    return 3, 5, 243, 0

def main():
  for arg1, arg2 in [(False, False), (False, True), (True, False), (True, True)]:
    x, y, ans, delta = get_input(arg1, arg2)
    res = power(x, y)
    print(res)
    print('Test success' if abs(res - ans) <= delta else 'Test failure')

if __name__ == '__main__':
  main()
