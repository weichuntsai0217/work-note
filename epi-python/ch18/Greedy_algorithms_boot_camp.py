from __future__ import print_function

def get_min_num_coins_for_change(cents):
  """
    Time complexity is O(1)
  """
  coins = [100, 50, 25, 10, 5, 1] # american coins
  num_of_coins = 0
  for coin in coins:
    num_of_coins += (cents / coin)
    cents %= coin
  return num_of_coins

def get_input(hard=False):
  return 753, 7+1+3

def main():
  for arg in [False]:
    cents, ans = get_input(arg)
    print('Test success' if get_min_num_coins_for_change(cents) == ans else 'Test failure')

if __name__ == '__main__':
  main()
