from __future__ import print_function
import bst

def get_input(case=0):
  root = bst.get_bst_from_epi_page_255()
  ans_status = True
  ans_root = None
  if case == 0:
    key = 7
    ans_root = bst.get_bst_from_epi_page_255(
      [19, 11, 43, 3, 17, 23, 47, 2, 5, 13, 37, 53, 29, 41, 31]
    ) 
  elif case == 1:
    key =  23
    ans_root = bst.get_bst_from_epi_page_255(
      [19, 7, 43, 3, 11, 29, 47, 2, 5, 17, 37, 53, 13, 31, 41]
    ) 
  elif case == 2:
    key = 31
    ans_root = bst.get_bst_from_epi_page_255(
      [19, 7, 43, 3, 11, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41]
    ) 
  elif case == 3:
    key = 1087
    ans_status = False
    ans_root = bst.get_bst_from_epi_page_255()
  return root, key, ans_status, ans_root

def main():
  root, key, ans_status, ans_root = get_input()
  print('The bst for each input case is:', root)
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    root, key, ans_status, ans_root = get_input(case)
    print('Input:')
    print('key =', key)
    print('Output:')
    status, root = bst.Bst.delete(root, key)
    print('root =', root)
    print('status =', status)
    print('ans_root =', ans_root)
    print('ans_status =', ans_status)
    print('Test success' if status == ans_status and bst.get_tree_traversal_str(root, order='preorder') == bst.get_tree_traversal_str(ans_root, order='preorder') else 'Test failure')

if __name__ == '__main__':
  main()


