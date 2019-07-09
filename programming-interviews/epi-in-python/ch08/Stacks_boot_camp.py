from __future__ import print_function
from utils_ch09 import Node, gen_list, get_list_str, is_equal

def print_linkedlist_in_reverse(head):
  """
    The time complexity is O(n) where n is the length of the list
    The additional space complexity is O(n)
  """
  stack = []
  node = head
  while node:
    stack.append(node.data)
    node = node.nxt

  while stack:
    print(stack.pop())

def get_input(case=0):
  if case == 0:
    return gen_list([1])
  elif case == 1:
    return gen_list([1,2,3,4,5])

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    head = get_input(case)
    print_linkedlist_in_reverse(head)

if __name__ == '__main__':
  main()
