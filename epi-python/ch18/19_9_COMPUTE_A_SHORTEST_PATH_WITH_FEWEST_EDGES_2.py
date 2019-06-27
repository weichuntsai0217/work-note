from __future__ import print_function
from heap import Heap

class Node(object):
  def __init__(self, idx):
    self.idx = idx
    self.edges = [] # [[node_1, weight_1], [node_2, weight_2]]
    self.prev = None # min path previous node
    self.min_dis = float('inf') # min_dis is minimum distance from some start node
    self.min_n_edges = 0

  def add_edge(self, node, weight):
    if isinstance(node, Node):
      self.edges.append([node, weight])

def comp(node_a, node_b):
  return node_a.min_dis > node_b.min_dis

def dijkstra(start, end, nodes):
  start.min_dis = 0 # from start node go to start node, the min distance is naturally 0.
  priority_queue = Heap([start], comp)
  while priority_queue.nodes:
    cur = priority_queue.pop_first_item()
    for (node, weight) in cur.edges:
      tmp_dis = cur.min_dis + weight
      tmp_n_edges = cur.min_n_edges + 1
      if (tmp_dis < node.min_dis) or (tmp_dis == node.min_dis and tmp_n_edges < node.min_n_edges):
        """
          the if condition above automatically prevent "go back and forth" problem between 2 adjacent nodes,
          thus we don't need a flag like "visited" to control it.
        """
        node.min_dis = tmp_dis
        node.min_n_edges = tmp_n_edges
        node.prev = cur
        priority_queue.insert(node)
 
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

def show_result(start, end, all_nodes):
  print('The start node is', start.idx)
  print('The end node is', end.idx)
  prev = end.prev
  path = [end.idx]
  while prev:
    path.insert(0, prev.idx)
    prev = prev.prev
  all_nodes = sorted(all_nodes, key=lambda x: x.idx)
  for node in all_nodes:
    print(node.idx, [node.min_dis, node.min_n_edges], node.prev.idx if node.prev else None)
  if len(path) > 1:
    print('The shorted path is:')
    print(' -> '.join(path))
  else:
    print('The shorted path does not exit.')
  print('\n')

def main():
  """
    The worst case time complexity is O( (E + V)logV ) because we use priority queue (implemented by heap) for Dijkstra's shorted path algorithm.
  """

  start, end, nodes = get_input()
  dijkstra(start, end, nodes)
  show_result(start, end, nodes)

  start, end, nodes = get_input(True, False)
  dijkstra(start, end, nodes)
  show_result(start, end, nodes)

  start, end, nodes = get_input(False, True)
  dijkstra(start, end, nodes)
  show_result(start, end, nodes)

  start, end, nodes = get_input(True, True)
  dijkstra(start, end, nodes)
  show_result(start, end, nodes)

if __name__ == '__main__':
  main()
