from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def shift_right(head, k):
  """
    The time complexity is O(n) where n is the length of the list.
    The additional space complexity is O(1).
  """
  if not head: return head
  tail = head
  n = 1
  while tail.nxt:
    n += 1
    tail = tail.nxt

  k %= n
  if k == 0: return head
  tail.nxt = head
  steps_to_new_head = n - k
  while steps_to_new_head > 0:
    tail = tail.nxt
    steps_to_new_head -= 1
  new_head = tail.nxt
  tail.nxt = None
  return new_head

def get_input(case=0):
  if case == 0:
    src = [1]
    k = 3
    ans_src = src
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, k, ans
  elif case == 1:
    src = [4,5]
    k = 7
    ans_src = [5,4]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, k, ans
  elif case == 2:
    src = [2,3,5,3,2]
    k = 3
    ans_src = [5,3,2,2,3]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, k, ans
  elif case == 3:
    src = [1,2,3,4,5,6,7]
    k = 4
    ans_src = [4,5,6,7,1,2,3]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, k, ans
  elif case == 4:
    src = [4,5,6]
    k = 4
    ans_src = [6,4,5]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, k, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    head, k, ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    print('k =', k)
    res = shift_right(head, k)
    print('Output:')
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if is_equal(res, None, ans, None) else 'Test failure')



if __name__ == '__main__':
  main()
