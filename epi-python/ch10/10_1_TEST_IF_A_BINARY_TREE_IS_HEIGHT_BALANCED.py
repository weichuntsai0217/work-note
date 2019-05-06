from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def recursive(node):
  """
    The time complexity O(n) where n is the number of nodes of the tree.
    The additional space complexity is O(h) where h is the height of the tree.
  """
  if not node:
    return -1

  h_left = recursive(node.left)
  if h_left < -1:
    return h_left
 
  h_right = recursive(node.right)
  if h_right < -1:
    return h_right

  if abs(h_left - h_right) <= 1:
    # balanced case
    return max(h_left, h_right) + 1
  return -2 # we use -2 means not balanced

def is_binary_tree_balanced(root):
  if recursive(root) <= -2:
    return False
  return True

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O']]
  if case == 0:
    root = gen_binary_tree_breadth_first(src)
    ans = True
    return root, ans
  elif case == 1:
    src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
    root = gen_binary_tree_breadth_first(src)
    ans = True
    return root, ans
  elif case == 2:
    src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
    src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
    root = gen_binary_tree_breadth_first(src)
    ans = False
    return root, ans
  elif case == 3:
    src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
    src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
    src.append([None] * 21 + ['M'] + [None] * 10)
    root = gen_binary_tree_breadth_first(src)
    ans = False
    return root, ans

def main():
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = is_binary_tree_balanced(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
