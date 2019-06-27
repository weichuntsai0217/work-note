from __future__ import print_function

class Node(object):
  def __init__(self, name, label, edges=None):
    """
      In constructor, please do NOT use mutable objects (ex: list or dict) as default value.
      This would cause "reference to the same object" problem.
      For more information,
      please refer to https://stackoverflow.com/questions/48899803/object-reference-issue-in-python-while-creating-a-tree
    """
    self.name = name # just for debug
    self.label = label
    self.edges = edges or []

  def add_edge(self, node):
    if not isinstance(node, Node): return
    self.edges.append(node)

def clone_graph(start_node):
  copied_start_node = Node(start_node.name, start_node.label)
  bfs(start_node, copied_start_node)
  return copied_start_node

def bfs(src, res):
  visited = {}
  visited[id(src)] = res
  queue = [src]
  while queue:
    # show_queue(queue)
    cur = queue[0]
    copied_cur = visited[id(cur)]
    for edge in cur.edges:
      if id(edge) in visited:
        copied_cur.add_edge(visited[id(edge)])
      else:
        tmp = Node(edge.name, edge.label)
        copied_cur.add_edge(tmp)
        visited[id(edge)] = tmp
        queue.append(edge)
    
    queue.pop(0)
  return res

def show_queue(q):
  tmp = map(lambda x: x.name, q)
  print(' -> '.join(tmp))

def get_input(use_dead_lock=False, hard=False, use_shuffle=False):
  import random
  nodes = []
  node_a = Node('a', 10)
  node_b = Node('b', 20)
  node_c = Node('c', 30)
  node_d = Node('d', 40)
  node_e = Node('e', 50)
  node_f = Node('f', 60)
  node_g = Node('g', 70)
  if use_dead_lock:
    print('Use deadlock data')
    if hard:
      print('in hard mode')
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
  if use_shuffle:
    random.shuffle(nodes)
  return nodes[0]

def show_simple_node(node):
  print('Level 0 ===')
  print('node.name =', node.name)
  print('node.label =', node.label)
  print('len(node.edges) =', len(node.edges))
  node0 = node.edges[0]
  node1 = node.edges[1]
  print('Level 1 - index 0 ===')
  print('node0.name =', node0.name)
  print('node0.label =', node0.label)
  print('len(node0.edges) =', len(node0.edges))
  print('Level 1 - index 1 ===')
  print('node1.name =', node1.name)
  print('node1.label =', node1.label)
  print('len(node1.edges) =', len(node1.edges))
  node00 = node0.edges[0]
  node10 = node1.edges[0]
  print('Level 2 - index 0 ===')
  print('node00.name =', node00.name)
  print('node00.label =', node00.label)
  print('len(node00.edges) =', len(node00.edges))
  print('node10.name =', node10.name)
  print('node10.label =', node10.label)
  print('len(node10.edges) =', len(node10.edges))
  print('\n')


def main():
  start_node = get_input(True, True)
  res = clone_graph(start_node)
# show_simple_node(start_node)
# show_simple_node(res)

  print('Check if every thing is deepcopied.')
  start_node.label = -10
  print(start_node.label)
  print(res.label)

  start_node.edges[0].edges[0].edges[0].label = -40
  print(start_node.edges[0].edges[0].edges[0].label)
  print(res.edges[0].edges[0].edges[0].label)

  

if __name__ == '__main__':
  main()
