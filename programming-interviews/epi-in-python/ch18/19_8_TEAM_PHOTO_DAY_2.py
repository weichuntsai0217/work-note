from __future__ import print_function

class Node(object):
  def __init__(self, idx, team):
    self.idx = idx # integer.
    self.team = sorted(team) # a list of ascending integers, ex: [2, 4, 7, 9, ...]
    self.edges = [] # a list of Node instances
    self.edge_map = {} # idx as key, to quickly check if some node is in my edge list.

  def add_edge(self, node):
    if isinstance(node, Node):
      self.edges.append(node)
      self.edge_map[node.idx] = True

  def is_back_of(self, node):
    """
      Our rule is that the front team height should be strictly less then the back team height (a < b).
    """
    team_back = self.team
    team_front = node.team
    length = len(team_back)
    for i in xrange(length):
      if team_front[i] >= team_back[i]:
        return False
    return True
    

def build_graph(teams):
  nodes = []
  for idx, team in enumerate(teams):
    nodes.append(Node(idx, team))
  
  length = len(nodes)

  for i in xrange(length):
    target = nodes[i]
    for j in xrange(length):
      tmp = nodes[j]
      if j != i and target.idx not in tmp.edge_map and target.is_back_of(tmp):
        target.add_edge(tmp)
        
  return nodes

def dfs(cur, history):
  history['cur_nodes'].append(cur)
  if not cur.edges:
    if len(history['cur_nodes']) > len(history['max_nodes']):
      history['max_nodes'] = [ node for node in history['cur_nodes'] ]
  for node in cur.edges: # if not cur.edges is True, this loop would not execute.
    dfs(node, history)
  history['cur_nodes'].pop(-1) # this step is important, do not forget to clean yourself before navigate to your siblings.
  return

def get_valid_teams(teams):
  nodes = build_graph(teams)
  history = {
    'cur_nodes': [],
    'max_nodes': [],
  }
  for node in nodes:
    dfs(node, history)
  return len(history['max_nodes'])

def get_input(not_all_valid=False, hard=False):
  def get_rdm(x):
    import random
    return sorted(x, key=lambda k: random.random())
  if not_all_valid:
    if hard:
      tmp = (
        get_rdm(range(6, 66, 6)),
        get_rdm(range(5, 55, 5)),
        get_rdm(range(4, 44, 4)),
        get_rdm(range(3, 33, 3)),
        get_rdm(range(2, 22, 2)),
        get_rdm(range(1, 21, 2)),
      )
      tmp[1][9] = 1
      tmp[3][9] = 1
      return tmp
    return (
      get_rdm([2, 4, 4, 8]),
      get_rdm([1, 3, 5, 7]),
    )
  else:
    if hard:
      return (
        get_rdm(range(6, 66, 6)),
        get_rdm(range(5, 55, 5)),
        get_rdm(range(4, 44, 4)),
        get_rdm(range(3, 33, 3)),
        get_rdm(range(2, 22, 2)),
        get_rdm(range(1, 21, 2)),
      )
    return (
      get_rdm(range(2, 10, 2)),
      get_rdm(range(1, 9, 2)),
    )

def main():
  print('1st')
  print(get_valid_teams(get_input()) == 2)
  print('2nd')
  print(get_valid_teams(get_input(False, True)) == 6)
  print('3rd')
  print(get_valid_teams(get_input(True)) == 1)
  print('4th')
  print(get_valid_teams(get_input(True, True)) == 4)

if __name__ == '__main__':
  main()
