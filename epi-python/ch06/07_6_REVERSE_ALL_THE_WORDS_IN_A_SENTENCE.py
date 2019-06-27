from __future__ import print_function

def find_word_start_and_end(s, i):
  while i < len(s) and s[i] == ' ':
    i += 1
  j = i
  while j < len(s) and s[j] != ' ':
    j += 1
  return i, j



def reverse_string_ary(s): # s is a string array, and would be reversed in-place.
  """
    The time complexity is O(n) where n is the length of s
    The additional space complexity is O(1) where n is the length of s
  """
  s.reverse()
  i = 0
  while i < len(s):
    start, end = find_word_start_and_end(s, i)
    mid = (start + end)/2
    invariant = start + end - 1
    for j in xrange(start, mid): # the last word index is end - 1, end - start is the word length
      tmp = s[j]
      s[j] = s[invariant - j]
      s[invariant - j] = tmp
    i = end

def reverse_string(s):
  """
    The time complexity is O(n) where n is the length of s.
    The additional space complexity (including the output) is O(n), because python's string is immutable.
  """
  ary = s.split() # python string split use continuous white spaces as seperator by default.
  ary.reverse()
  return ' '.join(ary)

def reverse_string_strict_space(s):
  """
    If you wan to reverse 'Alice   likes Bob' to  'Bob likes   Alice' (the continuous space length is different)
    Please use this function.
    The time complexity is O(n) where n is the length of s.
    The additional space complexity (including the output) is O(n), because python's string is immutable.
  """
  import re
  ary = s.split() # python string split use continuous white spaces as seperator by default.
  sps = filter(lambda x: bool(x), re.split('[a-zA-Z0-9]', s))
  ary.reverse()
  sps.reverse()
  res = []
  for i in xrange(len(ary)):
    res.append(ary[i])
    if i < len(sps):
      res.append(sps[i])
  return ''.join(res)

def get_input(case=0, use_array=False):
  if case == 0:
    s = 'Alice likes Bob'
    ans = 'Bob likes Alice'
    if use_array:
      return list(s), list(ans)
    return s, ans
  elif case == 1:
    s = 'Alice   likes Bob'
    ans = 'Bob likes   Alice'
    if use_array:
      return list(s), list(ans)
    return s, ans
def main():
  print('Use reverse_string')
  for case in xrange(1):
    s, ans = get_input(case)
    res = reverse_string(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  print('='*10)
  print('Use reverse_string_strict_space')
  for case in xrange(2):
    s, ans = get_input(case)
    res = reverse_string_strict_space(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  print('='*10)
  print('reverse_string_ary')
  for case in xrange(2):
    s, ans = get_input(case, True)
    reverse_string_ary(s)
    print(s)
    print('Test success' if s == ans else 'Test failure')
    
if __name__ == '__main__':
  main()
