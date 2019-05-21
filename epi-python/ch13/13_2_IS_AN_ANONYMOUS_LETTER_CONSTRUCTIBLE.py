from __future__ import print_function

def is_anonymous_constructible(ano_text, mag_text):
  """
    The time complexity is O(m + n) where m is the length of ano_text and n is the length of mag_text.
    The additional space complexity is O(c) where c is the number of distinct characters in ano_text.
  """
  ano_table = {}
  for c in ano_text:
    if c not in ano_table:
      ano_table[c] = 0
    ano_table[c] += 1
  for c in mag_text:
    if c in ano_table:
      ano_table[c] -= 1
      if ano_table[c] == 0:
        del ano_table[c]
        if ano_table == {}:
          break
  return ano_table == {}

def get_input(case=0):
  ano_text = 'edified'
  mag_text = 'aedifiedb'
  ans = True
  if case == 0:
    pass
  elif case == 1:
    mag_text = 'aedifedb'
    ans = False
    
  return ano_text, mag_text, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    ano_text, mag_text, ans = get_input(case)
    print('Input:')
    print('ano_text =', ano_text)
    print('mag_text =', mag_text)
    res = is_anonymous_constructible(ano_text, mag_text)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

