from __future__ import print_function
from utils_ch10 import gen_binary_tree_breadth_first

def traverse_inorder_with_parent(root):
  """
    The time complexity is O(n) where n is the number of nodes of the tree
    The additional space complexity is O(1) as the problem's requirement needs.
  """
  res = []
  cur = root
  prev = None
  while cur:
    """
      The key is that, when go bottom to explore subtree, prev is always the cur's parent.
      However when we detect that cur is prev's parent, that means left subtree or right subtree
      is traversed done, and we should move up to parent.
      We use a nxt variable to help cur and prev to figure what's going on in next round.
    """
    nxt = None
    if cur.parent == prev:
      # In this case, the current subtree is not traversed done
      if cur.left:
        nxt = cur.left
      else:
        res.append(cur.data)
        nxt = cur.right if cur.right else cur.parent
      
    elif cur.left == prev:
      # In this case cur.left is prev, this means the left subtree rooted in cur.right is traversed done.
      res.append(cur.data) # becuase the left subtree of cur is done, we record cur's data immediately.
      nxt = cur.right if cur.right else cur.parent
    else:
      # In this case cur.right is prev, this means the right subtree rooted in cur.right is traversed done.
      nxt = cur.parent
    prev = cur
    cur = nxt

  return ','.join(res)

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  if case == 0:
    root = gen_binary_tree_breadth_first(src, need_parent=True)
    order = 'inorder'
    ans = 'D,C,E,B,F,H,G,A,J,L,M,K,N,I,O,P'
    return root, order, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    root, order, ans = get_input(case)
    res = traverse_inorder_with_parent(root)
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

