from __future__ import print_function

def count_the_number_moves(n, k):
  """
    The time complexity is O(nk)
  """
  cache = []
  for i in xrange(n+1):
    cache.append(-1) # -1 means 'not calculated'
  return get_moves(n, k, cache)
def get_moves(n, k, cache):
  # if n < 0: return 0 # line 17 handles the case n < 0
  if n <= 1: return 1 # if n == 0, then the only 1 way is 'dont move'.
  if cache[n] != -1: return cache[n]
  moves = 0
  for i in xrange(1, k+1):
    if n - i < 0: break
    moves += get_moves(n-i, k, cache)
  cache[n] = moves
  return moves

def get_input(hard=False):
  if hard:
    return 6, 3, 24
  else:
    return 4, 2, 5

def main():
  for arg in [False, True]:
    n, k, ans = get_input(arg)
    expect = count_the_number_moves(n, k)
    print(expect)
    print('Test success' if expect == ans else 'Test failure')

if __name__ == '__main__':
  main()
