from __future__ import print_function
from utils_ch10 import get_tree_traversal_str, gen_binary_tree_breadth_first

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  if case == 0:
    root = gen_binary_tree_breadth_first(src)
    order = 'inorder'
    ans = 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
    return root, order, ans
  elif case == 1:
    root = gen_binary_tree_breadth_first(src)
    order = 'preorder'
    ans = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P'
    return root, order, ans
  elif case == 2:
    root = gen_binary_tree_breadth_first(src)
    order = 'postorder'
    ans = 'D,E,C,H,G,F,B,M,L,N,K,J,P,O,I,A'
    return root, order, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    root, order, ans = get_input(case)
    res = get_tree_traversal_str(root, order)
    print('order =', order)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')
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
