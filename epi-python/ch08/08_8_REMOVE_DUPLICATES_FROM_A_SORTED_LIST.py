from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def remove_duplicates_from_a_sorted_list(head):
  """
    The time complexity is O(n)
    The additional space complexity is O(1)
  """
  dummy_head = Node(0, head)
  node = dummy_head
  test_val = False
  while node.nxt:
    if test_val == False:
      test_val = node.nxt.data
      node = node.nxt
    elif test_val == node.nxt.data:
      node.nxt = node.nxt.nxt
    else:
      test_val = False
  return dummy_head.nxt

def get_input(case=0):
  if case == 0:
    src = [1]
    ans_src = src
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, ans
  elif case == 1:
    src = [2,2,3,5,7,11,11]
    ans_src = [2,3,5,7,11]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, ans
  elif case == 2:
    src = [2,3,3,3,5,7,11,11,13]
    ans_src = [2,3,5,7,11,13]
    head = gen_list(src)
    ans = gen_list(ans_src)
    return head, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    head, ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    res = remove_duplicates_from_a_sorted_list(head)
    print('Output:')
    print('head =', get_list_str(res))
    print('Test success' if is_equal(head, None, ans, None) else 'Test failure')


if __name__ == '__main__':
  main()
