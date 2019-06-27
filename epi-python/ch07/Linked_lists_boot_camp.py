from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt # nxt means "next", next is python's built-in function

def search(node, key):
  """
    Find the node whose val is the "key" and return that node
  """
  while node and node.data != key:
    node = node.nxt
  return node

def insert_after(node, new_node):
  """
    Insert new_node after node
  """
  new_node.nxt = node.nxt
  node.nxt = new_node

def delete(a_node):
  """
    Delete the node immediately following a_node
  """
  a_node.nxt = a_node.nxt.nxt


def main():
  pass

if __name__ == '__main__':
  main()
