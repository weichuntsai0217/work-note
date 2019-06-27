from __future__ import print_function

def search_in_a_sorted_2d_array(matrix, t):
  """
    The time complexity is O(m + n) where m is the number of rows and n is the number of columns
  """
  total_rows = len(matrix)
  row = 0
  col = len(matrix[0]) - 1
  while (row < total_rows) and (col >= 0):
    if matrix[row][col] == t:
      return True 
    elif matrix[row][col] < t:
      row += 1
    else:
      col -= 1
  return False


def get_input(case=0):
  x = [
    [-1, 2, 4, 4, 6],
    [1, 5, 5, 9, 21],
    [3, 6, 6, 9, 22],
    [3, 6, 8, 10, 24],
    [6, 8, 9, 12, 25],
    [8, 10, 12, 13, 40],
  ]
  t = -1
  ans = True
  if case == 0:
    pass
  elif case == 1:
    t = 6
    ans = True
  elif case == 2:
    t = 8
    ans = True
  elif case == 3:
    t = 40
    ans = True
  elif case == 4:
    t = 7
    ans = False
  elif case == 5:
    t = 9
    ans = True
  elif case == 6:
    t = 12
    ans = True
  elif case == 7:
    t = 13
    ans = True
  elif case == 8:
    t = 3
    ans = True
  elif case == 9:
    t = 41
    ans = False
  elif case == 10:
    t = -2
    ans = False
  return x, t, ans
    
def show_matrix(x):
  for i, row in enumerate(x):
    print(i, ' =>', row)

def main():
  for case in xrange(11):
    print('--- case {} ---'.format(case))
    x, t, ans = get_input(case)
    # print('Input:')
    # print('x =')
    # show_matrix(x)
    print('t =', t)
    print('Output:')
    res = search_in_a_sorted_2d_array(x, t)
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()




