from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def pivot_list(head, k):
  """
    As the problem's requirement, the node with the data which is euqal to k must be grouped together.
    The time complexity is O(n) where n is the length of the list
    The additional space complexity is O(1)
  """
  less_head = Node(0, None)
  less_iter = less_head
  equal_head = Node(0, None)
  equal_iter = equal_head
  greater_head = Node(0, None)
  greater_iter = greater_head
  node = head
  while node:
    if node.data < k:
      less_iter.nxt = node
      less_iter = less_iter.nxt
    elif node.data == k:
      equal_iter.nxt = node
      equal_iter = equal_iter.nxt
    elif node.data > k:
      greater_iter.nxt = node
      greater_iter = greater_iter.nxt
    node = node.nxt
  if not equal_head.nxt: return head # the pivot does not exist, just return the original head
  less_iter.nxt = equal_head.nxt
  equal_iter.nxt = greater_head.nxt
  greater_iter.nxt = None
  return less_head.nxt

def get_input(case=0):
  if case == 0:
    head = gen_list([3, 2, 2, 11, 7, 5, 11])
    ans = gen_list([3, 2, 2, 5, 7, 11, 11])
    k = 7
    return head, k, ans
  elif case == 1:
    src = [3, 2, 2, 11, 7, 5, 11]
    head = gen_list(src)
    ans = gen_list(src)
    k = 100
    return head, k, ans
  elif case == 2:
    head = gen_list([3, 2, 19, 2, 11, 7, 8, 5, 11, 4, 7])
    ans = gen_list([3, 2, 2, 5, 4, 7, 7, 19, 11, 8, 11])
    k = 7
    return head, k, ans
  elif case == 3:
    head = gen_list([7, 2, 19, 2, 11, 7, 8, 5, 11, 4, 7])
    ans = gen_list([2, 2, 5, 4, 7, 7, 7, 19, 11, 8, 11])
    k = 7
    return head, k, ans
  elif case == 4:
    head = gen_list([2, 19, 2, 11, 8, 5, 11, 4, 7])
    ans = gen_list([2, 2, 5, 4, 7, 19, 11, 8, 11])
    k = 7
    return head, k, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    print('Input:')
    head, k, ans = get_input(case)
    print('head =', get_list_str(head))
    print('k =', k)
    res = pivot_list(head, k)
    print('Output:')
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if get_list_str(res) == get_list_str(ans) else 'Test failure')

if __name__ == '__main__':
  main()
