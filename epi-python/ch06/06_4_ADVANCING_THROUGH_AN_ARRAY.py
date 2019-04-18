from __future__ import print_function

def can_go_to_end(x):
  """
    Time complexity is O(n)
    Additional space complexity is O(1)
  """
  furtherest_so_far = 0
  last_idx = len(x) - 1
  for i in xrange(0, last_idx):
    if i <= furtherest_so_far:
      furtherest_so_far = max(furtherest_so_far, i + x[i])
  return furtherest_so_far >= last_idx

def get_input(can_go=False):
  if can_go:
    return [3,3,1,0,2,0,1], can_go
  return [3, 2, 0,0, 2, 0,1], can_go

def main():
  for arg in [False, True]:
    x, ans = get_input(arg)
    res = can_go_to_end(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
