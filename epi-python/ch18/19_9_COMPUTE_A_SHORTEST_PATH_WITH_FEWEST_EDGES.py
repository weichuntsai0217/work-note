from __future__ import print_function

class Node(object):
  def __init__(self, idx):
    self.idx = idx # int or str, use what you like
    self.edges = []

  def add_edge(self, node, weight):
    self.edges.append([node, weight])

def get_min_row(cost_table):
  flag = float('inf')
  target = None
  for key in cost_table:
    row = cost_table[key]
    if not row['visited'] and row['cost'][0] < flag:
      flag = row['cost'][0]
      target = row
  return target

def get_and_pop_src_node(min_row, unvisited):
  src_idx = None
  src_node = None
  for index, node in enumerate(unvisited):
    if node.idx == min_row['dst_idx']:
      src_idx = index
      src_node = node
      break
  unvisited.pop(src_idx)
  return src_node


def dijkstra(start, end, unvisited):
  cost_table = {}
  for node in unvisited:
    cost_table[node.idx] = {
      'dst_idx': node.idx,
      'cost': [0, 0] if node.idx == start.idx else [float('inf'), 0],
      'prev': None,
      'visited': False,
    }

  while unvisited:
    min_row = get_min_row(cost_table)
    if not min_row: break # means no path from start to end
    src_node = get_and_pop_src_node(min_row, unvisited)

    for edge in src_node.edges:
      node, weight = edge
      row = cost_table[node.idx]
      if not row['visited']:
        tmp_cost = min_row['cost'][0] + weight
        tmp_n_edges = min_row['cost'][1] + 1
        if (tmp_cost < row['cost'][0]) or (tmp_cost == row['cost'][0] and tmp_n_edges < row['cost'][1]):
          row['cost'][0] = tmp_cost
          row['cost'][1] = tmp_n_edges
          row['prev'] = min_row['dst_idx']
        
    min_row['visited'] = True
  return cost_table

def show_result(start, end, cost_table):
  print('The start node is', start.idx)
  print('The end node is', end.idx)
  keys = sorted(cost_table.keys())
  for key in keys:
    row = cost_table[key]
    print(row['dst_idx'], row['cost'], row['prev'])
  prev = cost_table[end.idx]['prev']
  path = [end.idx]
  while prev:
    path.insert(0, prev)
    prev = cost_table[prev]['prev']
  if len(path) > 1:
    print('The shorted path is:')
    print(' -> '.join(path))
  else:
    print('The shorted path does not exit.')
  print('\n')


def get_input(hard=False, not_valid=False):
  import random
  if hard:
    """
      Figure 19.1 page 350
    """
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_f = Node('f')
    node_g = Node('g')
    node_h = Node('h')
    node_i = Node('i')
    node_j = Node('j')
    node_k = Node('k')
    node_l = Node('l')
    node_a.add_edge(node_b, 3)
    node_a.add_edge(node_c, 2)
    node_b.add_edge(node_a, 4)
    node_b.add_edge(node_k, 1)
    node_c.add_edge(node_e, 8)
    node_d.add_edge(node_c, 5)
    node_e.add_edge(node_d, 7)
    node_f.add_edge(node_g, 6)
    node_g.add_edge(node_f, 7)
    node_i.add_edge(node_j, 6)
    node_j.add_edge(node_f, 1)
    node_j.add_edge(node_l, 7)
    node_k.add_edge(node_i, 1)
    node_l.add_edge(node_i, 9)
    if not not_valid:
      node_d.add_edge(node_h, 5)
      node_g.add_edge(node_h, 4)
    all_nodes = [
      node_a,
      node_b,
      node_c,
      node_d,
      node_e,
      node_f,
      node_g,
      node_h,
      node_i,
      node_j,
      node_k,
      node_l,
    ]
    random.shuffle(all_nodes)
    return node_a, node_h, all_nodes

  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  node_d = Node('d')
  node_a.add_edge(node_b, 1)
  node_a.add_edge(node_c, 3)
  if not not_valid:
    node_b.add_edge(node_d, 2)
    node_c.add_edge(node_d, 4)
  all_nodes = [node_a, node_b, node_c, node_d]
  random.shuffle(all_nodes)
  return node_a, node_d, all_nodes

def main():
  """
  """
  start, end, unvisited = get_input()
  cost_table = dijkstra(start, end, unvisited)
  show_result(start, end, cost_table)

  start, end, unvisited = get_input(True, False)
  cost_table = dijkstra(start, end, unvisited)
  show_result(start, end, cost_table)

  start, end, unvisited = get_input(False, True)
  cost_table = dijkstra(start, end, unvisited)
  show_result(start, end, cost_table)

  start, end, unvisited = get_input(True, True)
  cost_table = dijkstra(start, end, unvisited)
  show_result(start, end, cost_table)

if __name__ == '__main__':
  main()
