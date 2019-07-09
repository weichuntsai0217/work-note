from __future__ import print_function

def reverse_digits(x):
  res = 0
  sign = 1
  if x < 0:
    x = -x
    sign = -1
  
  while x > 0:
    res = res * 10 + (x % 10)
    x /= 10

  return res

def is_palindrome_int(x):
  """
    If the interviewer doesn't allow you to use string.
    Time complexity is O(n) where n is the number of digits in x
    Additional space complexity is O(1)
  """
  if x < 0: return False # from the problem's spec, negative number is not a palindrome.
  return x == reverse_digits(x)

def is_palindrome_int_by_str(x):
  """
    If the interviewer allows you to use string.
    Time complexity is O(n) where n is the number of digits in x
    Addtional space complexity is O(n) where n is the number of digits in x
  """
  if x < 0: return False # from the problem's spec, negative number is not a palindrome.
  s = str(x)
  l = len(s) - 1
  m = len(s) / 2
  for i in xrange(m):
    if s[i] != s[l-i]:
      return False
  return True

def get_input(case=0):
  if case == 0:
    return 0, True
  elif case == 1:
    return 1, True
  elif case == 2:
    return 7, True
  elif case == 3:
    return 11, True
  elif case == 4:
    return 121, True
  elif case == 5:
    return 333, True
  elif case == 6:
    return 2147447412, True
  elif case == 7:
    return -1, False
  elif case == 8:
    return 12, False
  elif case == 9:
    return 100, False
  elif case == 10:
    return 2147483642, False

def main():
  print('Use is_palindrome_int:')
  for arg in xrange(11):
    x, ans = get_input(arg)
    res = is_palindrome_int(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  print('Use is_palindrome_int_by_str:')
  for arg in xrange(11):
    x, ans = get_input(arg)
    res = is_palindrome_int_by_str(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
