from __future__ import print_function

def get_sinusoidal_str(s):
  """
    Time complexity is O(n) where n is the length of s
  """
  res = []
  for i in xrange(1, len(s), 4):
    res.append(s[i])

  for i in xrange(0, len(s), 2):
    res.append(s[i])

  for i in xrange(3, len(s), 4):
    res.append(s[i])

  return ''.join(res)

def get_input(case=0):
  if case == 0:
    return 'Hello World!', 'e lHloWrdlo!'

def main():
  for case in xrange(1):
    s, ans = get_input(case)
    res = get_sinusoidal_str(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
