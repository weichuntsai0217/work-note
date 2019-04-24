from __future__ import print_function

def is_palindromic(s):
  """
    Time complexity is O(n) where n is the string length.
    Additional space complexity is O(1)
  """
  if not s: return False
  last_idx = len(s) - 1
  for i in xrange(len(s)/2):
    if s[i] != s[last_idx - i]:
      return False
  return True

def get_input(case=0):
  if case == 0:
    return 'a', True
  elif case == 1:
    return 'asdfdsa', True
  elif case == 2:
    return 'asdffdsa', True
  elif case == 3:
    return 'asdffsa', False

def main():
  for case in xrange(4):
    s, ans = get_input(case)
    res = is_palindromic(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
