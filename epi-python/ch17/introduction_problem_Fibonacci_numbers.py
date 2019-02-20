from __future__ import print_function


def get_fbn(n, use_bottom_up=False): # fbn means Fibonacci number
  if not isinstance(n, int) or n < 0: return None
  if use_bottom_up:
    return fbn_bottom_up(n)
  cache = {}
  return fbn_top_down(n, cache)

def fbn_bottom_up(n):
  """
    Time complexity: O(n)
    Space complexity: O(1) => because we don't need to save every Fibonacci number.
  """
  if n <= 1: return n
  n_minus_2 = 0
  n_minus_1 = 1
  for i in xrange(2, n+1):
    n_target = n_minus_2 + n_minus_1
    n_minus_2 = n_minus_1
    n_minus_1 = n_target
  return n_minus_1

def fbn_top_down(n, cache):
  """
    Time complexity: O(n)
    Space complexity: O(n)
  """
  if n <= 1: return n
  if n not in cache:
    cache[n] = fbn_top_down(n - 2, cache) + fbn_top_down(n - 1, cache)
  return cache[n]

def main():
  print('Use top down')
  n = 20
  res = []
  for i in xrange(n+1):
    res.append(get_fbn(i))
  print(res)
  print('\n==============\n')
  print('Use bottom up')
  n = 20
  res = []
  for i in xrange(n+1):
    res.append(get_fbn(i, True))
  print(res)

if __name__ == '__main__':
  main()
