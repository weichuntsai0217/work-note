from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first, get_tree_traversal_str

def recursive(preorder, idx):
  if preorder[idx] == None:
    return None, idx + 1
  node = BinaryTreeNode(preorder[idx])
  left, next_idx = recursive(preorder, idx+1)
  right, next_idx = recursive(preorder, next_idx)
  node.left = left
  node.right = right
  return node, next_idx

def get_binary_tree_by_preorder_with_marker(preorder):
  """
    The time complexity is O(n) where n is the number of nodes in the tree.
    The additional space compelxty is O(h) where h is the height of the tree.
  """
  root, next_id = recursive(preorder, 0)
  return root

def get_input(case=0):
  if case == 0:
    preorder = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]
    ans = ','.join(map(lambda x: str(x), preorder))
    return preorder, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    preorder, ans = get_input(case)
    root = get_binary_tree_by_preorder_with_marker(preorder)
    res = get_tree_traversal_str(root, 'preorder', True)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

