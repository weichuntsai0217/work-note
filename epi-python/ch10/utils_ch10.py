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

def traverse_tree(node, order, res, keep_none_node=False):
  if (not node) and keep_none_node:
    res.append(node)
    return
  if order == 'preorder':
    if node:
      res.append(node.data)
      traverse_tree(node.left, order, res, keep_none_node)
      traverse_tree(node.right, order, res, keep_none_node)
  elif order == 'postorder':
    if node:
      traverse_tree(node.left, order, res, keep_none_node)
      traverse_tree(node.right, order, res, keep_none_node)
      res.append(node.data)
  else: # default is 'inorder'
    if node:
      traverse_tree(node.left, order, res, keep_none_node)
      res.append(node.data)
      traverse_tree(node.right, order, res, keep_none_node)

def get_tree_traversal_str(root, order='inorder', keep_none_node=False):
  """
    The time complexity is O(n) where n is the number of nodes of the binary tree.
    The additional space complexity is O(h) where h is the height of ther binary tree.
  """
  res = []
  traverse_tree(root, order, res, keep_none_node)
  return ','.join(map(lambda x: str(x), res))
