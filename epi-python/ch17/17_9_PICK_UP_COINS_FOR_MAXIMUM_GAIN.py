from __future__ import print_function

def pickup_coins(coins):
  """
    Time complexity: O(n^2) where n is the number of coins.
  """
  cache = {}
  return max_revenue(coins, 0, len(coins) - 1, cache)

def get_key(a, b):
  return str(a) + '-' + str(b)

def max_revenue(coins, a, b, cache):
  # print('max_revenue is called.')
  if a > b: return 0
  if get_key(a, b) in cache: return cache[get_key(a, b)]

  left_sub_1 = max_revenue(coins, a+2, b, cache)
  left_sub_2 = max_revenue(coins, a+1, b-1, cache)
  pick_left = coins[a] + min(left_sub_1, left_sub_2)
  
  right_sub_1 = left_sub_2 # right_sub_1 and left_sub_2 are the same case (a+1, b-1)
  right_sub_2 = max_revenue(coins, a, b-2, cache)
  pick_right = coins[b] + min(right_sub_1, right_sub_2)
  
  return max(pick_left, pick_right)

def get_input(hard=False):
  if hard:
    return [25, 10, 5, 10, 5, 10, 5, 10, 25, 1], 65
  else:
    return [10, 25, 5, 1, 10, 5], 31

def main():
  for arg in [False, True]:
    coins, ans = get_input(arg)
    expect = pickup_coins(coins)
    print(expect)
    print('Test success' if expect == ans else 'Test failure')

if __name__ == '__main__':
  main()
