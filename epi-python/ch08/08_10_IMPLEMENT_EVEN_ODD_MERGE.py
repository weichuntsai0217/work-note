from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def even_odd_merge(head):
  """
    The time complexity is O(n) where n is the length of the list
    The additional space complexity is O(1)
  """
  if (not head) or (not head.nxt): return head
  even_head = head
  odd_head = head.nxt
  turn = 0
  tails = [even_head, odd_head]
  while True:
    another = turn ^ 1
    if not tails[another].nxt:
      tails[turn].nxt = tails[another].nxt
      break
    tails[turn].nxt = tails[another].nxt
    tails[turn] = tails[turn].nxt
    turn ^= 1
    
  tails[0].nxt = odd_head
  return even_head

def get_input(case=0):
  def gen_even_odd_array(x):
    res = []
    for i in xrange(0, len(x), 2):
      res.append(x[i])
    for i in xrange(1, len(x), 2):
      res.append(x[i])
    return res

  src = range(case + 1)
  ans_src = gen_even_odd_array(src)
  head = gen_list(src)
  ans = gen_list(ans_src)
  return head, ans

def main():
  for case in xrange(7):
    print('--- case {} ---'.format(case))
    head, ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    res = even_odd_merge(head)
    print('Output:')
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if is_equal(res, None, ans, None) else 'Test failure')

if __name__ == '__main__':
  main()
