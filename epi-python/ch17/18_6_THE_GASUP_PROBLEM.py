from __future__ import print_function

def get_ample_city(gas_added, distances):
  """
    Time complexity is O(n) where n is the length of gas_added (gas_added and distances have the same length)
    Additional space complexity is O(1)
  """
  """
    This problem assumes that the total gas you get is equal to the total gas you consume.
    and the ample city always exits.
    So when you start from the ample city and finally go back to the ample city,
    your total gas left is 0.
    From the above restriction, no matter what city you start, ignore the impossibility of negative gas,
    the city with min left gas is always the same and it is just the ample city.
  """
  rate = 20 # miles / gallon, this is from the problem's requirement
  candidate = 0
  min_left_gas = 0
  gas_remain = 0
  for i in xrange(1, len(gas_added)):
    gas_remain += gas_added[i-1] - distances[i-1]/rate
    if gas_remain < min_left_gas:
      min_left_gas = gas_remain
      candidate = i
  return candidate

def get_input(hard=False):
  if hard:
    return [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100], 3
  return [30, 25, 10], [400, 600, 200], 0

def main():
  for arg in [False, True]:
    gas_added, distances, ans = get_input(arg)
    res = get_ample_city(gas_added, distances)
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
