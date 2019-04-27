from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def is_cyclicity_less_space(node): # input node is the head of a list.
  slow = node
  fast = node
  while fast and fast.nxt:
    slow = slow.nxt
    fast = fast.nxt.nxt
    if slow == fast:
      cycle_len = 1
      fast = fast.nxt
      while slow != fast:
        fast = fast.nxt
        cycle_len += 1
      cycle_len_for_return = cycle_len
      adv_cycle_iter = node
      while cycle_len > 0:
        adv_cycle_iter = adv_cycle_iter.nxt
        cycle_len -= 1

      final_iter = node
      while final_iter != adv_cycle_iter:
        final_iter = final_iter.nxt
        adv_cycle_iter = adv_cycle_iter.nxt
      return final_iter, cycle_len_for_return 
  return None, 0

def is_overlapping_for_no_cycle_lists(l_0, l_1):
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

def is_overlapping_for_all_kinds_of_lists(head_1, head_2):
  """
    The time complexity is O(n + m) where n is the length of list 1 and n is the length of list 2.
    The additional space complexity is O(1).
  """
  cycle_node_1, cycle_len_1 = is_cyclicity_less_space(head_1)
  cycle_node_2, cycle_len_2 = is_cyclicity_less_space(head_2)
  if cycle_node_1 and cycle_node_2:
    if cycle_len_1 != cycle_len_2:
      # for overlapping case, they must share the same cycle and cycle_len_1 must be cycle_len_2,
      # so if cycle_len_1 != cycle_len_2, it means that these two lists are not overlapping.
      return None
    if cycle_node_1 == cycle_node_2:
      # These 2 lists must share the same cycle and is overlapping at the node before or equal to cycle_node_1
      # They share the same cycle start node, that cycle_node_1 (or cycle_node_2 is OK)
      len_1_before_cycle = 0
      len_2_before_cycle = 0
      iter_node_1 = head_1
      iter_node_2 = head_2
      while iter_node_1 != cycle_node_1:
        len_1_before_cycle += 1
        iter_node_1 = iter_node_1.nxt

      while iter_node_2 != cycle_node_1:
        len_2_before_cycle += 1
        iter_node_2 = iter_node_2.nxt
      
      longer = head_1 if len_1_before_cycle > len_2_before_cycle else head_2
      shorter = head_2 if len_1_before_cycle > len_2_before_cycle else head_1
      diff = abs(len_1_before_cycle - len_2_before_cycle)
      while diff > 0:
        longer = longer.nxt
        diff -= 1

      while longer != None and shorter != None and longer != shorter:
        longer = longer.nxt
        shorter = shorter.nxt

      return longer

    else:
      iter_node = cycle_node_1.nxt
      iter_len = cycle_len_1  - 1
      while iter_len > 0:
        if iter_node == cycle_node_2:
          return cycle_node_1 
        else:
          iter_node = iter_node.nxt
          iter_len -= 1
      return None
    
  elif (not cycle_node_1) and (not cycle_node_2):
    return is_overlapping_for_no_cycle_lists(head_1, head_2)
  else:
    # if one list has a cycle but the other list doesn't have a cycle, these two lists can not overlap.
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

def get_input(case=0):
  src_1 = [1,2,3,4,5,6,7,8,9]
  src_2 = [-1,-2]
  if case == 0:
    head_1 = gen_list(src_1, 6)
    len_1 = len(src_1) + 1
    head_2 = gen_list(src_2)
    len_2 = len(src_2)
    return head_1, len_1, head_2, len_2, None, 0
  elif case == 1:
    head_1 = gen_list(src_1)
    len_1 = len(src_1)
    head_2 = gen_list(src_2)
    len_2 = len(src_2)
    return head_1, len_1, head_2, len_2, None, 0
  elif case == 2:
    head_1 = gen_list(src_1, 6)
    len_1 = len(src_1) + 1
    src_2 = src_2 + [-3, -4]
    head_2 = gen_list(src_2, 1)
    len_2 = len(src_2) + 1
    return head_1, len_1, head_2, len_2, None, 0
  elif case == 3:
    head_1 = gen_list(src_1)
    len_1 = len(src_1)
    head_2 = gen_list(src_2)
    head_2.nxt.nxt = head_1.nxt.nxt.nxt.nxt
    len_2 = 7
    return head_1, len_1, head_2, len_2, head_1.nxt.nxt.nxt.nxt, 5
  elif case == 4:
    head_1 = gen_list(src_1, 6)
    len_1 = len(src_1) + 1
    head_2 = gen_list(src_2)
    head_2.nxt.nxt = head_1.nxt.nxt.nxt.nxt
    len_2 = 8
    return head_1, len_1, head_2, len_2, head_1.nxt.nxt.nxt.nxt, 6


def main():
  for case in xrange(5):
    print('--- case {} ---'.format(case))
    head_1, len_1, head_2, len_2, ans, len_ans = get_input(case)
    res = is_overlapping_for_all_kinds_of_lists(head_1, head_2)
    print('Input:')
    print('head_1 =', get_list_str(head_1, len_1))
    print('head_2 =', get_list_str(head_2, len_2))
    print('Output:')
    print('ans =', get_list_str(ans, len_ans))
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
