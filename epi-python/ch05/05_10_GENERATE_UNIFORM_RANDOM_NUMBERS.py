from __future__ import print_function

def zero_or_one():
  """
    This function is from the problem's spec.
    Please use this in you answer.
  """
  from random import randint
  return randint(0, 1)

def gen_rand(lb, ub): # lb is lower bound, ub is upper bound.
  """
    This problem is a little like to implement python's "randint" function.
    Time complexity is O(log(ub - lb + 1))
  """
  total_outcomes = ub - lb + 1
  res = total_outcomes
  while res >= total_outcomes:
    res = 0
    i = 0
    while (1 << i) < total_outcomes:
      res = (res << 1) | zero_or_one()
      i += 1
  return res + lb

def main():
  for i in xrange(30):
    print(gen_rand(4, 9))

if __name__ == '__main__':
  main()
