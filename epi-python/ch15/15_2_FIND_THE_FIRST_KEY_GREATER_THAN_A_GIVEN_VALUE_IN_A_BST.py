from __future__ import print_function
import bst 

def get_first_greater_key(root, value):
  """
    The time complexity is O(h) where h is the hieght of the tree.
    The additional space complexity is O(1).
  """
  candidate = None
  node = root
  while node:
    if node.data > value:
      candidate = node.data    
      node = node.left
    else:
      node = node.right
  return candidate

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  value = 23
  ans = 29
  if case == 0:
    pass
  elif case == 1:
    value = 100
    ans = None
  return root, value, ans


def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, value, ans = get_input(case)
    print('Input:')
    if case == 0:
      print('root =', root)
    print('value =', value)
    print('Output:')
    res = get_first_greater_key(root, value)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()


