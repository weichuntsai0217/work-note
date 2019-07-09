from __future__ import print_function
import bst 

def get_lca_in_bst(root, node_0, node_1):
  """
    Assume all keys in the bst are distinct and node_0 & node_1 are indeed in the bst, no further exception should be
    handled.
    The time complexity is O(h) where h is the height of the bst.
    The additional space complexity is O(1)
  """
  res = root
  s = node_0 if node_0.data < node_1.data else node_1
  b = node_1 if node_0.data < node_1.data else node_0
  while (res.data < s.data) or (res.data > b.data):
    while res.data < s.data:
      res = res.right
    while res.data > b.data:
      res = res.left
  return res

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  node_0 = root.left.left
  node_1 = root.left.right.right
  ans = root.left
  if case == 0:
    pass
  elif case == 1:
    node_0 = root.right.left.right
    node_1 = root.right.left.right.left
    ans = node_0
  return root, node_0, node_1, ans


def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, node_0, node_1, ans = get_input(case)
    print('Input:')
    if case == 0:
      print('root =', root)
    print('node_0 =', node_0.data)
    print('node_1 =', node_1.data)
    print('Output:')
    res = get_lca_in_bst(root, node_0, node_1)
    print('res.data =', res.data)
    print('ans.data =', ans.data)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()




