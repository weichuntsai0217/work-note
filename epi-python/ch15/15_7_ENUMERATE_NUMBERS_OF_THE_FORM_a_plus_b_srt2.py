from __future__ import print_function
import bst

class Item(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    self.val = a + b*(2.0 ** 0.5)

  def __eq__(self, other):
    if not isinstance(other, Item):
      return False
    return (self.a == other.a) and (self.b == other.b)
  def __lt__(self, other):
    if not isinstance(other, Item):
      return False
    if self.__eq__(other):
      return False
    return self.val < other.val
  def __le__(self, other):
    if not isinstance(other, Item):
      return False
    return self.__eq__(other) or self.__lt__(other)
  def __gt__(self, other):
    if not isinstance(other, Item):
      return False
    return not self.__le__(other)
  def __ge__(self, other):
    if not isinstance(other, Item):
      return False
    return self.__eq__(other) or self.__gt__(other)
  def __str__(self):
    return str(self.val)

def enum_a_plus_b_sqrt2(k):
  """
    The time complexity is O(k * h) where h is the bst height of root.
    (If the bse library you use is a self-balanced tree, then h = logk)
    The additional space complexity is O(k)
  """
  root = bst.BinaryTreeNode(Item(0, 0))
  res = []
  while len(res) < k:
    next_smallest = bst.Bst.first(root).data
    res.append(next_smallest)
    bst.Bst.insert(root, bst.BinaryTreeNode(Item(next_smallest.a + 1, next_smallest.b)))
    bst.Bst.insert(root, bst.BinaryTreeNode(Item(next_smallest.a, next_smallest.b + 1)))
    tmp, root = bst.Bst.pop_first(root)
  return res

def enum_a_plus_b_sqrt2_fast(k):
  """
    The time complexity is O(k).
    The additional space complexity is O(1).
  """
  res = [Item(0, 0)]
  i = 0
  j = 0
  while len(res) < k:
    plus_1 = Item(res[i].a + 1, res[i].b)
    plus_sqrt2 = Item(res[j].a, res[j].b + 1)
    res.append(plus_1 if plus_1 < plus_sqrt2 else plus_sqrt2)
    if res[-1] == plus_1:
      i += 1
    if res[-1] == plus_sqrt2:
      j += 1
  return res

def get_num_str(x):
  return '{:.5f}'.format(x)

def get_input(case=0):
  k = 15
  ans = [0.0, 1.0, 1.4142135623730951, 2.0, 2.414213562373095, 2.8284271247461903, 3.0, 3.414213562373095, 3.8284271247461903, 4.0, 4.242640687119286, 4.414213562373095, 4.82842712474619, 5.0, 5.242640687119286]
  ans = [get_num_str(x) for x in ans]
  if case == 0:
    pass
  return k, ans

def main():
  print('Use enum_a_plus_b_sqrt2:')
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    k, ans = get_input(case)
    print('Input:')
    print('k =', k)
    print('Output:')
    res_src = enum_a_plus_b_sqrt2(k)
    res = [ get_num_str(x.val) for x in res_src ]
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('\n========================')
  print('Use enum_a_plus_b_sqrt2_fast:')
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    k, ans = get_input(case)
    print('Input:')
    print('k =', k)
    print('Output:')
    res_src = enum_a_plus_b_sqrt2_fast(k)
    res = [ get_num_str(x.val) for x in res_src ]
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
