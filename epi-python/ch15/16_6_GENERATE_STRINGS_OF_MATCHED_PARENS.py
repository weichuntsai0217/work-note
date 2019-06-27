from __future__ import print_function
from collections import deque

def gen_parens(n):
  """
    The time complexity is (2n)!/(n!(n + 1)!). You must solve C(k + 1) = sum^i=k_i=0 C^k_i/(k+1) in EPI page 293.
    The additional space complexity is O(n^2)
  """
  def recursive(left_needed, right_needed, prefix, res):
    if (left_needed == 0) and (right_needed == 0):
      res.append(prefix)
      return

    if left_needed > 0:
      recursive(left_needed-1, right_needed, prefix + '(', res)

    if left_needed < right_needed:
      recursive(left_needed, right_needed-1, prefix + ')', res)

  res = []
  recursive(n, n, '', res)
  return res
  

def get_input(case=0):
  n = 1
  ans = ['()']
  if case == 0:
    pass
  elif case == 1:
    n = 2
    ans = ['()()', '(())']
  elif case == 2:
    n = 3
    ans = ['((()))', '(()())', '(())()', '()(())', '()()()']
  elif case == 3:
    n = 4
    ans = [
      '(((())))', '((()()))', '((())())', '((()))()', '(()(()))',
      '(()()())', '(()())()', '(())(())', '(())()()', '()((()))',
      '()(()())', '()(())()', '()()(())', '()()()()',
    ]
  return n, ans

def main():
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    print('Input:')
    n, ans = get_input(case)
    print('n =', n)
    print('Output:')
    res = list(gen_parens(n))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()


