from __future__ import print_function

def get_row_constraint(matrix):
  table = {}
  for i in xrange(len(matrix)):
    table[i] = {
      1: False,
      2: False,
      3: False,
      4: False,
      5: False,
      6: False,
      7: False,
      8: False,
      9: False,
    }
    for j in xrange(len(matrix[i])):
      if matrix[i][j] != None:
        table[i][matrix[i][j]] = True
  return table

def get_col_constraint(matrix):
  table = {}
  for j in xrange(len(matrix)):
    table[j] = {
      1: False,
      2: False,
      3: False,
      4: False,
      5: False,
      6: False,
      7: False,
      8: False,
      9: False,
    }
    for i in xrange(len(matrix)):
      if matrix[i][j] != None:
        table[j][matrix[i][j]] = True
  return table

def get_reg_idx(i, j):
  grid_row = i / 3
  grid_col = j / 3
  return grid_row * 3 + grid_col

def get_reg_constraint(matrix):
  table = {}
  for i in xrange(len(matrix)):
    for j in xrange(len(matrix[i])):
      reg_idx = get_reg_idx(i, j)
      if reg_idx not in table:
        table[reg_idx] = {
          1: False,
          2: False,
          3: False,
          4: False,
          5: False,
          6: False,
          7: False,
          8: False,
          9: False,
        }
      if matrix[i][j] != None:
        table[reg_idx][matrix[i][j]] = True
  return table

def sudoku_solver(matrix):
  """
    The time complexity for 9 x 9 sudoku is O(1).
    I use 3 table to enhance performance.
  """
  row_ct = get_row_constraint(matrix) # ct is constraint.
  col_ct = get_col_constraint(matrix)
  reg_ct = get_reg_constraint(matrix) # reg is region

  def get_candidates(matrix, i, j):
    cs = []
    target_row_ct = row_ct[i]
    target_col_ct = col_ct[j]
    target_reg_ct = reg_ct[get_reg_idx(i, j)]
    for key in xrange(1, 10):
      if (
        (not target_row_ct[key]) and
        (not target_col_ct[key]) and
        (not target_reg_ct[key])
      ):
        cs.append(key)
    return cs

  def set_constraints(matrix, i, j, key, m_val, ct_val):
    target_row_ct = row_ct[i]
    target_col_ct = col_ct[j]
    target_reg_ct = reg_ct[get_reg_idx(i, j)]
    matrix[i][j] = m_val
    target_row_ct[key] = ct_val
    target_col_ct[key] = ct_val
    target_reg_ct[key] = ct_val

  def get_next_row_col(matrix, start_row, start_col):
    j = start_col
    while j < len(matrix[start_row]):
      if matrix[start_row][j] == None:
        return start_row, j
      j += 1
    for i in xrange(start_row+1, len(matrix)):
      for j in xrange(len(matrix[i])):
        if matrix[i][j] == None:
          return i, j
    return None, None

  def recursive(matrix, i, j):
    if (i == None) and (j == None):
      return True
    candidates = get_candidates(matrix, i, j)
    if candidates:
      for number in candidates:
        set_constraints(matrix, i, j, number, number, True)
        next_i, next_j = get_next_row_col(matrix, i, j+1)
        if recursive(matrix, next_i, next_j):
          return True
        set_constraints(matrix, i, j, number, None, False)
    return False
 
  i, j = get_next_row_col(matrix, 0, 0)  
  recursive(matrix, i, j)
  return matrix

def get_input(case=0):
  game = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
  ]
  for i in xrange(len(game)):
    for j in xrange(len(game[i])):
      if game[i][j] == 0:
        game[i][j] = None
  ans = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
  ]
  return game, ans

def show_res(game):
  for row in game:
    print(row)

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    print('Input:')
    game, ans = get_input(case)
    print('game =', game)
    print('Output:')
    res = sudoku_solver(game)
    print('res =')
    show_res(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()





