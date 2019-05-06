from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def get_inorder_successor(node):
  """
    The time complexity is O(h) where h is the height of the tree.
    The additional space complexity is O(1).
  """
  if not node: return None
  if node.right:
    # find the left-most node in the right subtree of this input node.
    node = node.right
    while node.left:
      node = node.left
    return node
  else:
    # This input node is the right-most node of the left subtree of the ancestor we want.
    # = Find the closest ancestor whose left subtree contains node
    # = Find the 1st ancestor which tends to go to the right-hand side of the input node.
    while node.parent and node == node.parent.right:
      node = node.parent
    return node.parent


def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  node = None
  ans = None
  # order = 'inorder'
  # The sequence is 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
  if case == 0:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.left.left.left # 'D'
    ans = root.left.left # 'C'
  elif case == 1:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.left.right.right # 'G'
    ans = root # 'A'
  elif case == 2:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root # 'A'
    ans = root.right.left # 'J'
  elif case == 3:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.left # 'B'
    ans = root.left.right # 'F'
  elif case == 4:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.left.right # 'F'
    ans = root.left.right.right.left # 'H'
  elif case == 5:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.right.left.right.right # 'N'
    ans = root.right # 'I'
  elif case == 6:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    node = root.right.right.right # 'P'
    ans = None
  return node, ans

def main():
  for case in xrange(7):
    print('--- case {} ---'.format(case))
    node, ans = get_input(case)
    print('Input:')
    print('node.data =', node.data)
    res = get_inorder_successor(node)
    print('Output:')
    print('res.data =', res.data if res else res)
    print('ans.data =', ans.data if ans else ans)
    print('Test success' if (res == ans) else 'Test failure')
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

