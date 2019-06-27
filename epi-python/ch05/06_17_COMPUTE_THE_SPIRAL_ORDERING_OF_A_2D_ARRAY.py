from __future__ import print_function

def get_spiral_seq(x):
  """
    Time complexity is O(n^2) where n it the number of rows of x (here rows = cols)
    Additional space complexity is O(1) (not including the necessary return value)
  """
  seq = []
  rounds = len(x) / 2 # x is a square matrix from the problem's spec, that is rows = cols
  last_round = rounds - 1
  is_odd = bool(len(x) & 1)
  for r in xrange(rounds):
    top_row = r
    right_col = len(x) - 1 - r
    bottom_row = len(x) - 1 - r
    left_col = r

    # append top row elements
    for col in xrange(left_col ,right_col):
      seq.append(x[top_row][col])

    # append right col elements
    for row in xrange(top_row, bottom_row):
      seq.append(x[row][right_col])

    # append bottom row elements
    for col in xrange(right_col, left_col, -1):
      seq.append(x[bottom_row][col])

    # append left col elements
    for row in xrange(bottom_row, top_row, -1):
      seq.append(x[row][left_col])

  if is_odd: seq.append(x[rounds][rounds])
  return seq

def get_input(case=0):
  if case == 0:
    x = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ]
    ans = [1,2,3,6,9,8,7,4,5]
  elif case == 1:
    x = [
      [ 1, 2, 3, 4],
      [ 5, 6, 7, 8],
      [ 9,10,11,12],
      [13,14,15,16],
    ]
    ans = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

  return x, ans

def main():
  for arg in xrange(2):
    x, ans = get_input(arg)
    res = get_spiral_seq(x)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
