from __future__ import print_function

class Node(object):
  def __init__(self, name, edges=[]):
    self.name = name # only for test and validate
    self.color = 'w'
    # 'w' = 'white' means not vistied
    # 'g' = 'gray' means visited
    # 'b' = 'black' means its destination nodes are all visited (our graph is a directional graph.)
    self.edges = edges or [] # edges is a list of destination nodes

  def add_edge(self, node):
    if not node: return
    self.edges.append(node)


def dfs(node):
  # For dfs, if no cycle, all destination nodes would become 'black' befor their source.
  # if a desination node with gray is detected, that means the node points to the previous level and cause a deadlock.
  if node.color == 'g':
    return True
  node.color = 'g'
  for edge in node.edges:
    if edge.color != 'b':
      if dfs(edge):
        return True
  node.color = 'b'
  return False

def is_dead_lock(processes):
  for prc in processes:
    if prc.color == 'w' and dfs(prc):
      return True
  return False

def get_input(use_dead_lock=False, hard=False):
  import random
  nodes = []
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  node_d = Node('d')
  if use_dead_lock:
    print('Use deadlock data')
    if hard:
      print('in hard mode')
      node_e = Node('e')
      node_f = Node('f')
      node_g = Node('g')
      node_a.add_edge(node_b)
      node_a.add_edge(node_c)
      node_b.add_edge(node_c)
      node_c.add_edge(node_d)
      node_c.add_edge(node_g)
      node_d.add_edge(node_e)
      node_d.add_edge(node_f)
      node_f.add_edge(node_g)
      node_g.add_edge(node_b)
      nodes = [node_a, node_b, node_c, node_d, node_e, node_f, node_g]
    else:
      node_c.add_edge(node_d)
      node_d.add_edge(node_a)
      node_a.add_edge(node_b)
      node_a.add_edge(node_c)
      nodes = [node_a, node_b, node_c, node_d]
  else:
    print('Use no deadlock data')
    if hard:
      print('in hard mode')
      node_e = Node('e')
      node_f = Node('f')
      node_g = Node('g')
      node_a.add_edge(node_b)
      node_a.add_edge(node_c)
      node_b.add_edge(node_c)
      node_c.add_edge(node_d)
      node_c.add_edge(node_g)
      node_d.add_edge(node_e)
      node_d.add_edge(node_f)
      node_f.add_edge(node_g)
      nodes = [node_a, node_b, node_c, node_d, node_e, node_f, node_g]
    else:
      node_b.add_edge(node_d)
      node_c.add_edge(node_d)
      node_a.add_edge(node_b)
      node_a.add_edge(node_c)
      nodes = [node_a, node_b, node_c, node_d]
  random.shuffle(nodes)
  return nodes

def show_node_order(nodes):
  res = []
  for node in nodes:
    res.append(node.name)
  print('The process order is', res)

def main():
  """
    The worst case time complexity is O(V + E) where V is the number of vertexes and E is the number of edges.
  """
  processes = get_input(True, True)
  show_node_order(processes)
  print('Is dead lock?', 'Yes' if is_dead_lock(processes) else 'No')
  print('\n')

  processes = get_input(True, False)
  show_node_order(processes)
  print('Is dead lock?', 'Yes' if is_dead_lock(processes) else 'No')
  print('\n')

  processes = get_input(False, True)
  show_node_order(processes)
  print('Is dead lock?', 'Yes' if is_dead_lock(processes) else 'No')
  print('\n')

  processes = get_input(False, False)
  show_node_order(processes)
  print('Is dead lock?', 'Yes' if is_dead_lock(processes) else 'No')
  print('\n')


if __name__ == '__main__':
  main()
