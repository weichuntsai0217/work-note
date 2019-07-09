from __future__ import print_function

class PostingNode(object):
  def __init__(self, jump=None, nxt=None):
    self.order = -1 # from the problem's spec, -1 means not setting yet.
    self.jump = jump
    self.nxt = nxt

def recursive_set_order(node):
  """
    The time complexity is O(n) where n is the length of the list.
      Because line 16 guarantees that every nod would be set order only once, and the number of
      function stack is O(n)
    The additional space compexity is O(n) (because of the number of function stack is O(n))
  """
  recursive_set_order_helper(node, 0)

def recursive_set_order_helper(node, order):
  if node and node.order == -1:
    node.order = order
    order += 1
    order = recursive_set_order_helper(node.jump, order)
    order = recursive_set_order_helper(node.nxt, order)
  return order

def iterate_set_order(head):
  """
    The time complexity is O(n) where the length of the list is n
    The additional space compexity is O(n)
  """
  order = 0
  stack = [head]
  while stack:
    node = stack.pop()
    if node and node.order == -1:
      node.order = order
      order += 1
      stack.append(node.nxt)
      stack.append(node.jump)

def get_input(case=0):
  if case == 0:
    a = PostingNode()
    b = PostingNode()
    c = PostingNode()
    d = PostingNode()
    a.jump = c
    a.nxt = b
    b.jupm = d
    b.nxt = c
    c.jump = b
    c.nxt = d
    d.jump = d
    return a

def show_nodes(node):
  res = []
  while node:
    res.append(str(node.order))
    node = node.nxt
  print('[' + ' => '.join(res) + ']')

def main():
  print('Use recursive_set_order')
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    head = get_input(case)
    recursive_set_order(head)
    show_nodes(head)

  print('Use iterate_set_order')
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    head = get_input(case)
    iterate_set_order(head)
    show_nodes(head)

if __name__ == '__main__':
  main()
