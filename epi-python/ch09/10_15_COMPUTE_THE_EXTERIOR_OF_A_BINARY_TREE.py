from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first, get_tree_traversal_str

def traverse_inorder(node, res):
  if node:
    if (not node.left) and (not node.right):
      res.append(node.data)
    traverse_inorder(node.left, res)
    traverse_inorder(node.right, res)


def get_exterior(root):
  """
    The time complexity is O(n) where n is the number of tree nodes.
  """
  exteriors = [root.data]
  if root.left or root.right:
    node = root.left if root.left else root.right
    while node.left or node.right:
      exteriors.append(node.data)
      if node.left:
        node = node.left
      elif node.right:
        node = node.right

    traverse_inorder(root, exteriors)
    
    node = root.right if root.right else root.left
    right_side = []
    while node.right or node.left:
      right_side.append(node.data)
      if node.right:
        node = node.right
      else:
        node = node.left
    right_side.reverse()

    exteriors += right_side
  return ','.join(exteriors)

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  root = gen_binary_tree_breadth_first(src)
  ans = None
  if case == 0:
    ans = 'A,B,C,D,E,H,M,N,P,O,I'
  elif case == 1:
    root.left.left = None
    ans = 'A,B,F,G,H,M,N,P,O,I'
  elif case == 2:
    root.right.right = None
    ans = 'A,B,C,D,E,H,M,N,K,J,I'
  elif case == 3:
    root.left = None
    ans = 'A,I,J,K,L,M,N,P,O,I'
  elif case == 4:
    root.right = None
    ans = 'A,B,C,D,E,H,G,F,B'
  return root, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = get_exterior(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()



