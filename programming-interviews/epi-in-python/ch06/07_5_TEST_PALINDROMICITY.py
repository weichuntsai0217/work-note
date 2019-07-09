from __future__ import print_function

def is_alphanumeric(c):
  # For alphabet, I only check lower case, please use c = c.lower() before you pass c in this function
  # c.lower() doesn't affect numeric char and other notations.
  d = ord(c)
  if (d >= ord('0')) and (d <= ord('9')):
    return True
  if (d >= ord('a')) and (d <= ord('z')):
    return True
  return False

def test_sentence_palindromicity(s):
  """
    The time complexity is O(n)
    The additional space complexity is O(1)
  """
  if not s: return False # Based on your definition.
  i = 0
  j = len(s) - 1
  while i < j:
    while (not is_alphanumeric(s[i].lower())) and i < j:
      i += 1
    while (not is_alphanumeric(s[j].lower())) and i < j:
      j -= 1
    if s[i].lower() != s[j].lower():
      return False
    i += 1
    j -= 1

  return True

def get_input(case=0):
  if case == 0:
    return 'A man, a plan, a canal, Panama.', True
  elif case == 1:
    return 'Able was I, ere I saw Elba!', True
  elif case == 2:
    return '!!!2!', True
  elif case == 3:
    return 'Ray a Ray', False
  elif case == 4:
    return 'R!~ay a R!@ay', False


def main():
  for case in xrange(5):
    s, ans = get_input(case)
    res = test_sentence_palindromicity(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
