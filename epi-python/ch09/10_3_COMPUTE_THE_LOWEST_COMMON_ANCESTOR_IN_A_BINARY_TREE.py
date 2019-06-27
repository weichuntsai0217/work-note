from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first

def lca_helper(node, node_0, node_1):
  """
    The common ancestors satisfies that the number of nodes it finds (num_found)
    from its left subtree and right subtree is 2.
    And the lowest common ancestor is just the first time when num_found is 2 happens.
    The time complexity is O(n)
    The additional space complexity is O(h) where h is the height of the tree.
  """
  if not node:
    return { 'num_found': 0, 'ancestor': None }

  left_res = lca_helper(node.left, node_0, node_1)
  if left_res['num_found'] == 2:
    return left_res
  
  right_res = lca_helper(node.right, node_0, node_1)
  if right_res['num_found'] == 2:
    return right_res

  num_found = left_res['num_found'] + right_res['num_found'] + int(node == node_0) + int(node == node_1)
  return { 'num_found': num_found, 'ancestor': node if num_found == 2 else None}

def get_lca(root, node_0, node_1):
  return lca_helper(root, node_0, node_1)['ancestor']


"""My solution, same time and space complexity with EPI but with more code. However, this method can obtain the search path
def traverse(node, target, ancestors):
  if node:
    if node == target:
      ancestors.append(node)
      return True
    ancestors.append(node)
    if traverse(node.left, target, ancestors):
      return True
    if traverse(node.right, target, ancestors):
      return True
    ancestors.pop()
    return False
  return False

def get_lca(root, node_0, node_1):
  # The time complexity is O(n) where n is the number of the tree nodes.
  # The additional space complexity is O(h) where h is the height of the tree.
  ancestors_0 = []
  ancestors_1 = []
  traverse(root, node_0, ancestors_0)
  traverse(root, node_1, ancestors_1)
  shorter = ancestors_0 if len(ancestors_0) < len(ancestors_1) else ancestors_1
  longer = ancestors_1 if len(ancestors_0) < len(ancestors_1) else ancestors_0
  # print('ancestors_0 =', map(lambda x: x.data, ancestors_0))
  # print('ancestors_1 =', map(lambda x: x. data, ancestors_1))
  
  if shorter[len(shorter) - 1] == longer[len(shorter) - 1]:
    # node_0 is node_1's ancestor or vice versa.
    return shorter[len(shorter) - 1]
  res = shorter[0]
  for i in xrange(1, len(shorter)):
    if shorter[i] != longer[i]:
      res = shorter[i-1]
      break
  return res
"""


def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O']]
  src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  root = gen_binary_tree_breadth_first(src)
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
    res = get_lca(root, node_0, node_1)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('res.data =', res.data)
    print('ans.data =', ans.data)
    print('Test success' if res == ans and res.data == ans.data else 'Test failure')

if __name__ == '__main__':
  main()
