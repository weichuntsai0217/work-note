from __future__ import print_function
import bst 

def reconstruct_bst_by_preorder(array):
  """
    The time complexity is O(n^2) where n is the length of the array.
    The addition space complexity is O(h) where h is the height of tree.
  """
  def helper(array, start, end):
    if start == end:
      return None
    left_start = start+1
    left_end = start+1 # left_end = left_start + length
    for i in xrange(start+1, end):
      if array[i] < array[start]:
        left_end += 1
      else:
        break
    return bst.BinaryTreeNode(
      array[start],
      helper(array, left_start, left_end),
      helper(array, left_end, end)
    )
  if not array: return None
  return helper(array, 0, len(array))

def reconstruct_bst_by_preorder_fast(array):
  """
    The time complexity is O(n) where n is the length of the array.
    The addition space complexity is O(h) where h is the height of tree.
  """
  if not array: return None
  def rebuild_from_range(array, lower, upper, root_idx):
    if (
      (root_idx >= len(array)) or
      (array[root_idx] < lower) or
      (array[root_idx] > upper)
    ):
      return None, root_idx
    root = bst.BinaryTreeNode(array[root_idx])
    root_idx += 1
    left_tree, root_idx = rebuild_from_range(array, lower, root.data, root_idx)
    right_tree, root_idx = rebuild_from_range(array, root.data, upper, root_idx)
    root.left = left_tree
    root.right = right_tree
    return root, root_idx
  res, root_idx = rebuild_from_range(array, -float('inf'), float('inf'), 0)
  return res

def get_input(case=0):
  array = [43, 23, 37, 29, 31, 41, 47, 53]
  ans = ','.join(map(lambda x: str(x), array))
  if case == 0:
    pass
  elif case == 1:
    array = [43]
    ans = ','.join(map(lambda x: str(x), array))
  return array, ans


def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    print('Output:')
    res = bst.get_tree_traversal_str(reconstruct_bst_by_preorder_fast(array), order='preorder')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()




