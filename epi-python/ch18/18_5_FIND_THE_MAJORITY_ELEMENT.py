from __future__ import print_function

def find_the_majority_element(strs): 
  """
    Time complexity is O(n), where n is the length of strs.
    Space complexity is O(1)
  """
  # From the problem description, strs must have an str which occurs m times more than half of strs (n elements)
  # That is m/n > 1/2
  if not strs: return None
  candidate = ''
  count = 0
  for s in strs:
    if count == 0:
      candidate = s
    elif s == candidate:
      count += 1
    else:
      count -= 1
  return candidate

def get_input(hard=False):
  if hard:
    return ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a' ,'c', 'a'], 'a'
  return ['b', 'v', 'b'], 'b'

def main():
  for arg in [False, True]:
    strs, ans = get_input()
    print('Test success' if find_the_majority_element(strs) == ans else 'Test failure')

if __name__ == '__main__':
  main()
