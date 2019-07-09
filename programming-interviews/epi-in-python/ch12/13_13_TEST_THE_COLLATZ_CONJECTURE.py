from __future__ import print_function
import heapq

def test_collatz_conjecture_for_first_n(n):
  """
    The time complexity is at least proportional to n.
    But we don't know in what order.
  """
  known_cache = { 1: True } # 1 satisfies collatz_conjecture and we only record odd numbers.
  for i in xrange(3, n+1, 2):
    inf_loop_candidates = {}
    k = i
    while k >= i:
      """
        known_cache only records all odd numbers less than i.
        This program guarantees that all numbers in known_cache satisfy collatz_conjecture
        because if some odd number i does not satisfy collatz_conjecture, this program would
        return False immediately and would not check i+2, i+4, i+6, etc.
        So all numbers less than i meet collatz conjecture.
      """
      if k in inf_loop_candidates:
        # Infinity loop happens.
        return False
      else:
        inf_loop_candidates[k] = True

      if k & 1:
        if k in known_cache:
          break
        else:
          """
            This part is a little tricky.
            For example, if i = 3, then the converge process is
            3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
            You might wonder when we test 3, why we add 5 into known_cache before we proved 3 meets collatz_conjecture?
            This is because if 3 meets collatz_conjecture, so as 5 (if i = 5, the process is 5 -> 16 -> 8 -> 4 -> 2 -> 1);
            and if 3 does not meets collatz_conjecture, this program would return False immediately
            and we would not check 5, 7, 9, etc. So we can add 5 first to gain some performance.
          """
          known_cache[k] = True

        try:
          next_k = 3 * k + 1
        except OverflowError:
          return False
          
        k = next_k
      else:
        k >>= 1
  return True

def get_input(case=0):
  n = 100
  ans = True
  if case == 0:
    pass
  elif case == 1:
    n = 1000
  elif case == 2:
    n = 10000
  return n, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    n, ans = get_input(case)
    print('n =', n)
    res = test_collatz_conjecture_for_first_n(n)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

