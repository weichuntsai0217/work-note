from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

from copy import deepcopy

def can_pass(entrance, exit, maze):
  if maze[entrance[0]][entrance[1]] == 0 or maze[exit[0]][exit[1]] == 0: return False
  return dfs(entrance, exit, maze)

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

def dfs(cur, exit, maze):
  if cur == exit: return True
  maze[cur[0]][cur[1]] = 0 # mark the cur point as 0 means this point is visited.
  reachable_neighbors = get_reachable_neighbors(cur, maze)
  if len(reachable_neighbors) == 0: return False
  for nbr in reachable_neighbors:
    if dfs(nbr, exit, maze):
      return True
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


def main():
  """
    The worst case time complexity is O(maze rows times maze cols),
    that is the path you find contains every point in the maze (your dfs traverse every point.)
  """
  (entrance, exit, maze) = get_input()
  print('Can you pass the maze?', can_pass(entrance, exit, maze))

  (entrance, exit, maze) = get_input(True)
  print('Can you pass the maze?', can_pass(entrance, exit, maze))

if __name__ == '__main__':
  main()
