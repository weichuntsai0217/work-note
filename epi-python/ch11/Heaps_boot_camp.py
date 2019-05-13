from __future__ import print_function
import heapq
import random

class MyStr(str):
  def __new__(cls, s):
    return str.__new__(cls, s)
  def __lt__(self, other):
    return len(self) < len(other)
  def __gt__(self, other):
    return len(self) > len(other)
  def __le__(self, other):
    return len(self) <= len(other)
  def __ge__(self, other):
    return len(self) >= len(other)

def compute_k_largest(k, it):
  """
    The time compelxity is O(nlogk) when n is the length of it(number of elements from the iterator it) and k is
      the number means top N largest.
    The space compelxity is O()
  """
  res = []
  while True:
    try:
      x = next(it) # from the problem's spec, it is an iterator which implements next method.
      if len(res) < k:
        heapq.heappush(res, x)
      else:
        heapq.heappushpop(res, x)

    except StopIteration:
      break
  return res

def get_input(case=0):
  if case == 0:
    k = 5
    src = sorted(
      map(
        lambda x: MyStr(x),
        ['asd', 'qazw', 'qwdqsd', 'dshiauen', 'sfheounenoawq', 'rr', 'baeyi', 'pqwuieq', 'adnvajuoe538nca', 'ccc'],
      ),
      key=lambda x: random.random(),
    )
    it = iter(src)
    ans = sorted(src, reverse=True)[:k]
    return src, k, it, ans

def main():
  for case in xrange(1):
    src, k, it, ans = get_input(case)
    print('Input:')
    print('src for it =', src)
    res = sorted(compute_k_largest(k, it), reverse=True)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
