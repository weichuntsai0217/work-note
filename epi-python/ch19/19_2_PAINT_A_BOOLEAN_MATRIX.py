from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

from copy import deepcopy

def flip_maze(start, maze, is_start_black=False, use_bfs=False):
  if use_bfs:
    bfs(start, maze, is_start_black)
    return maze
  dfs(start, maze, is_start_black)
  return maze

def get_reachable_neighbors(cur, maze, is_start_black=False):
  color = 0 if is_start_black else 1
  reachable_neighbors = []
  max_row = len(maze) - 1
  max_col = len(maze[0]) - 1
  [row, col] = cur
  top = [row - 1, col] if (row - 1) >= 0 else None
  right = [row, col + 1] if (col + 1) <= max_col else None
  bottom = [row + 1, col] if (row + 1) <= max_row else None
  left = [row, col - 1] if (col - 1) >= 0 else None
  for nbr in [top, right, bottom, left]:
    if nbr and (maze[nbr[0]][nbr[1]] == color): reachable_neighbors.append(nbr)
  return reachable_neighbors

def dfs(cur, maze, is_start_black=False):
  print('this is dfs')
  color_to_paint = 1 if is_start_black else 0
  maze[cur[0]][cur[1]] = color_to_paint # mark the cur point as 0 means this point is visited.
  reachable_neighbors = get_reachable_neighbors(cur, maze, is_start_black)
  if len(reachable_neighbors) == 0:
    return
  for nbr in reachable_neighbors:
    dfs(nbr, maze, is_start_black)
  return

def get_reachable_neighbors_bfs(cur, maze, is_start_black=False):
  color = 0 if is_start_black else 1
  reachable_neighbors = []
  max_row = len(maze) - 1
  max_col = len(maze[0]) - 1
  [row, col] = cur
  top = [row - 1, col] if (row - 1) >= 0 else None
  right = [row, col + 1] if (col + 1) <= max_col else None
  bottom = [row + 1, col] if (row + 1) <= max_row else None
  left = [row, col - 1] if (col - 1) >= 0 else None
  for nbr in [top, right, bottom, left]:
    if nbr and (maze[nbr[0]][nbr[1]] == color):
      maze[nbr[0]][nbr[1]] = int(not bool(color))
      reachable_neighbors.append(nbr)
  return reachable_neighbors

def show_dup_item_in_queue(queue):
  for index, item in enumerate(queue):
    if item in queue[index+1:]:
      print('There is a duplicated item in queue')
      print('index =', index)
      print('item = ', item)
      break

def bfs(start, maze, is_start_black=False):
  print('this is bfs')
  queue = []
  color_to_paint = 1 if is_start_black else 0
  queue.append(start)
  maze[start[0]][start[1]] = color_to_paint
  while queue:
    print(queue)
    reachable_neighbors = get_reachable_neighbors_bfs(queue[0], maze, is_start_black)
    queue.pop(0)
    queue += reachable_neighbors
    show_dup_item_in_queue(queue)

def get_input(is_start_black=False):
  """
    0 means black
    1 means white
  """
  maze = [
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
  ]
  start = [5, 4]
  if is_start_black:
    start = [3, 6]
    for i in range(4, 10):
      for j in range(0, 7):
        maze[i][j] = 0
  return (start, maze)

def draw_maze(maze):
  for row in maze:
    print(row)

def show_result(maze, flipped_maze):
  print('The original maze is:')
  draw_maze(maze)
  print('\n')
  print('The flipped maze is:')
  draw_maze(flipped_maze)
  print('\n\n')

def main():
  """
    The worst case time complexity is O(4 * V) ~= ~= O(V) ~= O(m * n) where m is the number of rows and n is the number of columns.
    In bfs, you would see that the maximum nodes of queue is at most total vertexes, and each node contains at most 4 edges.
    So the complexity is O(4 * V).
    The worst case means that you traverse all points and paint them.
  """
  use_bfs = bool(sys.argv[1]) if len(sys.argv) > 1 else False

  is_start_black = False
  (start, maze) = get_input(is_start_black)
  flipped_maze = flip_maze(start, deepcopy(maze), is_start_black, use_bfs)
  show_result(maze, flipped_maze)


  is_start_black = True
  (start, maze) = get_input(is_start_black)
  print(flipped_maze == maze)
  flipped_maze = flip_maze(start, deepcopy(maze), is_start_black, use_bfs)
  show_result(maze, flipped_maze)

  is_start_black = False
  start = [0, 0]
  maze = [[1, 1], [1, 1]]
  flipped_maze = flip_maze(start, deepcopy(maze), is_start_black, use_bfs)
  show_result(maze, flipped_maze)

if __name__ == '__main__':
  main()
