from __future__ import print_function

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

def copy_tree(root):
  def traverse(src_node, dst_node):
    dst_node.data = src_node.data
    if src_node.left:
      dst_node.left = BinaryTreeNode()
      traverse(src_node.left, dst_node.left)
    if src_node.right:
      dst_node.right = BinaryTreeNode()
      traverse(src_node.right, dst_node.right)

  if root:
    new_root = BinaryTreeNode()
    traverse(root, new_root)
    return new_root
  return None

def gen_binary_trees(n):
  """
  """
  def recursive(num_nodes, root, node, res, counter): # `counter` is to assign an integer to node data for check.
    if num_nodes == 0:
      res.append(copy_tree(root))
      return

    node.left = BinaryTreeNode(counter+1)
    recursive(num_nodes - 1, root, node.left, res, counter+1)
    node.left = None
    
    node.right = BinaryTreeNode(counter+1)
    recursive(num_nodes - 1, root, node.right, res, counter+1)
    node.right = None

    if num_nodes >= 2:
      node.left = BinaryTreeNode(counter+1)
      node.right = BinaryTreeNode(counter+2)
      recursive(num_nodes - 2, root, node.left, res, counter+2)
      if num_nodes - 2 > 0:
        recursive(num_nodes - 2, root, node.right, res, counter+2)
      node.left = None
      node.right = None

  res = []
  root = BinaryTreeNode(0) # 0 is just to assign an integer to node data for check
  node = root
  recursive(n - 1, root, node, res, 0) # 0 is just to assign an integer to node data for check
  return res
  

def get_input(case=0):
  n = 3
  ans = 5
  if case == 0:
    pass
  elif case == 1:
    n = 4
    ans = 14
  elif case == 2:
    n = 5
    ans = 38
  return n, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    n, ans = get_input(case)
    print('n =', n)
    print('Output:')
    res = gen_binary_trees(n)
    print('len(res) =', len(res))
    print('ans =', ans)
    print('Test success' if len(res) == ans else 'Test failure')
    """
    for root in res:
      print('root =', root)
    """


if __name__ == '__main__':
  main()




