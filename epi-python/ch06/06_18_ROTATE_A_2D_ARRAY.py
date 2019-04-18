from __future__ import print_function

def rotate_2d_array(m):
  """
    Time complexity is O(n^2) where n is the number of rows/cols of m (because m is a square matrix.)
    Additional sapce complexity is O(n^2) where n is the number of rows/cols of m
  """
  res = []

  for col in xrange(len(m[0])):
    res.append([])
    res_row = len(res) - 1
    for row in xrange(len(m) - 1, -1 , -1):
      res[res_row].append(m[row][col])

  return res

def rotate_2d_array_in_place(m):
  """
    Time complexity is O(n^2) where n is the number of rows/cols of m (because m is a square matrix.)
    Additional sapce complexity is O(1)
  """
  last = len(m) - 1 # m is a square matrix.
  for i in xrange(len(m)/2):
    for j in xrange(i, last - i):
      tmp_1 = m[i][j]
      tmp_2 = m[j][last - i]
      tmp_3 = m[last - i][last - j]
      tmp_4 = m[last - j][i]
      m[i][j] = tmp_4
      m[j][last - i] = tmp_1
      m[last - i][last - j] = tmp_2
      m[last - j][i] = tmp_3

def get_input():
  m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
  ]
  ans = [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4],
  ]
  return m, ans

def main():
  m, ans = get_input()
  res = rotate_2d_array(m)
  print(res)
  print('Test success' if res == ans else 'Test success')

  print('=== Use in-place')
  m, ans = get_input()
  rotate_2d_array_in_place(m)
  print(m)
  print('Test success' if m == ans else 'Test success')
if __name__ == '__main__':
  main()
