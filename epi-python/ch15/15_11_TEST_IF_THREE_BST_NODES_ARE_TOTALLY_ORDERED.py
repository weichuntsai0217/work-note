from __future__ import print_function
import bst

def can_go(src, dst):
  while src and src != dst:
    if src.data > dst.data:
      src = src.left
    else:
      src = src.right
  return src == dst

def is_total_ordered(node_0, node_1, m_node):
  """
    If return is True, then the time complexity is O(d) where d is the depth difference between node_0 and node_1
    If return is False, then the time complexity is O(h) where h is the height of the bst.
    The additional space complexity is O(1).
  """
  search_0 = node_0
  search_1 = node_1
  while (
    (search_0 or search_1) and
    (search_0 != m_node) and
    (search_1 != m_node) and
    (search_0 != node_1) and
    (search_1 != node_0)
  ):
    if search_0:
      if search_0.data > m_node.data:
        search_0 = search_0.left
      else:
        search_0 = search_0.right
    if search_1:
      if search_1.data > m_node.data:
        search_1 = search_1.left
      else:
        search_1 = search_1.right
  if (
    (search_0 == node_1) or
    (search_1 == node_0) or
    ((search_0 != m_node) and (search_1 != m_node))
  ):
    return False
  return can_go(m_node, node_1) if search_0 == m_node else can_go(m_node, node_0)

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  node_0 = root.right
  node_1 = root.right.left.right.left.right
  m_node = root.right.left.right
  ans = True
  if case == 0:
    pass
  elif case == 1:
    node_1 = root.right
    node_0 = root.right.left.right.left.right
  elif case == 2:
    node_0 = root.left
    node_1 = root.right
    m_node = root.left.right.right
    ans = False

  return root, node_0, node_1, m_node, ans

def main():
  root, node_0, node_1, m_node, ans = get_input()
  print('The bst for each input case is:', root)
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    root, node_0, node_1, m_node, ans = get_input(case)
    print('Input:')
    print('node_0.data =', node_0.data)
    print('node_1.data =', node_1.data)
    print('m_node.data =', m_node.data)
    print('Output:')
    res = is_total_ordered(node_0, node_1, m_node)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()



