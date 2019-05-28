from __future__ import print_function
import bst

def get_range(root, interval):
  """
    The time complexity is O(h+m) where h is the bst height and m is the number of node data which lies in the interval.
    If the interval covers the min node and the max node, then m = n.
    I think it is still OK to say that the time complexity is O(n).
    The additional space complexity is O(h) because we need to record left_candidates and right_candidates.
  """
  def traverse_inorder(root, res):
    if not root:
      return
    traverse_inorder(root.left, res)
    res.append(root.data)
    traverse_inorder(root.right, res)
  node = root
  start, end = interval
  while node:
    if (node.data >= start) and (node.data <= end):
      break
    elif node.data < start:
      node = node.right
    else: # node.data > end
      node = node.left
  if not node:
    return [] # all data in bst are larger or less than the interval.
  res = []
  split_node = node
  left_candidates = []
  node = split_node.left
  while node:
    if node.data < start:
      node = node.right
    else:
      left_candidates.append(node)
      node = node.left
  right_candidates = []
  node = split_node.right
  while node:
    if node.data > end:
      node = node.left
    else:
      right_candidates.append(node)
      node = node.right

  for i in xrange(len(left_candidates)-1, -1, -1):
    can = left_candidates[i]
    res.append(can.data)
    traverse_inorder(can.right, res)

  res.append(split_node.data) 

  for can in right_candidates:
    traverse_inorder(can.left, res)
    res.append(can.data)
  return res

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  interval = [16, 31]
  ans = [17,19,23,29,31]
  if case == 0:
    pass
  elif case == 1:
    interval = [2, 31]
    ans = [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29, 31]
  return root, interval, ans

def main():
  root, interval, ans = get_input()
  print('The bst for each input case is:', root)
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    root, interval, ans = get_input(case)
    print('Input:')
    print('interval =', interval)
    print('Output:')
    res = get_range(root, interval)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()




