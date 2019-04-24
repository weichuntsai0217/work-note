from __future__ import print_function

def encode(s):
  """
    The time complexity is O(n)
  """
  if not s: return ''
  if len(s) == 1: return '1' + s
  res = ''
  i = 0
  for j in xrange(1, len(s)):
    if s[i] != s[j]:
      res += (str(j - i) + s[i])
      i = j
    elif j == (len(s) - 1):
      res += (str(j - i + 1) + s[i])

  return res

def is_number(s):
  if (ord(s) >= ord('0')) and (ord(s) <= ord('9')):
    return True
  return False

def decode(s):
  """
    The time complexity is O(n)
  """
  if len(s) <= 1: return ''
  res = ''
  i = 0
  for j in xrange(1, len(s)):
    if not is_number(s[j]):
      n = int(s[i:j])
      res += (s[j] * n)
      i = j + 1
      
  return res

def get_input_encode(case=0):
  if case == 0:
    return 's', '1s'
  elif case == 1:
    return 'aaaabcccaa', '4a1b3c2a'
  elif case == 2:
    return 'eeeffffee', '3e4f2e'

def get_input_decode(case=0):
  if case == 0:
    return '1s', 's'
  elif case == 1:
    return '4a1b3c2a', 'aaaabcccaa'
  elif case == 2:
    return '3e4f2e', 'eeeffffee'


def main():
  print('Check encode')
  for case in xrange(3):
    s, ans = get_input_encode(case)
    res = encode(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  print('='*10)
  print('Check decode')
  for case in xrange(3):
    s, ans = get_input_decode(case)
    res = decode(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
