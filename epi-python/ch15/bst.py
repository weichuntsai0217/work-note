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

  def __str__(self):
    queue = [self]
    res = '\n'
    while queue:
      this_level = []
      next_queue = []
      while queue:
        node = queue.pop(0)
        if node:
          this_level.append(node.data)
          next_queue.append(node.left)
          next_queue.append(node.right)
        else: # node is None
          this_level.append(node)
      if not all(x == None for x in this_level):
        res += ' '.join(map(lambda x: str(x) , this_level))
        if next_queue: res += '\n'
      queue = next_queue
    return res

def get_bst_from_epi_page_255(src=None):
  if not src:
    src = [19, 7, 43, 3, 11, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31]
  root = None
  for i in src:
    if root:
      Bst.insert(root, BinaryTreeNode(i))
    else:
      root = BinaryTreeNode(i)
  return root

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

class Bst(object):
  """
    Bst is "Binary Search Tree".
  """
  @staticmethod
  def insert(root, node, append_when_same_key=False):
    """
      The time complexity is O(h) where h is the height of the bst.
      The additional space complexity is O(h).
    """
    if not root:
      raise ValueError('The root does not exist.')
    if root.data == None:
      raise ValueError('The data of root is not initialized.')
    if node.data < root.data:
      if root.left:
        return Bst.insert(root.left, node)
      else:
        if append_when_same_key:
          node.data[1] = set([node.data[1]])
        root.left = node
        return True
    elif node.data > root.data:
      if root.right:
        return Bst.insert(root.right, node)
      else:
        if append_when_same_key:
          node.data[1] = set([node.data[1]])
        root.right = node
        return True
    else:
      """
        By definition keys in bst are all distinct, and this definition is quite OK for most simple scenarios.
        So if node.data == root.data, we regard this case as the data exists and we don't do anything.
      """
      if append_when_same_key: # This is a workaround flag for 15_13_ADD_CREDITS.py
        root.data[1].add(node.data[1])
        return True
      return False

  @staticmethod
  def delete(root, key):
    """
      The time complexity is O(h) where h is the height of the bst.
      The additional space complexity is O(1).
    """
    if not root:
      raise ValueError('The root does not exist.')
    parent = None
    key_node = root
    while key_node and key_node.data != key:
      parent = key_node
      if key < key_node.data:
        key_node = key_node.left
      elif key > key_node.data:
        key_node = key_node.right
    if not key_node:
      return False, root # the node with the key as data does not exist.

    if key_node.right:
      min_node = key_node.right
      parent = key_node
      while min_node.left:
        parent = min_node
        min_node = min_node.left
      key_node.data = min_node.data
      if parent.left == min_node:
        parent.left = min_node.right
      elif parent.right == min_node:
        parent.right = min_node.right
      min_node.right = None
    else:
      if root == key_node:
        root = root.left
        key_node.left = None
      else:
        if parent.left == key_node:
          parent.left = key_node.left
        elif parent.right == key_node:
          parent.right = key_node.left
        key_node.left = None
    return True, root

  @staticmethod    
  def search(root, key):
    if (not root) or (root.data == key):
      return root
    return Bst.search(root.left, key) if key < root.data else Bst.search(root.right, key)

  @staticmethod
  def pop_first(root): # pop the 1st (the smallest) node.
    """
      This method would return the 1st item and the root after the 1st item is removed.
      (Because it is possible that the 1st item is root itself.)
    """
    if not root: return None, None
    if not root.left:
      # root is the 1st element.
      new_root = root.right
      root.right = None
      return root, new_root
    parent = root
    node = root.left
    while node.left:
      parent = parent.left
      node = node.left
    parent.left = node.right
    node.right = None
    return node, root

  @staticmethod
  def first(root): # get the 1st (the smallest) node.
    if not root: return None
    node = root
    while node.left:
      node = node.left
    return node

  @staticmethod
  def last(root): # get the last (the largest) node.
    if not root: return None
    node = root
    while node.right:
      node = node.right
    return node
  
  @staticmethod
  def is_bst(root):
    """
      This one uses depth first search.
      The time complexity is O(n) where n is the number of nodes in the binary tree.
      The additional space complexity is O(h) where h is the binary tree height.
    """
    def recursive(node, lower, upper):
      if not node:
        return True
      elif (node.data < lower) or (node.data > upper):
        return False
      return recursive(node.left, lower, node.data) and recursive(node.right, node.data, upper)
    return recursive(root, -float('inf'), float('inf'))
  
  @staticmethod
  def is_bst_use_bfs(root):
    """
      This one uses breadth first search.
      The time complexity is O(n) where n is the number of nodes in the binary tree.
      The additional space complexity is O(m) where m is the maximum tree nodes in some level.
    """
    from collections import deque
    queue = deque([(root, -float('inf'), float('inf'))])
    while queue:
      entry = queue.popleft()
      if entry[0]: # entry = (node, lower, upper)
        node, lower, upper = entry
        if (node.data < lower) or (node.data > upper):
          return False
        queue.append((node.left, lower, node.data))
        queue.append((node.right, node.data, upper))
    return True

class SbBst(object):
  def insert(root, node):
    """
      SbBst is "Self-balanced binary search tree".
    """
    pass
