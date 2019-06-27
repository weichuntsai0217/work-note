from __future__ import print_function

SMALLER = 0
EQUAL = 1
LARGER = 2

def compare(a, b, precision=1e-5):
  global SMALLER
  global EQUAL
  global LARGER
  diff = (a - b) / b
  if diff < (-precision):
    return SMALLER
  elif diff > precision:
    return LARGER
  else:
    return EQUAL

def get_real_sqrt(x, precision=1e-5):
  """
    The time complexity is O(log (x / s)) where s = x * precision is the tolerance.
  """
  if x == 0.: return x
  global SMALLER
  global EQUAL
  global LARGER
  l = 1.
  h = x
  if x < 1.:
    l = x
    h = 1.
  while compare(l, h) == SMALLER:
    m = l + (h - l) * 0.5
    product = m * m
    if compare(product, x) == EQUAL:
      return m
    elif compare(product, x) == LARGER:
      h = m
    else:
      l = m
  return l
    

def get_input(case=0):
  x = 0.
  if case == 0:
    pass
  elif case == 1:
    x = 1.
  elif case == 2:
    x = 2.
  elif case == 3:
    x = 16.
  elif case == 4:
    x = 25.
  elif case == 5:
    x = 300.
  elif case == 6:
    x = 1024.
  elif case == 7:
    x = 3167.
  elif case == 8:
    x = 0.25
  ans = x ** 0.5
  return x, ans
    

def main():
  global EQUAL
  for case in xrange(9):
    print('--- case {} ---'.format(case))
    x, ans = get_input(case)
    print('Input:')
    print('x =', x)
    print('Output:')
    res = get_real_sqrt(x)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if (res == ans) or (compare(res, ans) == EQUAL) else 'Test failure')


if __name__ == '__main__':
  main()



