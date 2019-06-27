from __future__ import print_function

def is_overlap(a, b):
  return a[1][0] >= b[0][0] and a[0][0] <= b[1][0]

def is_left_to(a, b):
  return a[1][0] < b[0][0]

def get_min_point(p_a, p_b):
  point = None
  is_point_closed = None
  if p_a[0] < p_b[0]:
    point = p_a[0]
    is_point_closed = p_a[1]
  elif p_a[0] == p_b[0]:
    point = p_a[0]
    is_point_closed = p_a[1] or p_b[1]
  else: # p_a[0] > p_b[0]
    point = p_b[0]
    is_point_closed = p_b[1]
  return (point, is_point_closed)

def get_max_point(p_a, p_b):
  point = None
  is_point_closed = None
  if p_a[0] < p_b[0]:
    point = p_b[0]
    is_point_closed = p_b[1]
  elif p_a[0] == p_b[0]:
    point = p_b[0]
    is_point_closed = p_a[1] or p_b[1]
  else: # p_a[0] > p_b[0]
    point = p_a[0]
    is_point_closed = p_a[1]
  return (point, is_point_closed)

def compute_union_intervals(array):
  """ 
  array = [item, item, ...]
  item = [(0, True), (2, False)] => [(left, is_left_closed), (right, is_left_closed)]

  The time complexity is O(n * logn) where n is the array length.
  The additional space complexity is O(1).
  """
  if len(array) <= 0: return array
  array.sort(key=lambda x: x[0][0])
  res = []
  i = 0
  j = 1
  while i < len(array):
    mg_itr = [array[i][0], array[i][1]]
    while j < len(array):
      if is_left_to(mg_itr, array[j]):
        break
      elif is_overlap(mg_itr, array[j]):
        mg_itr = [
          get_min_point(mg_itr[0], array[j][0]),
          get_max_point(mg_itr[1], array[j][1]),
        ]
      j += 1
    res.append(mg_itr)
    i = j
    j += 1
  return res

  
def get_input(case=0):
  array = [
    [(2, True), (4, True)],
    [(8, True), (11, False)],
    [(13, False), (15, False)],
    [(16, False), (17, False)],
    [(1, True), (1, True)],
    [(3, True), (4, False)],
    [(7, True), (8, False)],
    [(12, False), (16, True)],
    [(0, False), (3, False)],
    [(5, True), (7, False)],
    [(9, False), (11, True)],
    [(12, True), (14, True)],
  ]
  ans = [[(0, False), (4, True)], [(5, True), (11, True)], [(12, True), (17, False)]]
  if case == 0:
    pass
  return array, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = compute_union_intervals(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()






