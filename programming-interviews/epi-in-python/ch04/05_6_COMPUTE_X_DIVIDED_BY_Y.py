from __future__ import print_function

def divide(x, y):
  """
    Time complexity is O(n) where n is the width of x (ex: 64-bit)
  """
  if y == 0: raise ValueError('Can not divide x by zero.')
  q = 0
  power = 0
  while x >= y:
    if (y << (power + 1)) > x:
      break
    else:
      power += 1
  y_power = y << power
  while x >= y:
    if x >= y_power:
      x -= y_power
      q += (1 << power)
    y_power >>= 1
    power -= 1
  return q

def get_input(big=False):
  if big:
    return int('1011010110111101', 2), int('101101', 2), int('10000001001', 2)
  return int('10101', 2), int('100', 2), int('101', 2)

def main():
  for arg in [False, True]:
    x, y, ans = get_input(arg)
    res = divide(x, y)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
