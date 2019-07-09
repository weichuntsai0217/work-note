from __future__ import print_function
import bst

def build_min_height_bst_from_sorted_array(array):
  """
    The time complexity is O(n)
    The additional space complexity is O(logn)
  """
  def recursive(array, start, end):
    if start >= end:
      return None
    m = start + (end - start) / 2
    return bst.BinaryTreeNode(
      array[m],
      recursive(array, start, m),
      recursive(array, m+1, end),
    )
  return recursive(array, 0, len(array))

def get_input(case=0):
  array = [1,2,3,4,5,6,7]
  ans = bst.gen_binary_tree_breadth_first([[4], [2, 6], [1, 3, 5, 7]])
  if case == 0:
    pass
  return array, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('arrat =', array)
    print('Output:')
    res = build_min_height_bst_from_sorted_array(array)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if bst.get_tree_traversal_str(res, order='preorder') == bst.get_tree_traversal_str(ans, order='preorder') else 'Test failure')

if __name__ == '__main__':
  main()

