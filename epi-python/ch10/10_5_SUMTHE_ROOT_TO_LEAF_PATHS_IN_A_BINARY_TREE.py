from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def recursive_top_bottom(node, partial_sum):
  if not node:
    # the parent of this current node is not a leaf but this parent has only one child.
    return 0

  partial_sum = partial_sum * 2 + node.data
  if (not node.left) and (not node.right):
    return partial_sum

  return (
    recursive_top_bottom(node.left, partial_sum) +
    recursive_top_bottom(node.right, partial_sum)
  )


def get_sum_top_bottom(root):
  """
    The time complexity is O(n) where n is the number of the tree nodes.
    The additional space complexity is O(h) where h is the height of the tree.
  """
  return recursive_top_bottom(root, 0)

def get_sum_bottom_up(node):
  """
    The time complexity is O(n) where n is the number of the tree nodes.
    The additional space complexity is O(h) where h is the height of the tree.
  """
  if (not node.left) and (not node.right):
    return node.data, 1
  res = 0
  order = 0
  if node.left:
    left_res, left_order = get_sum_bottom_up(node.left)
    res += left_res
    order += (left_order << 1)
  if node.right:
    right_res, right_order = get_sum_bottom_up(node.right)
    res += right_res
    order += (right_order << 1)
  return (res + node.data * order), order


def get_input(case=0):
  src = [[1], [0,1], [0, 1, 0, 0]]
  src.append([0, 1, None, 1, None, 0, None, 0])
  src.append([None] * 6 + [0] + [None] * 3 + [1, 0] + [None] * 4)
  src.append([None] * 21 + [1] + [None] * 10)
  root = gen_binary_tree_breadth_first(src)
  ans = 126
  if case == 0:
    return root, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    print('Use bottom_up')
    root, ans = get_input(case)
    res = get_sum_bottom_up(root)[0]
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')
    print('Use top_bottom')
    root, ans = get_input(case)
    res = get_sum_top_bottom(root)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
