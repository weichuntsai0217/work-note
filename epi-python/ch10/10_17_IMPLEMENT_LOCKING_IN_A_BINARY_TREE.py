from __future__ import print_function
from utils_ch10 import get_tree_traversal_str, gen_binary_tree_breadth_first

def is_locked(node):
  return node.locked

def set_unclocked(node):
  """
    The time complexity is O(h) where h is height of the tree
  """
  if node.locked:
    node.locked = False
    while node.parent:
      node.parent.num_desc_locked -= 1
      node = node.parent

def set_locked(node):
  """
    The time complexity is O(h) where h is height of the tree
  """
  if node.locked or (node.num_desc_locked > 0):
    return False

  iter_node = node.parent
  while iter_node:
    if iter_node.locked:
      return False
    iter_node = iter_node.parent

  node.locked = True
  iter_node = node.parent
  while iter_node:
    iter_node.num_desc_locked += 1
    iter_node = iter_node.parent
  return node.locked


def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  root = gen_binary_tree_breadth_first(src, need_parent=True)
  return root

def main():
  root = get_input()
  print('Test node "{}"'.format(root.left.right.data))
  print('Test success' if set_locked(root.left.right) == True else 'Test failure')
  print('Test success' if is_locked(root.left.right) == True else 'Test failure')
  print('Test success' if root.num_desc_locked == 1 else 'Test failure')
  print('============')

  print('Test node "{}"'.format(root.left.right.right.left.data))
  print('Test success' if set_locked(root.left.right.right.left) == False else 'Test failure')
  print('Test success' if is_locked(root.left.right.right.left) == False else 'Test failure')
  print('Test success' if root.num_desc_locked == 1 else 'Test failure')
  print('============')

  print('Test node "{}"'.format(root.right.left.right.data))
  print('Test success' if set_locked(root.right.left.right) == True else 'Test failure')
  print('Test success' if is_locked(root.right.left.right) == True else 'Test failure')
  print('Test success' if root.num_desc_locked == 2 else 'Test failure')
  print('Test success' if root.right.num_desc_locked == 1 else 'Test failure')
  print('============')

  print('Test node "{}"'.format(root.right.data))
  print('Test success' if set_locked(root.right) == False else 'Test failure')
  print('Test success' if is_locked(root.right) == False else 'Test failure')
  print('Test success' if root.num_desc_locked == 2 else 'Test failure')
  print('============')

  print('Test node "{}"'.format(root.right.left.right.data))
  set_unclocked(root.right.left.right)
  print('Test success' if is_locked(root.right.left.right) == False else 'Test failure')
  print('Test success' if root.num_desc_locked == 1 else 'Test failure')
  print('============')

if __name__ == '__main__':
  main()

