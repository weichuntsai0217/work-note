from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first

def recursive(preorder, pre_start, pre_end, in_start, in_end, map_data_to_inorder_idx):
  if (pre_end <= pre_start) or (in_end <= in_start):
    return None
  root_data = preorder[pre_start]
  root_in_idx = map_data_to_inorder_idx[root_data]
  left_subtree_len= root_in_idx - in_start

  return BinaryTreeNode(
    root_data,
    recursive(
      preorder,
      pre_start + 1,
      pre_start + 1 + left_subtree_len,
      in_start,
      root_in_idx,
      map_data_to_inorder_idx,
    ), # left child
    recursive(
      preorder,
      pre_start + 1 + left_subtree_len,
      pre_end,
      root_in_idx + 1,
      in_end,
      map_data_to_inorder_idx,
    ), # right child
  )

def get_binary_tree_from_inorder_preorder(preorder, inorder):
  """
    The time complexity is O(n) where n is the number of nodes in the tree.
    The additional space complexity is O(n)
  """
  map_data_to_inorder_idx = {}
  for i in xrange(len(inorder)):
    map_data_to_inorder_idx[inorder[i]] = i

  return recursive(
    preorder,
    0,
    len(preorder),
    0,
    len(inorder),
    map_data_to_inorder_idx,
  )

def traverse_tree(node, order, res):
  if order == 'preorder':
    if node:
      res.append(node.data)
      traverse_tree(node.left, order, res)
      traverse_tree(node.right, order, res)
  elif order == 'postorder':
    if node:
      traverse_tree(node.left, order, res)
      traverse_tree(node.right, order, res)
      res.append(node.data)
  else: # default is 'inorder'
    if node:
      traverse_tree(node.left, order, res)
      res.append(node.data)
      traverse_tree(node.right, order, res)

def get_tree_traversal_str(root, order='inorder'):
  """
    The time complexity is O(n) where n is the number of nodes of the binary tree.
    The additional space complexity is O(h) where h is the height of ther binary tree.
  """
  res = []
  traverse_tree(root, order, res)

  return ','.join(res)

def get_input(case=0):
  if case == 0:
    ans_preorder = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P'
    ans_inorder = 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
    return ans_preorder.split(','), ans_inorder.split(','), ans_preorder, ans_inorder

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    preorder, inorder, ans_preorder, ans_inorder = get_input(case)
    root = get_binary_tree_from_inorder_preorder(preorder, inorder)
    res_preorder = get_tree_traversal_str(root, 'preorder')
    res_inorder = get_tree_traversal_str(root, 'inorder')
    print('res_preorder =', res_preorder)
    print('ans_preorder =', ans_preorder)
    print('res_inorder =', res_inorder)
    print('ans_inorder =', ans_inorder)
    print('Test success' if res_preorder == ans_preorder and res_inorder == ans_inorder else 'Test failure')
    """
    # case 0 and 1 both based on EPI's page 150
    # case 0 + case 1 in breadth first order
    print(root.data)
    print(root.left.data, root.right.data)
    print(root.left.left.data, root.left.right.data, root.right.left.data, root.right.right.data)
    print(root.left.left.left.data, root.left.left.right.data, root.left.right.left, root.left.right.right.data, root.right.left.left, root.right.left.right.data, root.right.right.left, root.right.right.right.data)
    """
    """
    # case 1 only in breadth first order
    print(root.left.right.right.left.data)
    print(root.right.left.right.left.data)
    print(root.right.left.right.right.data)
    print(root.right.left.right.left.right.data)
    """
    """
    # check case 1 in breadth first order
    print(root.left.right.left)
    print(root.right.left.left)
    print(root.right.right.left)
    print(root.left.left.left.left)
    print(root.left.left.left.right)
    print(root.left.left.right.left)
    print(root.left.left.right.right)
    print(root.left.right.right.right)
    print(root.right.right.right.left)
    print(root.right.right.right.right)
    print(root.right.left.right.left.left)
    print(root.right.left.right.right.left)
    print(root.right.left.right.right.right)
    """

if __name__ == '__main__':
  main()

