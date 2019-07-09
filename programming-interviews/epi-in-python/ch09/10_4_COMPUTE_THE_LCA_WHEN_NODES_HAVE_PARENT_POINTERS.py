from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first

def get_height(node):
  h = 0
  while node.parent:
    h += 1
    node = node.parent
  return h

def get_lca_with_parent_field(root, node_0, node_1):
  """
    The time complexity is O(h) where h is the height of the tree.
    The additional space complexity is O(1).
  """
  h_0 = get_height(node_0)
  h_1 = get_height(node_1)
  diff = abs(h_0 - h_1)
  deep = node_0 if h_0 > h_1 else node_1
  shallow = node_1 if h_0 > h_1 else node_0
  while diff != 0:
    deep = deep.parent
    diff -= 1
  while deep != shallow:
    deep = deep.parent
    shallow = shallow.parent
  return deep

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O']]
  src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  root = gen_binary_tree_breadth_first(src, True)
  node_0 = None
  node_1 = None
  ans = None
  if case == 0:
    node_0 = root.left.left.left
    node_1 = root.right.right.right
    ans = root
  elif case == 1:
    node_0 = root.left.right.right
    node_1 = root.right.left.right.left
    ans = root
  elif case == 2:
    node_0 = root.right.left.right.left.right # 'M'
    node_1 = root.right.left.right.right # 'N'
    ans = root.right.left.right # 'K'
  elif case == 3:
    node_0 = root.left.left # 'C'
    node_1 = root.left.right.right.left # 'H'
    ans = root.left # 'B'
  elif case == 4:
    node_0 = root.left.right # 'F'
    node_1 = root.left.right.right.left # 'H'
    ans = root.left.right # 'F'
  return root, node_0, node_1, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    root, node_0, node_1, ans = get_input(case)
    print('Input:')
    print('node_0.data =', node_0.data)
    print('node_1.data =', node_1.data)
    res = get_lca_with_parent_field(root, node_0, node_1)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('res.data =', res.data)
    print('ans.data =', ans.data)
    print('Test success' if res == ans and res.data == ans.data else 'Test failure')

if __name__ == '__main__':
  main()
