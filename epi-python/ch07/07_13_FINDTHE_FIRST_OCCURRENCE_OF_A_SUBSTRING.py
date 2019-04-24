from __future__ import print_function

def find_first_substring(s, t):
  """
    The time complexity is O(mn) where m is the length of t and n is the length of s.
  """
  if len(s) > len(t): return -1
  if len(s) == len(t) or len(t) <= 1: return 0 if s == t else -1              

  s_len = len(s)
  for i in xrange(len(t)):
    if s == t[i:i+s_len]: return i
  return -1

def get_input(case=0):
  if case == 0:
    return 'aa', 'a', -1
  elif case == 1:
    return 'bbasd', 'bbasd', 0
  elif case == 2:
    return '', 'a', -1
  elif case == 3:
    return 'a', 'a', 0
  elif case == 4:
    return 'una', 'adhiuenaunadjskunabbuna',  8
  elif case == 5:
    return 'CGC', 'GACGCCA', 2

def main():
  for case in xrange(6):
    s, t, ans = get_input(case)
    res = find_first_substring(s, t)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
