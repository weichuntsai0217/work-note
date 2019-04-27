from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def add_list(head_1, head_2):
  """
    The time complexity is O(m + n) where m is the length of list 1 and n is the length of list 2
    The additional space complexity is O(max(m, n))
  """
  node_1 = head_1
  node_2 = head_2
  res_head = Node(0, None)
  res_node = res_head
  ca = 0 # carry
  while node_1 or node_2:
    data_1 = node_1.data if node_1 else 0
    data_2 = node_2.data if node_2 else 0
    tmp = data_1 + data_2 + ca
    res_node.nxt = Node(tmp % 10, None)
    ca = tmp / 10
    if node_1: node_1 = node_1.nxt
    if node_2: node_2 = node_2.nxt
    res_node = res_node.nxt
  if ca > 0:
    res_node.nxt = Node(ca, None)
  return res_head.nxt

def get_input(case=0):
  if case == 0:
    head_1 = gen_list([3, 1, 4])
    head_2 = gen_list([7, 0, 9])
    ans = gen_list([0, 2, 3, 1])
    return head_1, head_2, ans
  elif case == 1:
    head_1 = gen_list([9, 4])
    head_2 = gen_list([7, 0, 9])
    ans = gen_list([6, 5, 9])
    return head_1, head_2, ans
  elif case == 2:
    head_2 = gen_list([9, 4])
    head_1 = gen_list([7, 0, 9])
    ans = gen_list([6, 5, 9])
    return head_1, head_2, ans
  elif case == 3:
    head_1 = gen_list([9, 9])
    head_2 = gen_list([7, 0, 9])
    ans = gen_list([6, 0, 0, 1])
    return head_1, head_2, ans
  elif case == 4:
    head_1 = None
    head_2 = None
    ans = None
    return head_1, head_2, ans
  elif case == 5:
    head_1 = gen_list([7, 0, 9])
    head_2 = None
    ans = gen_list([7, 0, 9])
    return head_1, head_2, ans

def main():
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    print('Input:')
    head_1, head_2, ans = get_input(case)
    print('head_1 =', get_list_str(head_1))
    print('head_2 =', get_list_str(head_2))
    res = add_list(head_1, head_2)
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if get_list_str(res) == get_list_str(ans) else 'Test failure')


if __name__ == '__main__':
  main()
