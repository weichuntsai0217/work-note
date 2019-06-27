from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

class Item(tuple):
  def __lt__(self, other):
    return self[0] < other[0]
  def __eq__(self, other):
    return self[0] == other[0]
  def __le__(self, other):
    return self.__eq__(other) or self.__lt__(other)
  def __gt__(self, other):
    return not self.__le__(other)
  def __ge__(self, other):
    return self.__eq__(other) or self.__gt__(other)

def insertion_sort_list(head):
  """
    The time complexity is O(n^2) where n is the list length
    The additional space complexity is O(1)
  """
  dummy_head = Node(0, head)
  iter_node = head
  while iter_node and iter_node.nxt:
    if iter_node.data > iter_node.nxt.data:
      pre = dummy_head
      target = iter_node.nxt
      while pre.nxt.data <= target.data: # "<=" is to make this sorting stable. Yout class "Item" should have corresponding setting
        pre = pre.nxt
      iter_node.nxt = target.nxt
      target.nxt = pre.nxt
      pre.nxt = target
    else:
      iter_node = iter_node.nxt
  
  return dummy_head.nxt

def merge_lists(head_0, head_1):
  dummy_head = Node(0, None)
  iter_merge = dummy_head
  iter_0 = head_0
  iter_1 = head_1
  while iter_0 or iter_1:
    if iter_0 and iter_1:
      if iter_0.data <= iter_1.data:
        iter_merge.nxt = iter_0
        iter_0 = iter_0.nxt
      else:
        iter_merge.nxt = iter_1
        iter_1 = iter_1.nxt
    elif iter_0:
      iter_merge.nxt = iter_0
      iter_0 = iter_0.nxt
    elif iter_1:
      iter_merge.nxt = iter_1
      iter_1 = iter_1.nxt
    iter_merge = iter_merge.nxt
  return dummy_head.nxt

def merge_sort(head):
  """
    The time complexity is O(n * logn) where n is the length of the list.
    The additional space complexity is O(logn)
  """
  if (not head) or (not head.nxt):
    return head
  pre_slow = head
  slow = head
  fast = head
  while fast and fast.nxt:
    pre_slow = slow
    slow = slow.nxt
    fast = fast.nxt.nxt
  pre_slow.nxt = None
  return merge_lists(merge_sort(head), merge_sort(slow))
  
  
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

def get_input(case=0):
  src = map(
    lambda x: Item(x),
    [(5, 'z'), (3, 'x'), (4, 'r'), (2, 'd'), (3, 'f'), (2, 'b'), (3, 'e'), (1, 'h')]
  )
  head = gen_list(src)
  counts = len(src)
  ans = head.nxt.nxt.nxt.nxt.nxt.nxt.nxt
  if case == 0:
    pass
  elif case == 1:
    src = map(
      lambda x: Item(x),
      [(5, 'd'), (3, 'c'), (1, 'b'), (3, 'a')]
    )
    head = gen_list(src)
    counts = len(src)
    ans = head.nxt.nxt
  return head, counts, ans

def main():
  print('User insertion_sort_list:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    head, counts, ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    res = insertion_sort_list(head)
    print('Output:')
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if res == ans else 'Test failure')
  print('\n===============')
  print('User merge_sort:')
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    head, counts, ans = get_input(case)
    print('Input:')
    print('head =', get_list_str(head))
    res = merge_sort(head)
    print('Output:')
    print('res =', get_list_str(res))
    print('ans =', get_list_str(ans))
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()







