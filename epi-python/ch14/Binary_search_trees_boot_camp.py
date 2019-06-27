from __future__ import print_function
import bst 

def get_input(case=0):
  root = bst.BinaryTreeNode(3)
  for i in xrange(7):
    if i != 3:
      bst.Bst.insert(root, bst.BinaryTreeNode(i))
  key = 3
  ans = root
  if case == 0:
    pass
  elif case == 1:
    key = 1
    ans = root.left.right
  elif case == 2:
    key = 5
    ans = root.right.right
  elif case == 3:
    key = 6
    ans = root.right.right.right
  return root, key, ans


def main():
  root, key, ans = get_input()
  print('root =\n', root)
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    root, key, ans = get_input(case)
    print('Input:')
    print('key =', key)
    print('Output:')
    res = bst.Bst.search(root, key)
    print('res =', res.data)
    print('ans =', ans.data)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
