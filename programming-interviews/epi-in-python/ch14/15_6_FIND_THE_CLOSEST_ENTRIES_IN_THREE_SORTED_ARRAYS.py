from __future__ import print_function
import bst 

def get_the_distance_of_the_closest_entries_in_k_sorted_arrays(arrays):
  """
    The time complexity is O(n * h) where n is the total numbers of elements in arrays.
    h is the height of the bst we use in line 22.
    If the bst library you use is a self-balanced bst, then h = logk where
    k is the number of arrays in arrays.
  """
  heads = [0] * len(arrays)
  root = None
  for i in xrange(len(arrays)):
    array = arrays[i]
    head = heads[i]
    if root:
      """
        We use a tuple = (array_val, array_source_id) as tree node data
        and tulple would compare the 1st value first and then the 2nd value,
        so even array_val is the same, we still have array_source_id to make them distinct.
      """
      bst.Bst.insert(root, bst.BinaryTreeNode((array[head], i)))
    else:
      root = bst.BinaryTreeNode((array[head], i))
  res = float('inf')
  while True:
    res = min(res, bst.Bst.last(root).data[0] - bst.Bst.first(root).data[0])
    first_node, root = bst.Bst.pop_first(root)
    (val, array_id) = first_node.data
    heads[array_id] += 1
    if heads[array_id] >= len(arrays[array_id]):
      return res
    data = (arrays[array_id][heads[array_id]], array_id)
    bst.Bst.insert(root, bst.BinaryTreeNode(data))


def get_input(case=0):
  arrays = [
    [5, 10, 15],
    [3, 6, 9, 12, 15],
    [8, 16, 24],
  ]
  ans = 1
  if case == 0:
    pass
  elif case == 1:
    arrays = [
      [3, 6, 13],
      [5, 10],
      [10, 16, 24],
    ]
    ans = 3
  return arrays, ans


def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    arrays, ans = get_input(case)
    print('Input:')
    print('arrays =', arrays)
    print('Output:')
    res = get_the_distance_of_the_closest_entries_in_k_sorted_arrays(arrays)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()





