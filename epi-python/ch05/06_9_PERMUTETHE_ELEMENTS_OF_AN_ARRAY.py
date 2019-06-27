from __future__ import print_function

def permute(x, p):
  """
    Time complexity is O(n)
    Additional space complexity is O(1)
  """
  for i in xrange(len(x)):
    src_idx = i
    src_val = x[src_idx]
    while (p[src_idx] != None) and (src_idx != p[src_idx]):
      dst_idx = p[src_idx]
      tmp = x[dst_idx]
      x[dst_idx] = src_val
      p[src_idx] = None
      src_idx = dst_idx
      src_val = tmp

    p[i] = None


def get_input(case=0):
  x = ['a', 'b', 'c', 'd']
  p = []
  ans = []
  if case == 0:
    p = [2, 0, 1, 3]
    ans = ['b', 'c', 'a', 'd']
  elif case == 1:
    p = [1, 2, 3, 0]
    ans = ['d', 'a', 'b', 'c']
  elif case == 2:
    p = [0, 2, 3, 1]
    ans = ['a', 'd', 'b', 'c']
  elif case == 3:
    p = [0, 1, 2, 3]
    ans = ['a', 'b', 'c', 'd']
  elif case == 4:
    x.append('e')
    p = [2, 0, 4, 3, 1]
    ans = ['b', 'e', 'a', 'd', 'c']
  return x, p, ans
    
def main():
  for arg in xrange(5):
    x, p, ans = get_input(arg)
    permute(x, p)
    print(x)
    print('Test success' if x == ans else 'Test failure')

if __name__ == '__main__':
  main()
