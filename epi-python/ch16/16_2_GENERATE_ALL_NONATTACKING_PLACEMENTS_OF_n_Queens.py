from __future__ import print_function

def is_valid(sol):
  last_row = len(sol) - 1
  for i in xrange(last_row):
    diff = abs(sol[i] - sol[last_row])
    if (diff == 0) or (diff == (last_row - i)):
      return False
  return True

def n_queens(n):
  """
    The time complexity is about (n!)/(c^n), no exactly form.
    The additional space complexity is O(n)
  """
  def recursive(n, row, sol, res):
    if row == n:
      res.append([x for x in sol])
      return
    for j in xrange(n):
      sol.append(j)
      if is_valid(sol):
        recursive(n, row+1, sol, res)
      sol.pop()

  res = []
  sol = []
  recursive(n, 0, sol, res)
  return res

def show_res(res, n):
  def gen_default_board(n):
    default_board = []
    for i in xrange(n):
      default_board.append([])
      for j in xrange(n):
        default_board[i].append('O')
    return default_board
  table = {}
  for sol in res:
    s = str(sol)
    if s not in table:
      table[s] = 0
    table[s] += 1
    print('sol =', s)
    board = gen_default_board(n)
    for row, col in enumerate(sol):
      board[row][col] = 'X'
    print('    ', [str(item) for item in xrange(n)])
    for i, row_data in enumerate(board):
      print(i, '=>', row_data)
    print('\n')

  for key in table:
    if table[key] > 1:
      print('duplicated: ', key, table[key])
    print('key = {}  count = {}'.format(key, table[key]))

def get_input(case=0):
  n = 3
  ans = []
  if case == 0:
    pass
  elif case == 1:
    n = 4
    ans = []
  elif case == 2:
    n = 5
    ans = []
  return n, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    n, ans = get_input(case)
    print('Input:')
    print('Output:')
    res = n_queens(n)
    show_res(res, n)

if __name__ == '__main__':
  main()

