from __future__ import print_function
from copy import deepcopy

def get_boundary_whites(board):
  if len(board) == 0: return []
  last_row = len(board) - 1
  last_col = len(board[0]) - 1
  boundary_ws = []

  for col, item in enumerate(board[0]):
    if item == 'W': boundary_ws.append([0, col])

  for row, item in enumerate(board):
    if item[last_col] == 'W': boundary_ws.append([row, last_col])

  for col, item in enumerate(board[last_row]):
    if item == 'W': boundary_ws.append([last_row, col])

  for row, item in enumerate(board):
    if item[0] == 'W': boundary_ws.append([row, 0])

  return boundary_ws


def get_init_visited(board):
  tot_rows = len(board)
  tot_cols = len(board[0])
  visited = []
  for i in range(tot_rows):
    visited.append([])
    for j in range(tot_cols):
      visited[i].append(False)
  # be careful:
  # return [[False]*tot_cols]*tot_rows would cause "reference to self" problem!!!!!!!!!!!
  return visited

def is_valid_white(node, tot_rows, tot_cols, board, visited):
  row = node[0]
  col = node[1]
  if row < 0 or row >= tot_rows: return False
  if col < 0 or col >= tot_cols: return False
  if board[row][col] != 'W': return False
  if visited[row][col]: return False
  return True

def bfs(board, start, visited):
  tot_rows = len(board)
  tot_cols = len(board[0])
  queue = []
  dpos = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  row = start[0]
  col = start[1]
  if visited[row][col]: return
  visited[row][col] = True
  queue.append(start)
  while queue:
    center = queue[0]
    for p in dpos:
      node = [center[0]+p[0], center[1]+p[1]]
      if is_valid_white(node, tot_rows, tot_cols, board, visited):
        visited[node[0]][node[1]] = True
        queue.append(node)
    queue.pop(0)
    

def paint_enclosed_whites_to_blacks(board):
  bws = get_boundary_whites(board)
  visited = get_init_visited(board)
  for item in bws:
    bfs(board, item, visited)

  for i, row_item in enumerate(board):
    for j, col_item in enumerate(row_item):
      if col_item == 'W' and not visited[i][j]:
        board[i][j] = 'B'
  return board

def draw_matrix(matrix):
  for row in matrix:
    print(row)
  print('\n')

def main():
  """
    The worst case time complexity is O(4 * V) ~= ~= O(V) ~= O(m * n) where m is the number of rows and n is the number of columns.
    In bfs, you would see that the maximum nodes of queue is at most total vertexes, and each node contains at most 4 edges.
    So the complexity is O(4 * V).
    The worst case means that you traverse all points and paint them.
  """
  board = [
    ['B', 'W', 'B', 'B'],
    ['W', 'B', 'W', 'W'],
    ['B', 'W', 'W', 'B'],
    ['B', 'B', 'B', 'B'],
  ]

  res_board = paint_enclosed_whites_to_blacks(deepcopy(board))
  draw_matrix(board)
  draw_matrix(res_board)

if __name__ == '__main__':
  main()
