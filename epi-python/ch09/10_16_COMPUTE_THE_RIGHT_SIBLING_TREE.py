from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first, get_tree_traversal_str
from collections import deque

def set_level_next(root): # root is a perfect binary tree from the problem's spec.
  """
    The time complexity is O(n) where n is the number of nodes in the tree.
    And becuase the input is a perfect binary tree, n = 2^(h+1) - 1 where h is the height of the tree.
    h = math.floor(math.log(n, 2))
    The additional space complexity is O(2^h) that is the number of nodes in the max level
  """
  if not root: return None
  queue = deque([root])
  while queue:
    level_nodes = deque([])
    while queue:
      parent = queue.popleft()
      if len(queue) > 0:
        parent.level_next = queue[0]
      else:
        parent.level_next = None
      if parent.left: level_nodes.append(parent.left)
      if parent.right: level_nodes.append(parent.right)
    queue = level_nodes
  return root

def set_level_next_less_space(root): # root is a perfect binary tree from the problem's spec.
  """
    The time complexity is O(n) where n is the number of nodes in the tree.
    The additional space complexity is O(1)
  """
  def set_childs_level_next(node_start):
    iter_node = node_start
    while iter_node:
      iter_node.left.level_next = iter_node.right
      if iter_node.level_next:
        iter_node.right.level_next = iter_node.level_next.left
      else:
        iter_node.right.level_next = None
      iter_node = iter_node.level_next

  if not root: return None
  root.level_next = None
  node_start = root
  while node_start.left:
    set_childs_level_next(node_start)
    node_start = node_start.left
  return root

def get_level_next_str(root):
  if not root: return ''
  res = []
  queue = [root]
  while queue:
    node = queue.pop(0)
    if node.left:
      queue.append(node.left)
    while node:
      res.append(node.data)
      node = node.level_next
  return ','.join(res)

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O']]
  root = gen_binary_tree_breadth_first(src)
  ans = None
  if case == 0:
    ans = 'A,B,I,C,F,J,O'
  elif case == 1:
    src.append(['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'])
    root = gen_binary_tree_breadth_first(src)
    ans = 'A,B,I,C,F,J,O,P,Q,R,S,T,U,V,W'
  return root, ans

def main():
  print('Use set_level_next:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = get_level_next_str(set_level_next(root))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('Use set_level_next_less_space:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = get_level_next_str(set_level_next_less_space(root))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()




