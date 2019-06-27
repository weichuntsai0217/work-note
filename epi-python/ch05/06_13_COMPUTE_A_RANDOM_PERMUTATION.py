from __future__ import print_function

def swap(x, i, j):
  temp = x[i]
  x[i] = x[j]
  x[j] = temp

def get_random_perm(n):
  """
    Time complexity is O(n) where n is the input number.
  """
  import random
  x = range(n) # Time complexity is O(n)
  for i in xrange(len(x)):
    j = random.randint(i, len(x) - 1) # Time complexity is O(logn)
    swap(x, i, j)
  return x

def get_input(big=False):
  if big:
    return 15
  return 6

def main():
  for arg in [False, True]:
    n = get_input(arg)
    res = get_random_perm(n)
    print(res)

if __name__ == '__main__':
  main()
