from __future__ import print_function
import bst 

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  ans = True
  if case == 0:
    pass
  elif case == 1:
    root.left.left.left.data = 4
    ans = False
  elif case == 2:
    root.left.right.right.data = 10
    ans = False
  elif case == 3:
    root.right.right.right.data = 46
    ans = False
  elif case == 4:
    root.right.left.right.left.data = 38
    ans = False
  elif case == 5:
    root.data = 100
    ans = False

  return root, ans


def main():
  print('Use bst.Bst.is_bst')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    if case == 0:
      print('Input:')
      print('root =', root)
    print('Output:')
    res = bst.Bst.is_bst(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')
  print('\n==========')
  print('Use bst.Bst.is_bst_use_bfs')
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    root, ans = get_input(case)
    if case == 0:
      print('Input:')
      print('root =', root)
    print('Output:')
    res = bst.Bst.is_bst_use_bfs(root)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

