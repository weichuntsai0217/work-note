from __future__ import print_function

class Node(object):
  def __init__(self, data, nxt=None):
    self.data = data
    self.nxt = nxt

def merge_two_sorted_lists(h1, h2): # h1 and h2 are heads.
  """
    The time complexity is O(n + m) where n is the length of node_1 and m is the length of node_2
    The additional space complexity is O(1)
  """
  if h1 and (not h2): return h1
  if h2 and (not h1): return h2
  h = h1 if h1.data <= h2.data else h2
  p1 = h1
  p2 = h2
  cur_merged_end = Node(0, None)
  while p1 and p2:
    if p1.data <= p2.data:
      cur_merged_end.nxt = p1
      p1 = p1.nxt
    else:
      cur_merged_end.nxt = p2
      p2 = p2.nxt
    cur_merged_end = cur_merged_end.nxt
  cur_merged_end.nxt = p1 if p1 else p2
  return h

def get_list_str(h):
  res = []
  node = h
  while node:
    res.append(str(node.data))
    node = node.nxt
  return ' => '.join(res)

def is_equal(h1, h2):
  s1 = get_list_str(h1)
  s2 = get_list_str(h2)
  return s1 == s2

def get_input(case=0):
  h1 = Node(2)
  h2 = Node(3)
  if case == 0:
    return h1, None, h1
  elif case == 1:
    return None, h2, h2
  elif case == 2:
    h1.nxt = Node(5, Node(7))
    h2.nxt = Node(11)
    return h1, h2, h1
  elif case == 3:
    h1.nxt = Node(5, Node(7))
    h2.data = 5
    h2.nxt = Node(11)
    return h1, h2, h1

def main():
  for case in xrange(4):
    h1, h2, ans = get_input(case)
    print('Input:')
    print(get_list_str(h1))
    print(get_list_str(h2))
    res = merge_two_sorted_lists(h1, h2)
    print('Output:')
    print(get_list_str(res))
    print('Test success' if is_equal(res, ans) else 'Test failure')
    print('='*10)

if __name__ == '__main__':
  main()
