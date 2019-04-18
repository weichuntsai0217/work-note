from __future__ import print_function

def make_entries_with_even_value_first(x):
  """
    Time complexity is O(n) where n is the length of the array x.
  """
  even_idx = 0
  odd_idx = len(x) - 1
  while even_idx < odd_idx:
    if (x[even_idx] & 1) == 0:
      even_idx += 1
    else:
      swap = x[even_idx]
      x[even_idx] = x[odd_idx]
      x[odd_idx] = swap
      odd_idx -= 1
  return x

def get_input(hard=False):
  if hard:
    return [3, 1, 2, 4, 9, 6, 5, 8, 7], [8, 6, 2, 4, 9, 5, 1, 7, 3]
  return [1, 2, 3, 4, 5, 6, 7, 8], [8, 2, 6, 4, 5, 7, 3, 1]

def main():
  for arg in [False, True]:
    x, ans = get_input(arg)
    res = make_entries_with_even_value_first(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
