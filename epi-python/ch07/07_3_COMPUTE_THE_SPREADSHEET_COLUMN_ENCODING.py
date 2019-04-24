from __future__ import print_function

def get_spreadsheet_col_integer_id(s):
  """
    The time complexity is O(n) where n is the string length
  """
  res = 0
  offset = (ord('A') - 1)
  for c in s:
    digit = ord(c) - offset
    res = res * 26 + digit
  return res

def variant_1_get_spreadsheet_col_integer_id_from_zero(s):
  return get_spreadsheet_col_integer_id(s) - 1

def variant_2_get_spreadsheet_col_alphabet_id(x):
  """
    The time complexity is O(math.log(x, 26))
  """
  def get_single_alphabet(digit):
    if digit == 0: return 'Z' # 0 -> 'Z'
    offset = ord('A') - 1
    return chr(digit + offset) # 1 -> 'A', 2 -> 'B', ..., 25 -> 'Y'
  res = ''
  while x != 0:
    r = x % 26
    c = get_single_alphabet(r)
    if r == 0:
      x -= 26
    res = c + res
    x /= 26
  return res

def get_input(case=0):
  if case == 0:
    return 'A', 1
  elif case == 1:
    return 'D', 4
  elif case == 2:
    return 'Z', 26
  elif case == 3:
    return 'AA', 27
  elif case == 4:
    return 'FJ', 166
  elif case == 5:
    return 'ZZ',  702
  elif case == 6:
    return 'AAA', 703
  elif case == 7:
    return 'FJU', 4337
  elif case == 8:
    return 'ZZZ', 18278
  elif case == 9:
    return 'ZAZ', 17628
  elif case == 10:
    return 'AZZ', 1378

def main():
  print('Change alphabet id to integer id')
  for case in xrange(11):
    s, ans = get_input(case)
    res = get_spreadsheet_col_integer_id(s)
    print(res)
    print('Test success' if res == ans else 'Test failure')
  print('=====')
  print('Change integer id to alphabet id')
  for case in xrange(11):
    ans, x = get_input(case)
    res = variant_2_get_spreadsheet_col_alphabet_id(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')
if __name__ == '__main__':
  main()
