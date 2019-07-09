from __future__ import print_function
from collections import deque
"""
  deque guarantees that the time complexity for popleft is O(1) (Amortized worst case)
"""

class BinaryTreeNode(object):
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def get_nodes_by_depth(root):
  """
    The time complexity is O(n) where n is the number of nodes of the binary tree
    The additional space complexity is O(m) where m is the maximum number of nodes at some level.
  """
  queue = deque([root])
  res = []
  while queue:
    next_queue = deque([])
    this_level = []
    while queue:
      parent = queue.popleft()
      this_level.append(parent.data)
      if parent.left:
        next_queue.append(parent.left)
      if parent.right:
        next_queue.append(parent.right)
    res.append(this_level)
    queue = next_queue

  return res

def gen_binary_tree_breadth_first(x):
  queue = deque()
  root = BinaryTreeNode(x[0][0])
  queue.append(root)
  for i in xrange(1, len(x)):
    depth = x[i]
    for j in xrange(0, len(depth), 2):
      parent = queue.popleft()
      if parent:
        parent.left = BinaryTreeNode(depth[j]) if depth[j] != None else None
        parent.right = BinaryTreeNode(depth[j+1]) if depth[j+1] != None else None
        queue.append(parent.left)
        queue.append(parent.right)
      else:
        # in this case, depth[j] and depth[j+1] are both None based on my input design.
        queue.append(depth[j])
        queue.append(depth[j+1])
  return root

def remove_none(x):
  res = []
  for depth in x:
    res.append([])
    for i in xrange(len(depth)):
      if depth[i] != None:
        res[-1].append(depth[i])
  return res

def get_input(case=0):
  src = [[314], [6,6], [271, 561, 2, 271], [28, 0, None, 3, None, 1, None, 28]]
  if case == 0:
    root = gen_binary_tree_breadth_first(src)
    ans = remove_none(src)
  elif case == 1:
    src.append([None] * 6 + [17] + [None] * 3 + [401, 257] + [None] * 4)
    src.append([None] * 21 + [641] + [None] * 10)
    root = gen_binary_tree_breadth_first(src)
    ans = remove_none(src)
  return root, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = get_nodes_by_depth(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')
    # print(ans)
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
