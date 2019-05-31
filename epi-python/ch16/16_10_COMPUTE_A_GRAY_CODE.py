from __future__ import print_function

def get_gray_code(n):
  """
    The time complexity is O(2^n)
    The additional space complexity is O(n)
  """
  if n == 1:
    return [0, 1]
  res = get_gray_code(n - 1)
  for i in xrange(len(res) - 1, -1, -1):
    res.append((1 << n - 1) | res[i])
  return res

def get_input(case=0):
  n = 2
  ans = ['0', '1', '11', '10']
  if case == 0:
    pass
  elif case == 1:
    n = 3
    ans = ['0', '1', '11', '10', '110', '111', '101', '100']
  elif case == 2:
    n = 4
    ans = ['0', '1', '11', '10', '110', '111', '101', '100', '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']
  return n, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    n, ans = get_input(case)
    print('n =', n)
    print('Output:')
    res = [format(x, 'b') for x in get_gray_code(n)]
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()






