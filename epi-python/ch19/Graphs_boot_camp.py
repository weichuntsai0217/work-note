from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

def build_graph(matches):
  """Check if the argument is a Class.
    matches:
      A list of matches, ex: [[teamA, teamB], [teamC, teamD]], [teamA, teamB] means teamA has beaten teamB
    Returns:
      A dict like:
      {
        'teamA': [teamB],
        'teamC': [teamD],
      }
      this dict is a graph implement by adjcent list
  """
  graph = {}
  for match in matches:
    key = match[0]
    val = match[1]
    if key not in graph:
      graph[key] = []
    graph[key].append(val)
  return graph

def dfs(graph, cur_team, dst_team, visited):
  if cur_team == dst_team: return True
  if cur_team in visited or cur_team not in graph: return False
  visited[cur_team] = True
  for team in graph[cur_team]:
    if dfs(graph, team, dst_team, visited):
      return True
  return False

def can_team_a_beat_team_b(matches, team_a, team_b):
  print('team_a = ', team_a)
  print('team_b = ', team_b)
  if team_a == team_b: return False # Edge case: team_a cannot beat itself
  graph = build_graph(matches)
  if team_a not in graph: return False # Edge case: team_a never wins
  visited = {}
  return dfs(graph, team_a, team_b, visited)



def main():
  matches = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'a'],
    ['e', 'd'],
    ['c', 'r'],
    ['r', 'c'],
  ]
  print(can_team_a_beat_team_b(matches, 'a', 'r'))
  print('\n')
  print(can_team_a_beat_team_b(matches, 'a', 'e'))
  print('\n')

if __name__ == '__main__':
  main()
