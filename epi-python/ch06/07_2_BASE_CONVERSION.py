from __future__ import print_function

def base_conversion(s, b_src, b_dst):
  """
    Time complexity is O(n(1 + log(b_src, b_dst)))
    where n is the length of s and log(b_src, b_dst) is log b_src with base b_dst
    Additional space complexity is O(1)
  """
  if not s: return None
  if s == '0': return s
  res = ''
  number = 0
  sign = '-' if s[0] == '-' else ''
  start = 1 if sign == '-' else 0
  table = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
  }

  for i in xrange(start, len(s)):
    digit = table[s[i]] if s[i] in table else ord(s[i]) - ord('0')
    number = number * b_src + digit

  while number != 0:
    """
      The time complexity of this loop is math.floor(math.log(number, b_dst))+1 because
      the number of digits is the total loop time.
      If you want to know how many digits of a number(in decimal, that is base 10) under some base,
      just take log with the base you want.
      Ex: Let's consider a number 1024 in decimal(base 10), then
        1. Under base 10, the number of digits of 1024 is math.floor(math.log(1024, 10)) + 1 = 4
        2. Under base 2, the number of digits of 1024 is math.floor(math.log(1024, 2)) + 1 = 11
    """
    r = number % b_dst
    res = (table[r] if r in table else chr(r + ord('0')))+ res
    number /= b_dst

  return sign + res

def get_input(case=0):
  if case == 0:
    return '615', 7, 13, '1A7'
  elif case == 1:
    return '0', 7, 13, '0'
  elif case == 2:
    return '-615', 7, 13, '-1A7'

def main():
  for case in xrange(3):
    s, b_src, b_dst, ans = get_input(case)
    res = base_conversion(s, b_src, b_dst)
    print(res)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
