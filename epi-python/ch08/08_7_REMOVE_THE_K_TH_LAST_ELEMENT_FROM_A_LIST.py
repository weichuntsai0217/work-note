from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal


def remove_the_k_th_last_element(head, k):
  """
    From the problem, you can not store the length of the list.
    We assume the input k is always valid for list (no out-of-range).
    The time complexity is O(n).
    The additional space complexity is O(1).
  """
  dummy_head = Node(0, head)
  end = dummy_head.nxt
  while k > 0:
    end = end.nxt
    k -= 1
  start = dummy_head
  while end:
    start = start.nxt
    end = end.nxt
  start.nxt = start.nxt.nxt
  return dummy_head.nxt

def get_input(case=0):
  if case == 0:
    head = gen_list([1])
    k = 1
    ans = None
    len_ans = 0
    return head, k, ans, len_ans
  elif case == 1:
    head = gen_list([1, 2])
    k = 1
    ans = gen_list([1])
    len_ans = 1
    return head, k, ans, len_ans
  elif case == 2:
    head = gen_list([1, 2, 3])
    k = 1
    ans = gen_list([1, 2])
    len_ans = 2
    return head, k, ans, len_ans
  elif case == 3:
    head = gen_list([1, 2, 3, 4])
    k = 2
    ans = gen_list([1, 2, 4])
    len_ans = 3
    return head, k, ans, len_ans
  elif case == 4:
    head = gen_list([1, 2, 3, 4])
    k = 3
    ans = gen_list([1, 3, 4])
    len_ans = 3
    return head, k, ans, len_ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    head, k, ans, len_ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    print('k =', k)
    res = remove_the_k_th_last_element(head, k)
    print('Output:')
    print('res =', get_list_str(res))
    print('Test success' if is_equal(res, len_ans, ans, len_ans) else 'Test failure')


if __name__ == '__main__':
  main()
