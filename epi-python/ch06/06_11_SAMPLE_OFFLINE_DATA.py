from __future__ import print_function

def swap(x, i, j):
  temp = x[i]
  x[i] = x[j]
  x[j] = temp

def get_random_subset(x, size):
  """
    Time complexity is O(size), where size is the number elements in the subset you want.
  """
  import random
  for i in xrange(size):
    j = random.randint(i, len(x) - 1) # randint is O(logN), assume logN is less than size
    swap(x, i, j)

def get_input():
  return [2,3,4,7,1,8], 3

def main():
  x, size = get_input()
  get_random_subset(x, size)
  print(x)

if __name__ == '__main__':
  main()
