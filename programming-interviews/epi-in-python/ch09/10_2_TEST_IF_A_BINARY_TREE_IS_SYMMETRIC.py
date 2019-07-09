from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first

def traverse(subtree_0, subtree_1):
  # Because of line 25,
  # subtree_0 is always on the left-hand side of root.
  # subtree_1 is always on the right-hand side of root.
  """
    The time complexity is O(n) where n is the number of nodes in the tree.
    The additional space complexity is O(h) where h is the height of the tree.
  """
  if not subtree_0 and not subtree_1:
    return True
  elif subtree_0 and subtree_1:
    return (
      subtree_0.data == subtree_1.data and
      traverse(subtree_0.left, subtree_1.right) and
      traverse(subtree_0.right, subtree_1.left)
    )
  else:
    return False


def is_binary_tree_symmetric(root):
  if not root or traverse(root.left, root.right):
    return True
  return False

def get_sym_level(x):
  return x + list(reversed(x))

def get_input(case=0):
  if case == 0:
    src = [['0'], ['1','1'], [None, '2', '2', None]]
    root = gen_binary_tree_breadth_first(src)
    ans = True
  elif case == 1:
    src = [['0'], ['1','1'], [None, '2', '3', None]]
    root = gen_binary_tree_breadth_first(src)
    ans = False
  elif case == 2:
    src = [['0'], ['1','1'], get_sym_level(['2', '3'])]
    root = gen_binary_tree_breadth_first(src)
    ans = True
  elif case == 3:
    level_2 = get_sym_level(['2', '3'])
    level_3 = get_sym_level([None, '4', '5', None])
    src = [['0'], ['1','1'], level_2, level_3]
    root = gen_binary_tree_breadth_first(src)
    ans = True
  elif case == 4:
    level_2 = get_sym_level(['2', '3'])
    level_3 = get_sym_level(['4', '5', None, '6'])
    level_4 = get_sym_level([None]*6 + ['7', None])
    src = [['0'], ['1','1'], level_2, level_3, level_4]
    root = gen_binary_tree_breadth_first(src)
    ans = True
  elif case == 5:
    level_2 = get_sym_level(['2', '3'])
    level_3 = get_sym_level(['4', '5', None, '6'])
    level_4 = get_sym_level([None]*6 + ['7', None])
    src = [['0'], ['1','-1'], level_2, level_3, level_4]
    root = gen_binary_tree_breadth_first(src)
    ans = False
  elif case == 6:
    level_2 = get_sym_level(['2', '3'])
    level_3 = get_sym_level(['4', '5', None, '6'])
    level_4 = get_sym_level([None]*6 + ['7', None])
    level_4[9] = 20
    src = [['0'], ['1','1'], level_2, level_3, level_4]
    print('src =', src)
    root = gen_binary_tree_breadth_first(src)
    ans = False
  
  return root, ans

def main():
  for case in xrange(7):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = is_binary_tree_symmetric(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

