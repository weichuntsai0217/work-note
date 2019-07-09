from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def is_overlapping(l_0, l_1):
  """
    The time complexity is O(n)
    The additional space complexity is O(1)
  """
  ls = [l_0, l_1]
  lens = [0, 0]
  for i in xrange(len(ls)):
    node = ls[i]
    while node:
      lens[i] += 1
      node = node.nxt

  long_idx = 0
  short_idx = 1
  if lens[0] <= lens[1]:
    long_idx = 1
    short_idx = 0
  diff = lens[long_idx] - lens[short_idx]

  while diff > 0:
    ls[long_idx] = ls[long_idx].nxt
    diff -= 1

  while ls[long_idx] != None and ls[short_idx] != None and ls[long_idx] != ls[short_idx]:
    ls[long_idx] = ls[long_idx].nxt
    ls[short_idx] = ls[short_idx].nxt

  return ls[long_idx]

def gen_list(src, cyclic_to=None): # cyclic_to is the index beginning with 1
  head = None
  prev = None
  tail = None
  for idx, data in enumerate(src):
    if prev == None and head == None:
      head = Node(data)
      prev = head
    else:
      node = Node(data)
      prev.nxt = node
      prev = prev.nxt
      if idx == (len(src) - 1):
        node.nxt = tail
      if (idx + 1) == cyclic_to:
        tail = node
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

def get_input(case=0):
  src_0 = [1,2,3,4,5,6,7]
  src_1 = [-3,-4]
  if case == 0:
    l_0 = gen_list(src_0)
    l_1 = gen_list(src_1)
    ans = l_0.nxt.nxt.nxt.nxt
    l_1.nxt.nxt = ans
    return l_0, l_1, ans
  elif case == 1:
    l_0 = gen_list(src_0)
    l_1 = gen_list(src_1)
    ans = None
    return l_0, l_1, ans 
  elif case == 2:
    l_0 = gen_list(src_0)
    l_1 = l_0
    ans = l_0
    return l_0, l_1, ans 

def main():
  for case in xrange(3):
    print('Input:')
    l_0, l_1, ans = get_input(case)
    print(get_list_str(l_0))
    print(get_list_str(l_1))
    res = is_overlapping(l_0, l_1)
    print('Output:')
    print(res.data if res else res)
    print(get_list_str(res))
    print('Test success' if res == ans else 'Test failure')
    print('='*10)

if __name__ == '__main__':
  main()
