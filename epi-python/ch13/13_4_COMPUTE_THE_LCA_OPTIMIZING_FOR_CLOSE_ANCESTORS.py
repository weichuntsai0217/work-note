from __future__ import print_function
from collections import deque

class BinaryTreeNode(object):
  def __init__(self, data=None, left=None, right=None, name=None, parent=None, total=None, level_next=None, locked=False):
    # name is for test, not necessary fo interview
    self.data = data
    self.left = left
    self.right = right
    self.name = name
    self.parent = parent
    self.total = total # total is the number of nodes in the subtree which is rooted at this current node.
    self.level_next = level_next
    self.locked = locked
    self.num_desc_locked = 0

def gen_binary_tree_breadth_first(x, need_parent=False, is_dict_input=False):
  queue = deque()
  root = None
  if is_dict_input:
    root = BinaryTreeNode(**(x[0][0]))
  else:
    root = BinaryTreeNode(x[0][0])
  queue.append(root)
  for i in xrange(1, len(x)):
    depth = x[i]
    for j in xrange(0, len(depth), 2):
      parent = queue.popleft()
      if parent:
        if is_dict_input:
          parent.left = BinaryTreeNode(**(depth[j])) if depth[j] != None else None
          parent.right = BinaryTreeNode(**(depth[j+1])) if depth[j+1] != None else None
        else:
          parent.left = BinaryTreeNode(depth[j]) if depth[j] != None else None
          parent.right = BinaryTreeNode(depth[j+1]) if depth[j+1] != None else None
        if need_parent:
          if parent.left: parent.left.parent = parent
          if parent.right: parent.right.parent = parent
        queue.append(parent.left)
        queue.append(parent.right)
      else:
        # in this case, depth[j] and depth[j+1] are both None based on my input design.
        queue.append(depth[j])
        queue.append(depth[j+1])
  return root

def get_lca_faster(node_0, node_1):
  """
    'lca' means the lowest common ancestor.
    For the worst caseThe, time complexity is O(h) where h is the tree height.
    and the additional space complexity is O(h).
    For most cases, the time complexity and  is O(d0 + d1)
    where d0 is the distance from node_0 to lca and d1 is the distance from node_1 to lca.
  """
  table = {}
  while node_0 or node_1:
    if node_0 in table:
      return node_0
    elif node_0:
      table[node_0] = True
      node_0 = node_0.parent
      
    if node_1 in table:
      return node_1
    elif node_1:
      table[node_1] = True
      node_1 = node_1.parent

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O']]
  src.append(['D', 'E', None, 'G', None, 'K', None, 'P'])
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  root = gen_binary_tree_breadth_first(src, True)
  node_0 = None
  node_1 = None
  ans = None
  if case == 0:
    node_0 = root.left.left.left
    node_1 = root.right.right.right
    ans = root
  elif case == 1:
    node_0 = root.left.right.right
    node_1 = root.right.left.right.left
    ans = root
  elif case == 2:
    node_0 = root.right.left.right.left.right # 'M'
    node_1 = root.right.left.right.right # 'N'
    ans = root.right.left.right # 'K'
  elif case == 3:
    node_0 = root.left.left # 'C'
    node_1 = root.left.right.right.left # 'H'
    ans = root.left # 'B'
  elif case == 4:
    node_0 = root.left.right # 'F'
    node_1 = root.left.right.right.left # 'H'
    ans = root.left.right # 'F'
  return root, node_0, node_1, ans

def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    root, node_0, node_1, ans = get_input(case)
    print('Input:')
    print('node_0.data =', node_0.data)
    print('node_1.data =', node_1.data)
    res = get_lca_faster(node_0, node_1)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('res.data =', res.data)
    print('ans.data =', ans.data)
    print('Test success' if res == ans and res.data == ans.data else 'Test failure')

if __name__ == '__main__':
  main()



