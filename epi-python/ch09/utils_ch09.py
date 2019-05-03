from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def gen_list(src, cyclic_to=None): # cyclic_to is the index beginning with 1
  head = None
  prev = None
  tail = None
  for idx, data in enumerate(src):
    if prev == None and head == None:
      head = Node(data)
      prev = head
      if cyclic_to == 1:
        tail = head
    else:
      node = Node(data)
      prev.nxt = node
      prev = prev.nxt
      if idx == (len(src) - 1):
        node.nxt = tail
      if (idx + 1) == cyclic_to:
        tail = node
  if len(src) == 1 and cyclic_to == 1:
    head.nxt = head # the case for one-node list with a self loop.
  return head

def get_list_str(h, counts=None):
  res = []
  node = h
  if isinstance(counts, int):
    while counts > 0:
      res.append(str(node.data))
      node = node.nxt
      counts -= 1
  else:
    while node:
      res.append(str(node.data))
      node = node.nxt
  return '[' + ' => '.join(res) + ']'

def is_equal(h1, h1_counts, h2, h2_counts):
  s1 = get_list_str(h1, h1_counts)
  s2 = get_list_str(h2, h2_counts)
  return s1 == s2

