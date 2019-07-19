"""
  Use python 3.6.8
"""
"""
  We focus on operations on singly-linked lists
  We use `head` for the first node of the singly-linked list.
  We assume that
    1. Users always input valid start and end index to our functions.
    2. The index for `head` is 0, just as the array tradition.
  Note that, because of the nature of the singly-linked list, the implements are in-place,
  and if you want to have a copy version, just copy the original data.
"""


class Node(object):
  def __init__(self, data=None, nxt=None):
    self.data = data
    self.nxt = nxt

def rotate_in_place(head, shift, start, end): 
  """
    Rotate an array in place with a right (positive) or left (negative) shift.
    The sublist is from start ~ end (inclusive), that is `end - start + 1` is the length of the sublist.
    The sign of input shift for right or left follows the `collections.deque` tradition.

    We always convert the input shift to an equvalent left shift and then do equivalent shift left.
    Because we always do left shift, the converted shift is always positive.
    +3 => 3 - 5 = -2
    1,2,3,4,5
    3 4 5 1 2

    -2 => -2 - (-5) = 3
    1,2,3,4,5
    3 4 5 1 2
  """
  def helper(head, shift, tail):
    """
      In `helper`, `shift` is always >= 0 and always means 'left shift' and
      shift is less than the length of the sublist.
    """
    prv = Node(None, head)
    for _ in range(shift):
      prv = prv.nxt
    if prv.nxt == head:
      return head, tail
    else:
      new_head = prv.nxt
      prv.nxt = None
      tail.nxt = head
      return new_head, prv

  if start >= end: return head

  i = 0
  sublength = end - start + 1
  node = head
  prv_sublist = Node(None, head)
  sublist_tail = None
  while node:
    if i == (start - 1):
      prv_sublist = node # prv_sublist.nxt is the sublist head.
    if i == end:
      sublist_tail = node
    node = node.nxt
    i += 1
  aft_sublist = sublist_tail.nxt
  sublist_tail.nxt = None
  
  
  shift %= sublength  # # convert to an equivalent right shift (positive)
  if shift == 0: return head
  shift = sublength - shift
  """
    The above line converts the right shift to an equivalent left shift represented by a positive value
    because later we only do left shift, the positive or negative does not mean much to us,
    we only need the absolute value of shift,
    that's why we do i - shift instead of shift - i
  """
  sublist_head, sublist_tail = helper(prv_sublist.nxt, shift, sublist_tail)
  prv_sublist.nxt = sublist_head
  sublist_tail.nxt = aft_sublist
  return prv_sublist.nxt if start == 0 else head

def remove_duplicates_in_a_sorted_list(head):
  if not head: return head
  node = head
  while node.nxt:
    if node.data == node.nxt.data:
      node.nxt = node.nxt.nxt
    else:
      node = node.nxt
  return head

def remove_duplicates_in_an_unsorted_list(head):
  if not head: return head
  seen = set([head.data])
  node = head
  while node.nxt:
    if node.nxt.data in seen:
      node.nxt = node.nxt.nxt
    else:
      seen.add(node.nxt.data)
      node = node.nxt
  return head

def merge_two_sorted_lists(head_a, head_b):
  """
    The time complexity is O(m + n) where m is the head_a list length and n is he head_b list length.
    The space complexity including the output is O(1).
  """
  dummy_head = Node()
  tail = dummy_head
  while head_a and head_b:
    if head_a.data <= head_b.data:
      tail.nxt = head_a
      head_a = head_a.nxt
    else:
      tail.nxt = head_b
      head_b = head_b.nxt
    tail = tail.nxt
  tail.nxt = head_a or head_b
  return dummy_head.nxt

def merge_two_adjacent_sublists_in_a_src_list(head, p, q, r):
  """
    The time complexity is O(n) where n is the src list length.
    The space complexity including the output is O(1).
    The valid p, q, r are:
      p <= q and q < r
    I don't handle other meaningless cases(e.g., q = r, this means only one sublist).
    The first sublist is from p ~ q (inclusive)
    and the second sublist is from q + 1 ~ r (inclusive)
  """
  def merge_helper(head_a, tail_a, head_b, tail_b):
    """
      The time complexity is O(m + n) where m is the head_a list length and n is he head_b list length.
      The space complexity including the output is O(1).
    """
    dummy_head = Node()
    tail = dummy_head
    while head_a and head_b:
      if head_a.data <= head_b.data:
        tail.nxt = head_a
        head_a = head_a.nxt
      else:
        tail.nxt = head_b
        head_b = head_b.nxt
      tail = tail.nxt
    if head_a:
      tail.nxt = head_a
      return dummy_head.nxt, tail_a
    else:
      tail.nxt = head_b
      return dummy_head.nxt, tail_b

  node = head
  prv_sublist = Node(None, head)
  head_left = None
  tail_left = None
  head_right = None
  tail_right = None
  for i in range(r+1):
    if i == p-1:
      prv_sublist = node
    if i == p:
      head_left = node
    if i == q:
      tail_left = node
    if i == q+1:
      head_right = node
    if i == r:
      tail_right = node
    node = node.nxt
  aft_sublist = tail_right.nxt
  if tail_left: tail_left.nxt = None
  if tail_right: tail_right.nxt = None

  sublist_head, sublist_tail = merge_helper(head_left, tail_left, head_right, tail_right)
  prv_sublist.nxt = sublist_head
  sublist_tail.nxt = aft_sublist
  return prv_sublist.nxt if p == 0 else head

def reverse_a_sublist(head, s, f): # s is the start index and f is the final(end) index.
  dummy = Node(None, head)
  prv = dummy
  i = 0
  while i < s: # because prv is before head, we don't need (s-1) condition
    prv = prv.nxt
    i += 1

  end = prv.nxt
  """
    At beginning, `prv.nxt` is
      1. the start of the original sublist
      2. the end of the reversed sublist.
    We use `end` to save the the end of the reversed sublist.
  """
  for _ in range(f - s):
    """
      When the while loop executes, `prv.nxt` would be advanced and
      always points to the tempariry start of the reversed sublist.
      After the loop ended, prv.nxt is just the start of the reversed sublist.
    """
    tmp = end.nxt
    end.nxt = tmp.nxt
    tmp.nxt = prv.nxt
    prv.nxt = tmp
    s += 1

  return dummy.nxt

def parition(head, x, start, end):
  """
    Partition the sublist base on the given x as the pivot value.
    The sublist is from start ~ end (inclusive)
  """
  def helper(head, x):
    smaller_head = Node()
    smaller_tail = smaller_head
    equal_head = Node() 
    equal_tail = equal_head
    larger_head = Node()
    larger_tail = larger_head
    while head:
      if head.data < x:
        smaller_tail.nxt = head
        smaller_tail = smaller_tail.nxt
      elif head.data == x:
        equal_tail.nxt = head
        equal_tail = equal_tail.nxt
      else:
        larger_tail.nxt = head
        larger_tail = larger_tail.nxt
      head = head.nxt
    larger_tail.nxt = None
    equal_tail.nxt = larger_head.nxt
    smaller_tail.nxt = equal_head.nxt
    real_tail = None
    if larger_tail != larger_head:
      real_tail = larger_tail
    elif equal_tail != equal_head:
      real_tail = equal_tail
    elif smaller_tail != smaller_head:
      real_tail = smaller_tail
    return smaller_head.nxt, real_tail

  node = head
  dummy = Node(None, head)
  prv_sublist = dummy
  sublist_tail = None
  for i in range(end+1):
    if i == (start - 1):
      prv_sublist = node # prv_sublist.nxt is the original sublist head.
    elif i == end:
      sublist_tail = node
    node = node.nxt
  aft_sublist = sublist_tail.nxt
  sublist_tail.nxt = None

  sublist_head, sublist_tail = helper(prv_sublist.nxt, x)
  prv_sublist.nxt = sublist_head
  sublist_tail.nxt = aft_sublist
  return dummy.nxt

def is_palindromic(head, start, end):
  """
    Check if the sublist is palindromic.
    The sublist is from start ~ end (inclusive)
  """
  def reverse(head):
    prv = Node(None, head) # prv is actually a dummy before head
    end = head
    while end.nxt:
      tmp = end.nxt
      end.nxt = tmp.nxt
      tmp.nxt = prv.nxt
      prv.nxt = tmp
    return prv.nxt
  def helper(head):
    slow = head
    fast = head
    while fast and fast.nxt:
      slow = slow.nxt
      fast = fast.nxt.nxt
    """
      If the list length is an odd number, after the above while loop ended
      `fast` is the tail node and `slow` now is the middle node of the list, not the
      first node of the second half list, e.g.,
      ```
        1 => 2 => 3 => 2 => 1
                 slow       fast
      ```
      You might think that for this odd length case, why we don't move `slow` to next node
      to make it the first node of the second half list?
      That's because after we reverse the second half list, it would be
      ```
        1 => 2 => 3 <= 2 <= 1
        head                slow
      ```
      That is, the first half and second half heads both point to `3`(the middle node of the original list)
      and this would not affect our testing result.
      Feel free to 2 lines immediately after the while loop like:
      ```
        if fast: slow = slow.nxt
      ```
      if you are not comfortable with the original scheme.
    """
    slow = reverse(slow)
    while head and slow:
      if head.data != slow.data:
        return False
      head = head.nxt
      slow = slow.nxt
    return True

  if start == end: return True
  
  dummy = Node(None, head)
  prv_sublist = dummy
  sublist_tail = None
  node = head
  for i in range(end+1):
    if i == (start - 1):
      prv_sublist = node # prv_sublist.nxt is the original sublist head.
    elif i == end:
      sublist_tail = node
    node = node.nxt
  aft_sublist = sublist_tail.nxt
  sublist_tail.nxt = None # cut the sublist, otherwise reverse function would iterate to the tail of the source list.
  return helper(prv_sublist.nxt)

def is_cyclic(head):
  """
    Check if a list is clyclic. If it is cyclic, return the cycle start node and cycle length, otherwise return
      None and 0.
    The time complexity is O(n) where n is the number of nodes in the list
    The additional space complexity is O(1)
  """
  slow = head
  fast = head
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
      adv_cycle_iter = head
      for _ in range(cycle_len):
        adv_cycle_iter = adv_cycle_iter.nxt

      final_iter = head
      while final_iter != adv_cycle_iter:
        final_iter = final_iter.nxt
        adv_cycle_iter = adv_cycle_iter.nxt
      return final_iter, cycle_len
  return None, 0

# Test utils starts
def gen_list(src, cyclic_to=None):
  head = None
  prev = None
  tail = None
  for idx, data in enumerate(src):
    node = Node(data)
    if prev == None and head == None:
      head = node
      prev = head
    else:
      prev.nxt = node
      prev = prev.nxt
    if cyclic_to == idx:
      tail = node
    if idx == len(src) - 1:
      node.nxt = tail
  return head

def get_list_str(h, counts=None):
  res = []
  node = h
  if isinstance(counts, int):
    for _ in range(counts):
      res.append(str(node.data))
      node = node.nxt
  else:
    while node:
      res.append(str(node.data))
      node = node.nxt
  return '[' + ' => '.join(res) + ']'

def is_equal(h1, h2, counts_1=None, counts_2=None):
  s1 = get_list_str(h1, counts_1)
  s2 = get_list_str(h2, counts_2)
  return s1 == s2

def rot(array, shift):
  from collections import deque
  res = deque(array)
  res.rotate(shift)
  return list(res)

def test_rotate_in_place():
  def get_inputs(case):
    prefix = list('')
    suffix = list('')
    data = [0, 1, 2, 3, 4]
    head = gen_list(prefix + data + suffix)
    shift = 0
    ans_head = head
    if case == 0:
      pass
    elif case == 1:
      shift = 2
      ans_head = head.nxt.nxt.nxt
    elif case == 2:
      shift = 12
      ans_head = head.nxt.nxt.nxt
    elif case == 3:
      head = gen_list(prefix+ data + suffix)
      shift = -2
      ans_head = head.nxt.nxt
    elif case == 4:
      head = gen_list(prefix+ data + suffix)
      shift = -12
      ans_head = head.nxt.nxt
    elif case == 5:
      prefix = list('ab')
      head = gen_list(prefix+ data + suffix)
      shift = -12
      ans_head = head
    elif case == 6:
      suffix = list('cde')
      head = gen_list(prefix+ data + suffix)
      shift = -12
      ans_head = head.nxt.nxt
    elif case == 7:
      prefix = list('ab')
      suffix = list('cde')
      head = gen_list(prefix+ data + suffix)
      shift = -12
      ans_head = head
    start = len(prefix)
    end = len(prefix) + len(data) - 1
    ans_list = gen_list(prefix + rot(data, shift) + suffix)
    return head, shift, start, end, ans_head, ans_list
  for case in range(8):
    head, shift, start, end, ans_head, ans_list = get_inputs(case)
    res_head = rotate_in_place(head, shift, start, end)
    assert res_head == ans_head
    assert is_equal(res_head, ans_list)
  print('rotate_in_place success')

def test_remove_duplicates_in_a_sorted_list():
  def get_inputs(case):
    src = []
    head = gen_list(src)
    ans = gen_list(src)
    if case == 0:
      pass
    elif case == 1:
      src = [0]
      head = gen_list(src)
      ans = gen_list(src)
    elif case == 2:
      src = [0, 1, 1, 1, 2, 2, 2, 2]
      head = gen_list(src)
      ans = gen_list(list(range(3)))
    elif case == 3:
      src = [0, 0, 1, 1, 1, 2]
      head = gen_list(src)
      ans = gen_list(list(range(3)))
    elif case == 4:
      src = [0, 0, 1, 1, 1, 2, 2, 2, 2]
      head = gen_list(src)
      ans = gen_list(list(range(3)))
    return head, ans

  for case in range(5):
    head, ans = get_inputs(case)
    res_head = remove_duplicates_in_a_sorted_list(head)
    assert is_equal(head, ans)
  print('remove_duplicates_in_a_sorted_list success')

def test_remove_duplicates_in_an_unsorted_list():
  def get_inputs(case):
    src = []
    head = gen_list(src)
    ans = gen_list(src)
    if case == 0:
      pass
    elif case == 1:
      src = [0]
      head = gen_list(src)
      ans = gen_list(src)
    elif case == 2:
      src = [1, 2, 2, 0, 2, 2, 1, 1]
      head = gen_list(src)
      ans = gen_list([1, 2, 0])
    elif case == 3:
      src = [0, 1, 0, 1, 2, 1]
      head = gen_list(src)
      ans = gen_list([0, 1, 2])
    elif case == 4:
      src = [2, 1, 1, 2, 1, 2, 2, 0, 0]
      head = gen_list(src)
      ans = gen_list([2, 1, 0])
    return head, ans

  for case in range(5):
    head, ans = get_inputs(case)
    res_head = remove_duplicates_in_an_unsorted_list(head)
    assert is_equal(head, ans)
  print('remove_duplicates_in_an_unsorted_list success')

def test_merge_two_sorted_lists():
  def get_inputs(case):
    head_a = None
    head_b = None
    ans_head = None
    ans_list = None
    if case == 0:
      pass
    elif case == 1:
      head_a = gen_list([0])
      ans_head = head_a
      ans_list = gen_list([0])
    elif case == 1:
      head_b = gen_list([0])
      ans_head = head_b
      ans_list = gen_list([0])
    elif case == 2:
      head_a = gen_list([2, 5, 7])
      head_b = gen_list([3, 11])
      ans_head = head_a
      ans_list = gen_list([2, 3, 5, 7, 11])
    elif case == 3:
      head_a = gen_list([3, 11])
      head_b = gen_list([2, 5, 7])
      ans_head = head_b
      ans_list = gen_list([2, 3, 5, 7, 11])

    return head_a, head_b, ans_head, ans_list
  
  for case in range(4):
    head_a, head_b, ans_head, ans_list = get_inputs(case)
    res_head = merge_two_sorted_lists(head_a, head_b)
    assert res_head == ans_head
    assert is_equal(res_head, ans_list)
  print('merge_two_sorted_lists success')

def test_merge_two_adjacent_sublists_in_a_src_list():
  def get_inputs(case):
    prefix = list('')
    suffix = list('')
    data_left = [2, 5, 7]
    data_right = [3, 11]
    head = gen_list(prefix + data_left + data_right + suffix)
    ans_head = head
    if case == 0:
      pass
    elif case == 1:
      prefix = list('ab')
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head
    elif case == 2:
      suffix = list('cde')
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head
    elif case == 3:
      prefix = list('ab')
      suffix = list('cde')
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head
    elif case == 4:
      data_left = [5]
      data_right = [3]
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head.nxt
    elif case == 5:
      prefix = list('ab')
      data_left = [5]
      data_right = [3]
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head
    elif case == 6:
      suffix = list('cde')
      data_left = [5]
      data_right = [3]
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head.nxt
    elif case == 7:
      prefix = list('ab')
      suffix = list('cde')
      data_left = [5]
      data_right = [3]
      head = gen_list(prefix + data_left + data_right + suffix)
      ans_head = head
    p = len(prefix)
    q = len(prefix) + len(data_left) - 1
    r = len(prefix) + len(data_left) + len(data_right) - 1
    ans_list = gen_list(prefix + sorted(data_left + data_right) + suffix)
    return head, p, q, r, ans_head, ans_list

  for case in range(8):
    head, p, q, r, ans_head, ans_list = get_inputs(case)
    res_head = merge_two_adjacent_sublists_in_a_src_list(head, p, q, r)
    assert res_head == ans_head
    assert is_equal(res_head, ans_list)
  
  print('merge_two_adjacent_sublists_in_a_src_list success')

def test_reverse_a_sublist():
  def get_inputs(case):
    prefix = list('')
    suffix = list('')
    data = [1,2,3,4,5]
    head = gen_list(prefix + data + suffix)
    ans_head = head.nxt.nxt.nxt.nxt
    if case == 0:
      pass
    elif case == 1:
      prefix = list('ab')
      head = gen_list(prefix + data + suffix)
      ans_head = head
    elif case == 2:
      suffix = list('cde')
      head = gen_list(prefix + data + suffix)
      ans_head = head.nxt.nxt.nxt.nxt
    elif case == 3:
      prefix = list('ab')
      suffix = list('cde')
      head = gen_list(prefix + data + suffix)
      ans_head = head
    elif case == 4:
      data = [1]
      head = gen_list(prefix + data + suffix)
      ans_head = head
    elif case == 5:
      prefix = list('ab')
      data = [1]
      head = gen_list(prefix + data + suffix)
      ans_head = head
    elif case == 6:
      suffix = list('cde')
      data = [1]
      head = gen_list(prefix + data + suffix)
      ans_head = head
    elif case == 7:
      prefix = list('ab')
      suffix = list('cde')
      data = [1]
      head = gen_list(prefix + data + suffix)
      ans_head = head

    s = len(prefix)
    f = len(prefix) + len(data) - 1
    ans_list = gen_list(prefix + list(reversed(data)) + suffix)
    return head, s, f, ans_list

  for case in range(8):
    head, s, f, ans_list = get_inputs(case)
    res_head = reverse_a_sublist(head, s, f)
    assert is_equal(res_head, ans_list)
  print('reverse_a_sublist success')

def test_parition():
  def get_inputs(case):
    def get_ans_data(data, x):
      res = []
      for d in data:
        if d < x:
          res.append(d)
      for d in data:
        if d == x:
          res.append(d)
      for d in data:
        if d > x:
          res.append(d)
      return res
    prefix = list('')
    suffix = list('')
    data = [5,2,4,3,1,3]
    head = gen_list(prefix + data + suffix)
    x = 3
    ans_head = head.nxt
    if case == 0:
      pass
    elif case == 1:
      prefix = list('ab')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 3
      ans_head = head
    elif case == 2:
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 3
      ans_head = head.nxt
    elif case == 3:
      prefix = list('ab')
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 3
      ans_head = head
    elif case == 4:
      prefix = list('ab')
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 5
      ans_head = head
    elif case == 5:
      prefix = list('ab')
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 1
      ans_head = head
    elif case == 6:
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 5
      ans_head = head.nxt
    elif case == 7:
      suffix = list('cde')
      data = [5,2,4,3,1,3]
      head = gen_list(prefix + data + suffix)
      x = 1
      ans_head = head.nxt.nxt.nxt.nxt
    elif case == 8:
      suffix = list('cde')
      data = [1]
      head = gen_list(prefix + data + suffix)
      x = 1
      ans_head = head
    elif case == 9:
      suffix = list('cde')
      data = [1]
      head = gen_list(prefix + data + suffix)
      x = 3
      ans_head = head
    elif case == 10:
      prefix = list('ab')
      data = [1]
      head = gen_list(prefix + data + suffix)
      x = 1
      ans_head = head
    elif case == 11:
      prefix = list('ab')
      data = [1]
      head = gen_list(prefix + data + suffix)
      x = 3
      ans_head = head
      
    ans_list = gen_list(prefix + get_ans_data(data, x) + suffix)
    start = len(prefix)
    end = len(prefix) + len(data) - 1

    return head, x, start, end, ans_head, ans_list

  for case in range(12):
    head, x, start, end, ans_head, ans_list = get_inputs(case)
    res_head = parition(head, x, start, end)
    assert res_head == ans_head
    assert is_equal(res_head, ans_list)
  print('partition success')

def test_is_palindromic():
  
  def get_inputs(case):
    prefix = list('')
    suffix = list('')
    data = [1]
    head = gen_list(prefix + data + suffix)
    ans = True
    if case == 0:
      pass
    elif case == 1:
      data = [1,1]
      head = gen_list(prefix + data + suffix)
      ans = True
    elif case == 2:
      data = [1,2]
      head = gen_list(prefix + data + suffix)
      ans = False
    elif case == 3:
      data = [7,3,1,5,1,3,7]
      head = gen_list(prefix + data + suffix)
      ans = True
    elif case == 4:
      data = [7,3,1,5,2,3,7]
      head = gen_list(prefix + data + suffix)
      ans = False
    elif case == 5:
      prefix = list('ab')
      suffix = list('cde')
      head = gen_list(prefix + data + suffix)
      ans = True
    elif case == 6:
      prefix = list('ab')
      suffix = list('cde')
      data = [1,1]
      head = gen_list(prefix + data + suffix)
      ans = True
    elif case == 7:
      prefix = list('ab')
      suffix = list('cde')
      data = [1,2]
      head = gen_list(prefix + data + suffix)
      ans = False
    elif case == 8:
      prefix = list('ab')
      suffix = list('cde')
      data = [7,3,1,5,1,3,7]
      head = gen_list(prefix + data + suffix)
      ans = True
    elif case == 9:
      prefix = list('ab')
      suffix = list('cde')
      data = [7,3,1,5,2,3,7]
      head = gen_list(prefix + data + suffix)
      ans = False
    start = len(prefix)
    end = len(prefix) + len(data) - 1
    return head, start, end, ans

  for case in range(9, 10):
    head, start, end, ans = get_inputs(case)
    res = is_palindromic(head, start, end)
    assert res == ans
  print('is_palindromic success')

def test_is_cyclic():
  def get_inputs(case):
    src = list(range(7))
    cyclic_to = None
    head = gen_list(src, cyclic_to)
    counts = None
    ans_cycle_len = 0
    ans = None
    if case == 0:
      pass
    elif case == 1:
      cyclic_to = 2
      head = gen_list(src, cyclic_to)
      ans = head.nxt.nxt
    elif case == 2: # one node and self-loop, that is node.nxt is node itself.
      src = [0]
      cyclic_to = 0
      head = gen_list(src, cyclic_to)
      ans = head
      return head, 2, 1, head.nxt.nxt
    if isinstance(cyclic_to, int):
      counts = len(src) + 1
      ans_cycle_len = len(src) - cyclic_to
    return head, counts, ans_cycle_len, ans

  for case in range(3):
    head, counts, ans_cycle_len, ans = get_inputs(case)
    res, res_cycle_len = is_cyclic(head)
    assert res == ans
    assert res_cycle_len == ans_cycle_len
  print('is_cyclic success')

# Test utils ends

def main():
  test_rotate_in_place()
  test_remove_duplicates_in_a_sorted_list()
  test_remove_duplicates_in_an_unsorted_list()
  test_merge_two_sorted_lists()
  test_merge_two_adjacent_sublists_in_a_src_list()
  test_reverse_a_sublist()
  test_is_palindromic()
  test_parition()
  test_is_cyclic()

if __name__ == '__main__':
  main()

