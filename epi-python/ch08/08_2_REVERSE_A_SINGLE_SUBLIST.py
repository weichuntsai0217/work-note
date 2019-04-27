from __future__ import print_function

class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def reverse_a_sublist(head, s, f): # the first element of a list is from index 1
  """
    The time complexity is O(f)
    The additional space complexity is O(1)
  """
  if (not head) or (not head.nxt) or (s == f): return head
  dummy_head = Node(0, head) # dummy_head.nxt is head
  prev = dummy_head
  k = 1
  while k < s:
    prev = prev.nxt
    k += 1

  end = prev.nxt # the start node, and it finally would be the end of the sublist
  while s < f:
    tmp = end.nxt
    end.nxt = tmp.nxt
    tmp.nxt = prev.nxt
    prev.nxt = tmp
    s += 1
    """
      When each loop starts:
      `end` is always the "s" node (`end` means it would be the end of the sublist after reversed.)
      `end.nxt` is always the 2nd node which is not handled.
      `prev.nxt` is always the 1st node which is not handled. (in loop 1, `prev.nxt` and `end` is the same but only for loop 1)
      The "f" node would not be handled, because finally it would be `prev.nxt` after "f-1" node is handled.
    """
  return dummy_head.nxt

def gen_list(src):
  head = None
  prev = None
  for data in src:
    if prev == None and head == None:
      head = Node(data)
      prev = head
    else:
      node = Node(data)
      prev.nxt = node
      prev = prev.nxt

  return head

def get_list_str(h):
  res = []
  node = h
  while node:
    res.append(str(node.data))
    node = node.nxt
  return '[' + ' => '.join(res) + ']'

def is_equal(h1, h2):
  s1 = get_list_str(h1)
  s2 = get_list_str(h2)
  return s1 == s2
  
def get_input(case=0):
  if case == 0:
    return gen_list([1,2,3,4,5,6,7]), 3, 6, gen_list([1,2,6,5,4,3,7])
  elif case == 1:
    return gen_list([1,2,3,4,5,6,7]), 1, 3, gen_list([3,2,1,4,5,6,7])
  elif case == 2:
    return gen_list([1,2,3,4,5,6,7]), 5, 7, gen_list([1,2,3,4,7,6,5])
  elif case == 3:
    return gen_list([1]), 1, 1, gen_list([1])
  elif case == 4:
    return gen_list([2,3]), 1, 2, gen_list([3,2])

def main():
  for case in xrange(5):
    head, s, f, ans = get_input(case)
    print('Input:')
    print('list =', get_list_str(head), 's =', s, 'f =', f)
    res = reverse_a_sublist(head, s, f)
    print('Output:')
    print(get_list_str(res))
    print('Test success' if is_equal(res, ans) else 'Test failure')
    print('='*10)

if __name__ == '__main__':
  main()
