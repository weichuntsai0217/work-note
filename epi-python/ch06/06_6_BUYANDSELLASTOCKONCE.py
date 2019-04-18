from __future__ import print_function

def get_max_profit(x):
  """
    Time complexity is O(n) where n is the length of x
  """
  max_profit = 0
  min_price = float('inf')
  for p in x:
    max_profit = max(max_profit, p - min_price)
    min_price = min(min_price, p)
  return max_profit


def get_input(case=0):
  if case == 0:
    return [310,315,275,295,260,270,290,230,255,250], 30 
  elif case == 1:
    return [12,11,13,9,12,8,14,13,15], 7

def main():
  for arg in xrange(2):
    x, ans = get_input(arg)
    res = get_max_profit(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
