from __future__ import print_function

def is_chr_array_palindromic_permutations(chr_array):
  """
    The time complexity is O(n) where n is the length of the chr_array
    The additional space complexity is O(c) where c is the number of distinct characters in the chr_array.
  """
  counts = {}
  for c in chr_array:
    if c not in counts:
      counts[c] = 0
    counts[c] += 1
  odd_counts = 0
  for key in counts:
    if counts[key] & 1:
      odd_counts += 1
      if odd_counts > 1:
        return False
  return True

def get_input(case=0):
  chr_array = list('edified')
  ans = True
  if case == 0:
    pass
  elif case == 1:
    chr_array = list('foobaraboof')
  elif case == 2:
    chr_array = list('foobaeeeraboof')
    ans = False
  return chr_array, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    chr_array, ans = get_input(case)
    print('Input:')
    print('chr_array =', chr_array)
    res = is_chr_array_palindromic_permutations(chr_array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
