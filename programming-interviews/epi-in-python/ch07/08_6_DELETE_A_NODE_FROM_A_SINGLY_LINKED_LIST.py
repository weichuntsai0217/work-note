from __future__ import print_function
from utils_ch08 import gen_list, get_list_str, is_equal

def delete_a_node_which_is_not_a_tail(node):
  """
    This problem assumes the node to delete is not a tail.
    The time complexity is O(1).
    The additional complexity complexity is O(1).
  """
  node.data = node.nxt.data
  node.nxt = node.nxt.nxt

def get_input(case=0):
  src = [1,2,3]
  if case == 0:
    head = gen_list(src)
    node = head
    ans = gen_list([2, 3])
    return head, node, ans
  elif case == 1:
    head = gen_list(src)
    node = head.nxt
    ans = gen_list([1, 3])
    return head, node, ans

def main():
  for case in xrange(2):
    head, node, ans = get_input(case)
    print('--- case {} ---'.format(case))
    print('Input:')
    print('head =', get_list_str(head))
    print('node =', get_list_str(node, 1))
    delete_a_node_which_is_not_a_tail(node)
    print('Output:')
    print('head =', get_list_str(head))
    print('Test success' if is_equal(head, 2, ans, 2) else 'Test failure')

if __name__ == '__main__':
  main()
