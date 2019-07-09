from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def traverse_tree(node, k):
  """
    The time complexity is O(h) where h is the height of the tree.
    The additional space complexity is O(h) where h is the height of the tree.
    If you don't use recursive, you can follow EPI's guide that use a while to iterate node and
    the additional space complexity is O(1).
  """
  tmp = node.left.total + 1 if node.left else 1
  if k == tmp:
    return node
  elif k < tmp:
    return traverse_tree(node.left, k)
  else:
    return traverse_tree(node.right, k - tmp)

def get_input(case=0):
  src = [
    [{'data': 'A', 'total': 16}],
    [{'data': 'B', 'total': 7}, {'data': 'I', 'total': 8}],
    [{'data': 'C', 'total': 3}, {'data': 'F', 'total': 3}, {'data': 'J', 'total': 5}, {'data': 'O', 'total': 2}],
    [{'data': 'D', 'total': 1}, {'data': 'E', 'total': 1}, None,
     {'data': 'G', 'total': 2}, None,
     {'data': 'K', 'total': 4}, None,
     {'data': 'P', 'total': 1}
    ]
  ]
  src.append(
    [None] * 6 +
    [{'data': 'H', 'total': 1}] +
    [None] * 3 +
    [{'data': 'L', 'total': 2}, {'data': 'N', 'total': 1}] +
    [None] * 4
  )
  src.append([None] * 21 + [{'data': 'M', 'total': 1}] + [None] * 10)
  root = gen_binary_tree_breadth_first(src, is_dict_input=True)
  # order = 'inorder'
  # The inorder sequence is 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
  k = None
  ans = None
  if case == 0:
    k = 1
    ans = root.left.left.left # the 'D' node
  elif case == 1:
    k = 5
    ans = root.left.right # the 'F' node
  elif case == 2:
    k = 16
    ans = root.right.right.right # the 'P' node
  elif case == 3:
    k = 11
    ans = root.right.left.right.left.right # the 'M' node
  elif case == 4:
    k = 8
    ans = root # the 'A' node
  return root, k, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    root, k, ans = get_input(case)
    res = traverse_tree(root, k)
    print('res.data =', res.data)
    print('ans.data =', ans.data)
    print('Test success' if (res == ans) and (res.data == ans.data) else 'Test failure')
    """
    # case 0 and 1 both based on EPI's page 150
    # case 0 + case 1 in breadth first order
    print(root.data)
    print(root.left.data, root.right.data)
    print(root.left.left.data, root.left.right.data, root.right.left.data, root.right.right.data)
    print(root.left.left.left.data, root.left.left.right.data, root.left.right.left, root.left.right.right.data, root.right.left.left, root.right.left.right.data, root.right.right.left, root.right.right.right.data)
    """
    """
    # case 1 only in breadth first order
    print(root.left.right.right.left.data)
    print(root.right.left.right.left.data)
    print(root.right.left.right.right.data)
    print(root.right.left.right.left.right.data)
    """
    """
    # check case 1 in breadth first order
    print(root.left.right.left)
    print(root.right.left.left)
    print(root.right.right.left)
    print(root.left.left.left.left)
    print(root.left.left.left.right)
    print(root.left.left.right.left)
    print(root.left.left.right.right)
    print(root.left.right.right.right)
    print(root.right.right.right.left)
    print(root.right.right.right.right)
    print(root.right.left.right.left.left)
    print(root.right.left.right.right.left)
    print(root.right.left.right.right.right)
    """

if __name__ == '__main__':
  main()

