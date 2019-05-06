from __future__ import print_function
from utils_ch10 import BinaryTreeNode, gen_binary_tree_breadth_first, get_tree_traversal_str

class ListNode(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    self.tail = self.head

  def append(self, item):
    if self.tail:
      self.tail.nxt = ListNode(item)
      self.tail = self.tail.nxt
    else:
      self.head = ListNode(item)
      self.tail = self.head
    

def traverse_inorder(node, res):
  if node:
    if (not node.left) and (not node.right):
      res.append(node)
    traverse_inorder(node.left, res)
    traverse_inorder(node.right, res)

def get_leaves_as_linked_list(root):
  """
    The time complexity is O(n)
    The additional space complexity is O(h)
  """
  res = LinkedList()
  traverse_inorder(root, res)
  return res

def get_list_node_str(ls):
  res = []
  node = ls.head
  while node:
    res.append(node.data.data) # node.data is a tree node
    node = node.nxt

  return ','.join(map(lambda x: str(x), res))

def get_input(case=0):
  src = [['A'], ['B','I'], ['C', 'F', 'J', 'O'], ['D', 'E', None, 'G', None, 'K', None, 'P']]
  src.append([None] * 6 + ['H'] + [None] * 3 + ['L', 'N'] + [None] * 4)
  src.append([None] * 21 + ['M'] + [None] * 10)
  if case == 0:
    root = gen_binary_tree_breadth_first(src)
    # order = 'inorder'
    ans = 'D,E,H,M,N,P'
    return root, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    res = get_leaves_as_linked_list(root)
    res_str = get_list_node_str(res)
    print('res =', res)
    print('res_str =', res_str)
    print('ans =', ans)
    print('Test success' if res_str == ans else 'Test failure')

if __name__ == '__main__':
  main()


