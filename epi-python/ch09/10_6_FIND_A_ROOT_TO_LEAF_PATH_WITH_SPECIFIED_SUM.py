from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def recursive(target, node, partial_sum):
  """
    The time complexity is O(n) where n is the number of the tree nodes.
    The additional space complexity is O(h) where h is the height of ther tree.
  """
  if not node:
    # The parent of this current node has only one child and that child is not me.
    return False

  partial_sum += node.data
  if (not node.left) and (not node.right):
    return partial_sum == target

  return (
    recursive(target, node.left, partial_sum) or
    recursive(target, node.right, partial_sum)
  )

def is_path_weight_existed(target, root):
  return recursive(target, root, 0)


def get_input(case=0):
  src = [[314], [6,6], [271, 561, 2, 271]]
  src.append([28, 0, None, 3, None, 1, None, 28])
  src.append([None] * 6 + [17] + [None] * 3 + [401, 257] + [None] * 4)
  src.append([None] * 21 + [641] + [None] * 10)
  root = gen_binary_tree_breadth_first(src)
  target = None
  ans = None
  if case == 0:
    target = 591
    ans = True
  elif case == 1:
    target = 320
    ans = False
  elif case == 2:
    target = 1365
    ans = True
  return target, root, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    target, root, ans = get_input(case)
    res = is_path_weight_existed(target, root)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

