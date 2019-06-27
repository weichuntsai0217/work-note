from __future__ import print_function

def convert_from_roman_to_decimal(s):
  """
    The problem assumes the input s is a valid Roman number.
    The time complexity is O(n)
    The additional space complexity is O(1)
  """
  table = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }
  res = table[s[len(s) - 1]]
  for i in xrange(len(s)-2, -1, -1):
    if table[s[i]] < table[s[i+1]]:
      res -= table[s[i]]
    else:
      res += table[s[i]]
  return res

def get_input(case=0):
  if case == 0:
    return 'ML', 1050
  elif case == 1:
    return 'XXXXXIIIIIIIII', 59
  elif case == 2:
    return 'LVIIII', 59
  elif case == 3:
    return 'LIX', 59

def main():
  for case in xrange(4):
    s, ans = get_input(case)
    res = convert_from_roman_to_decimal(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
