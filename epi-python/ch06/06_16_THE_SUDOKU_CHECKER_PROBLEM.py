from __future__ import print_function

def get_table():
  return {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
  }

def is_duplicated_row(x, r):
  table = get_table()
  for i in x[r]:
    if i != 0:
      if table[i] == 0:
        table[i] = 1
      else:
        return True
  return False

def is_duplicated_col(x, c):
  table = get_table()
  for j in xrange(len(x)): # a sudoku game has same rows and columns (9X9)
    i = x[j][c]
    if i != 0:
      if table[i] == 0:
        table[i] = 1
      else:
        return True
  return False

def is_duplicated_region(x, r, c):
  table = get_table()
  for j in xrange(r, r + 3):
    for k in xrange(c, c + 3):
      i = x[j][k]
      if i != 0:
        if table[i] == 0:
          table[i] = 1
        else:
          return True
  return False

def is_valid_sudoku(x):
  """
    Time complexity is O(n^2) where n is the number of row in x (rows and columns are the same in sudoku game)
    Additional space complexity is O(n) because we use get_table
  """
  for r in xrange(len(x)):
    if is_duplicated_row(x, r):
      return False

  for c in xrange(len(x)):
    if is_duplicated_col(x, c):
      return False

  for r in xrange(0, 9, 3):
    for c in xrange(0, 9, 3):
      if is_duplicated_region(x, r, c):
        return False

  return True

def get_input():
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
  return game, True

def main():
  x, ans = get_input()
  res = is_valid_sudoku(x)
  print(res)
  print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
