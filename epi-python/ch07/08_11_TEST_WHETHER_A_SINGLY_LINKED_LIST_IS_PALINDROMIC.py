from __future__ import print_function
from utils_ch08 import Node, gen_list, get_list_str, is_equal

def is_palindromic(head):
  """
    The time complexity is O(n) where n is the length of the list
    The additional space complexity is O(n)
  """
  if not head: return True
  history = []
  node = head
  while node:
    history.append(node.data)
    node = node.nxt
  last = len(history) - 1
  for i in xrange(len(history)/2):
    if history[i] != history[last-i]:
      return False
  return True

def reverse_list(head):
  if not head.nxt: return head
  dummy_head = Node(0, head)
  end = dummy_head.nxt
  while end.nxt:
    tmp = end.nxt
    end.nxt = end.nxt.nxt
    tmp.nxt = dummy_head.nxt
    dummy_head.nxt = tmp
  return dummy_head.nxt


def is_palindromic_less_space(head):
  """
    The time complexity is O(n) where n is the length of the list
    The additional space complexity is O(1).
  """
  if not head: return True

  slow = head
  fast = head
  while fast and fast.nxt:
    slow = slow.nxt
    fast = fast.nxt.nxt

  first_half_iter = head
  second_half_iter = reverse_list(slow)
  """
  second_half_head = second_half_iter
  """
  while first_half_iter and second_half_iter:
    if first_half_iter.data != second_half_iter.data:
      """
      you can reverse 2nd half sublist back to original here,
      depends on the interviewr's opinion:
        second_half_head = reverse_list(second_half_head)
      """
      return False
    first_half_iter = first_half_iter.nxt
    second_half_iter = second_half_iter.nxt
  """
  you can reverse 2nd half sublist back to original here,
  depends on the interviewr's opinion:
    second_half_head = reverse_list(second_half_head)
  """
  return True
  
def get_input(case=0):
  if case == 0:
    return None, True
  elif case == 1:
    return gen_list([1]), True
  elif case == 2:
    return gen_list([1,1]), True
  elif case == 3:
    return gen_list([1,2]), False
  elif case == 4:
    return gen_list([7,3,1,5,1,3,7]), True
  elif case == 5:
    return gen_list([7,3,1,5,2,3,7]), False

def main():
  print('Use is_palindromic =====')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    head, ans = get_input(case)
    res = is_palindromic(head)
    print(res)
    print('Test success' if res == ans else 'Test failure')

  print('Use is_palindromic_less_space =====')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    head, ans = get_input(case)
    res = is_palindromic_less_space(head)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
