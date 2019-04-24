from __future__ import print_function

def int_to_str(x):
  """
    Time complexity is O(n) where n is the number of digits in x.
    Additional space complexity is O(1) (not including the table/data used by ord and chr function)
  """
  if x != 0 and not x: return None
  res = '' if x != 0 else '0'
  sign = '-' if x < 0 else ''
  if x < 0:
    x = -x
  while x != 0:
    r = x % 10
    res = chr(r + ord('0')) + res
    x /= 10
  return sign + res

def str_to_int(s):
  """
    Time complexity is O(n) where n is string length
    Additional space complexity is O(1) (not including the table/data used by ord function)
  """
  if not s: return None
  res = 0
  sign = -1 if s[0] == '-' else 1
  start = 1 if sign == -1 else 0
  for i in xrange(start, len(s)):
    digit = ord(s[i]) - ord('0')
    res = res * 10 + digit
  return sign * res

def get_input(case=0, is_int_to_str=False):
  if is_int_to_str:
    if case == 0:
      return 123, '123'
    elif case == 1:
      return 29371728, '29371728'
    elif case ==2:
      return -29371728, '-29371728'
    elif case ==3:
      return 0, '0'
  else:
    if case == 0:
      return '123', 123
    elif case == 1:
      return '29371728', 29371728
    elif case ==2:
      return '-29371728', -29371728
    elif case ==3:
      return '0', 0
    

def main():
  for case in xrange(4):
    s, ans = get_input(case)
    res = str_to_int(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  for case in xrange(4):
    x, ans = get_input(case, True)
    res = int_to_str(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
