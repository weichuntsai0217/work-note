from __future__ import print_function

def is_pattern_existed(src, ptn):
  """
    Time complexity: O(mns), m is the number of rows of src, n is the number of columns of src, s is the length of ptn.
  """
  attempts = set()
  for row in xrange(len(src)):
    for col in xrange(len(src[0])):
      if search_pattern(src, (row, col), ptn, 0, attempts):
        return True
  return False
    

def get_valid_cors(src, src_cor):
  res = []
  row, col = src_cor
  if row - 1 >= 0 and row - 1 <= len(src) - 1:
    res.append((row - 1, col))
  if col + 1 >= 0 and col + 1 <= len(src[0]) - 1:
    res.append((row, col + 1))
  if row + 1 >= 0 and row + 1 <= len(src) - 1:
    res.append((row + 1, col))
  if col - 1 >= 0 and col - 1 <= len(src[0]) - 1:
    res.append((row, col - 1))
  return res

def search_pattern(src, src_cor, ptn, ptn_idx, attempts):
  if ptn_idx == len(ptn): return True
  if (src_cor[0], src_cor[1], ptn_idx) in attempts: return False
  if src[src_cor[0]][src_cor[1]] == ptn[ptn_idx]:
    valid_cors = get_valid_cors(src, src_cor)
    for cor in valid_cors:
      if search_pattern(src, cor, ptn, ptn_idx + 1, attempts):
        return True
  attempts.add((src_cor[0], src_cor[1], ptn_idx))
  return False

def get_input(hard=False, no_pattern=False):
  src = None
  ptn = None
  ans = True
  if hard:
    src = [
      [1, 6, 7, 55],
      [3, 1, 5, 10],
      [1, 6, 7, 22],
      [7, 1, 4, 33],
    ]
    if no_pattern:
      ptn = [1, 6, 7, 1]
      ans = False
    else:
      ptn = [1, 4, 1]
  else:
    src = [
      [1, 2, 3],
      [3, 4, 5],
      [5, 6, 7],
    ]
    if no_pattern:
      ptn = [1, 3, 4, 7]
      ans = False
    else:
      ptn = [1, 3, 4, 6]
  return src, ptn, ans

def main():
  for hard, no_pattern in [(False, False), (False, True), (True, False), (True, True)]:
    src, ptn, ans = get_input(hard, no_pattern)
    print('Test success.' if is_pattern_existed(src, ptn) == ans else 'Test failure.')

if __name__ == '__main__':
  main()
