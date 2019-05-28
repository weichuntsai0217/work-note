from __future__ import print_function
import bst 

def get_k_largest_elements(root, k):
  """
    The time complexity is O(h + k) where h is the height of the tree.
    The additional space complexity is O(h)
  """
  def recursive(node, k, res):
    if node and len(res) < k:
      recursive(node.right, k, res)
      if len(res) < k:
        res.append(node.data)
        recursive(node.left, k, res)
  res = []
  recursive(root, k, res)
  return res

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  k = 3
  ans = [53,47,43]
  if case == 0:
    pass
  elif case == 1:
    k = 4
    ans.append(41)
  return root, k, ans


def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, k, ans = get_input(case)
    print('Input:')
    if case == 0:
      print('root =', root)
    print('k =', k)
    print('Output:')
    res = get_k_largest_elements(root, k)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()



