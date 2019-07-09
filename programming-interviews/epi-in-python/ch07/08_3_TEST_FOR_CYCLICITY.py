from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def is_cyclicity(node): # input node is the head of a list.
  """
    The time complexity is O(n) where n is the number of nodes in the list
    The additional space complexity is O(n) where n is the number of nodes in the list
  """
  table = {}
  while node:
    key = id(node)
    if key in table:
      return node
    else:
      table[key] = True
    node = node.nxt
  return None

def is_cyclicity_less_space(node): # input node is the head of a list.
  """
    The time complexity is O(n) where n is the number of nodes in the list
    The additional space complexity is O(1)
  """
  slow = node
  fast = node
  while fast and fast.nxt:
    """
      It is obvious that `fast` would enter into the cycle faster than `slow`.
      So at some loop when `slow` is at the start node of the cycle,
      at that time if there are k nodes between `fast` and `slow`
      (that is `fast` must go k nodes to catch up with `slow`),
      then it is obvious that `fast` can catch up with `slow` after k loops.
      Because `fast` walk 2 nodes per loop and `slow` walks 1 node per loop,
      `fast` can decrease the distance between `slow` by (2 - 1) = 1 node per loop.
    """
    slow = slow.nxt
    fast = fast.nxt.nxt
    if slow == fast:
      cycle_len = 1
      fast = fast.nxt
      while slow != fast:
        fast = fast.nxt
        cycle_len += 1

      """
        Why `adv_cycle_iter` and `final_iter` work?
          Let me explain by an example.
          Assume the cycle length is 5 (the cycle contains 5 nodes) and both of `adv_cycle_iter` & `final_iter`
          advance 1 node per loop.
          You can imagine that if we can create the condition below:
            "
            Let `adv_cycle_iter` be at the start node of the cycle, and
            `final_iter` be 5 nodes behind of `adv_cycle_iter` (that means `final_iter` need to
            go 5 nodes to reach the start node of the cycle)
            "
          then after 5 loops,
          `final_iter` would reach the start node of the cycle and at the same time
          `adv_cycle_iter` also reach the start node of the cycle because `adv_cycle_iter` just take a lap
          around the cycle and you can return `final_iter` to finish our job.
          So to meet the condition in the double quotes above,
          First we can set `adv_cycle_iter` and `final_iter` are all head and then move
          `adv_cycle_iter` 5 nodes ahead of `final_iter`, now we just let both of `adv_cycle_iter` & `final_iter`
          advance 1 node per loop, then at some loop, `adv_cycle_iter` and `final_iter` would meet the condition
          we mentioned above and problem solved.
      """
      adv_cycle_iter = node
      while cycle_len > 0:
        adv_cycle_iter = adv_cycle_iter.nxt
        cycle_len -= 1

      final_iter = node
      while final_iter != adv_cycle_iter:
        final_iter = final_iter.nxt
        adv_cycle_iter = adv_cycle_iter.nxt
      return final_iter
  return None

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
  return head

def get_list_str(h, counts):
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
  src = [1,2,3,4,5,6,7]
  if case == 0:
    head = gen_list(src)
    return head, len(src), 0, None
  elif case == 1:
    head = gen_list(src, 3)
    return head, len(src)+1, 6, head.nxt.nxt
  elif case == 2: # one node and self-loop, that is node.nxt is node itself.
    head = Node(1, None)
    head.nxt = head
    return head, 2, 1, head.nxt.nxt

def main():
  print('Use is_cyclicity')
  for case in xrange(3):
    print('Input:')
    head, counts, cycle_len, ans = get_input(case)
    print('list =', get_list_str(head, counts))
    res = is_cyclicity(head)
    print('Output:')
    print(get_list_str(res, cycle_len))
    print('Test success' if res == ans else 'Test failure')
    print('='*10)


  print('Use is_cyclicity_less_space')
  for case in xrange(3):
    print('Input:')
    head, counts, cycle_len, ans = get_input(case)
    print('list =', get_list_str(head, counts))
    res = is_cyclicity_less_space(head)
    print('Output:')
    print(get_list_str(res, cycle_len))
    print('Test success' if res == ans else 'Test failure')
    print('='*10)

if __name__ == '__main__':
  main()
