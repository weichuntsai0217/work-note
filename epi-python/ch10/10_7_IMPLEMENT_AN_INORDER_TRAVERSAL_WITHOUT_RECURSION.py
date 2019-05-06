from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def traversal_inorder_no_recursive(root):
  """
    The time complexity is O(n) where n is the number of the tree nodes.
    The additional space complexity is O(h) where h is the height of the tree.
  """
  res = []
  stack = []
  cur = root
  while stack or cur:
    if cur:
      stack.append(cur)
      cur = cur.left
    else:
      cur = stack.pop()
      res.append(cur.data)
      cur = cur.right
      
  return ','.join(res)

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  if case == 0:
    root = gen_binary_tree_breadth_first(src)
    order = 'inorder'
    ans = 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
    return root, order, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    root, order, ans = get_input(case)
    res = traversal_inorder_no_recursive(root)
    print('order =', order)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()


