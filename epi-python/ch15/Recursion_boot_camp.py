from __future__ import print_function

def gcd(x, y):
  """
    The time complexity is O(log max(x,y)) because you divide x( or y) at least 2.
    Or you can say the time complexity is O(n) where n is the number of bits representing the inputs. 
    The additional space complexity is O(log max(x,y))
  """
  big = x if x > y else y
  small = y if x > y else x
  return big if small == 0 else gcd(small, big % small)

def gcd_while(x, y):
  """
    The time complexity is O(log max(x,y)) because you divide x( or y) at least 2.
    Or you can say the time complexity is O(n) where n is the number of bits representing the inputs. 
    The additional space complexity is O(1).
  """
  big = x if x > y else y
  small = y if x > y else x
  while small != 0:
    r = big % small
    big = small
    small = r
  return big

def get_input(case=0):
  if case == 0:
    return 156, 36, 12
  elif case == 1:
    return 70, 4, 2

def main():
  print('Use gcd:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    print('Input:')
    x, y, ans = get_input(case)
    print('x =', x)
    print('y =', y)
    print('Output:')
    res = gcd(x, y)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('\n==============')
  print('Use gcd_while:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    print('Input:')
    x, y, ans = get_input(case)
    print('x =', x)
    print('y =', y)
    print('Output:')
    res = gcd_while(x, y)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
