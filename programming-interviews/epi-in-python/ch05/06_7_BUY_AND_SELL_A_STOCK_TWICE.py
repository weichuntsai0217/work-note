from __future__ import print_function

def get_max_profit_twice(x):
  """
    Time complexity is O(n) where n is the length of x
    Additional complexity is O(n) where n is the length of x
  """
  min_price = float('inf')
  max_profit = 0 # max_profit so far.
  forward = []
  for i in xrange(len(x)):
    min_price = min(min_price, x[i])
    max_profit = max(max_profit, x[i]- min_price)
    forward.append(max_profit)

  max_price = 0
  max_profit = 0 # max_profit so far.
  max_combine_profit = 0
  for i in xrange(len(x)-1, 0, -1):
    max_price = max(max_price, x[i])
    max_profit = max(max_profit, max_price - x[i])
    max_combine_profit = max(max_combine_profit, forward[i-1] + max_profit)

  return max_combine_profit


def get_input(case=0):
  if case == 0:
    return [310,315,275,295,260,270,290,230,255,250], 55
  elif case == 1:
    return [12,11,13,9,12,8,14,13,15], 10

def main():
  for arg in xrange(2):
    x, ans = get_input(arg)
    res = get_max_profit_twice(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
