from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

from copy import deepcopy

def get_maze_path(entrance, exit, maze):
  if maze[entrance[0]][entrance[1]] == 0 or maze[exit[0]][exit[1]] == 0: return False
  path = []
  dfs(entrance, exit, maze, path)
  return path

def get_reachable_neighbors(cur, maze):
  reachable_neighbors = []
  max_row = len(maze) - 1
  max_col = len(maze[0]) - 1
  [row, col] = cur
  top = [row - 1, col] if (row - 1) >= 0 else None
  right = [row, col + 1] if (col + 1) <= max_col else None
  bottom = [row + 1, col] if (row + 1) <= max_row else None
  left = [row, col - 1] if (col - 1) >= 0 else None
  for nbr in [top, right, bottom, left]:
    if nbr and maze[nbr[0]][nbr[1]]: reachable_neighbors.append(nbr)
  return reachable_neighbors

def dfs(cur, exit, maze, path):
  path.append(cur)
  if cur == exit: return True
  maze[cur[0]][cur[1]] = 0 # mark the cur point as 0 means this point is visited.
  reachable_neighbors = get_reachable_neighbors(cur, maze)
  if len(reachable_neighbors) == 0:
    path.pop(len(path)-1)
    return False
  for nbr in reachable_neighbors:
    if dfs(nbr, exit, maze, path):
      return True
  path.pop(len(path)-1)
  return False

def get_input(not_pass=False):
  """
    0 means wall
    1 means road
  """
  maze_pass = [
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
  ]
  maze_not_pass = deepcopy(maze_pass)
  maze_not_pass[1][8] = 0
  entrance = [len(maze_pass) - 1, 0]
  exit = [0, len(maze_pass[0]) - 1]
  return (entrance, exit, maze_not_pass if not_pass else maze_pass)

def draw_maze(maze):
  for row in maze:
    print(row)

def show_result(maze, path):
  print('Can you pass the maze?', 'Yes' if path else 'No')
  print('The maze is:')
  draw_maze(maze)
  print('The path you find is:')
  print(path)
  print('\n\n')

def main():
  """
    The worst case time complexity is O(V + E) where V is the number of vertexes and E is the number of edges.
    The worst case means that after you traverse all points and then you find a path or a dead end.
  """
  (entrance, exit, maze) = get_input()
  path = get_maze_path(entrance, exit, deepcopy(maze))
  show_result(maze, path)

  (entrance, exit, maze) = get_input(True)
  path = get_maze_path(entrance, exit, deepcopy(maze))
  show_result(maze, path)

if __name__ == '__main__':
  main()
