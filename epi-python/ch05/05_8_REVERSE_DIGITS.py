from __future__ import print_function

def reverse_digits(x):
  """
    Time complexity is O(n) where n is the number of digits.
  """
  res = 0
  sign = 1
  if x < 0:
    sign = -1
    x = -x

  while x > 0:
    res = res * 10 + x % 10
    x /= 10

  return sign * res

def get_input(case=0):
  if case == 0:
    return 0, 0
  elif case == 1:
    return 2, 2
  elif case == 2:
    return 10, 1
  elif case == 3:
    return 42, 24
  elif case == 4:
    return -1, -1
  elif case == 5:
    return -314, -413
  elif case == 6:
    return -234728, -827432

def main():
  for arg in xrange(7):
    x, ans = get_input(arg)
    res = reverse_digits(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
