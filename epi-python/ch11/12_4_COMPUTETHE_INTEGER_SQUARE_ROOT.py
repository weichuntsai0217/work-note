from __future__ import print_function

def get_int_sqrt(x):
  """
    The time complexity is O(logx) where x is the input integer.
  """
  l = 0
  h = x
  while l <= h:
    m = l + (h - l) / 2
    product = m * m
    if product <= x:
      l = m + 1
    else:
      h = m - 1
  return l - 1

def get_input(case=0):
  x = 0
  ans = 0
  if case == 0:
    pass
  elif case == 1:
    x = 1
    ans = 1
  elif case == 2:
    x = 2
    ans = 1
  elif case == 3:
    x = 16
    ans = 4
  elif case == 4:
    x = 25
    ans = 5
  elif case == 5:
    x = 300
    ans = 17
  elif case == 6:
    x = 1024
    ans = 32
  elif case == 7:
    x = 3167
    ans = 56
  return x, ans
    

def main():
  for case in xrange(8):
    print('--- case {} ---'.format(case))
    x, ans = get_input(case)
    print('Input:')
    print('x =', x)
    print('Output:')
    res = get_int_sqrt(x)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()


