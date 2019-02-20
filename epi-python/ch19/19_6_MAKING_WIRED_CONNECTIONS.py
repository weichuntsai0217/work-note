from __future__ import print_function

class Node(object):
  def __init__(self, name, edges=None):
    self.name = name # for debug
    self.distance = -1 # -1 means not visited.
    self.edges = edges or []

  def add_edge(self, node):
    if isinstance(node, Node):
      self.edges.append(node)

  def set_distance(self, distance):
    if isinstance(distance, int):
      self.distance = distance

def is_valid_wire_connection_for_pcb(nodes): # nodes here roughly means all nodes on pcb board.
  for start_node in nodes:
    if isinstance(start_node, Node) and start_node.distance == -1:
      start_node.set_distance(0)
      if not bfs(start_node):
        return False
  return True

def bfs(start_node):
  queue = [start_node]
  while queue:
    cur = queue.pop(0)
    for edge in cur.edges:
      if edge.distance == -1:
        edge.set_distance(cur.distance + 1)
        queue.append(edge)
      elif edge.distance == cur.distance:
        return False
  return True
 
def get_input(use_invalid=False, hard=False, use_shuffle=False):
  import random
  nodes = []
  if hard:
    print('in hard mode, use the data like Figure 19.8 in page 364')
    for i in xrange(22):
      nodes.append(Node(str(i)))
    if use_invalid:
      nodes[0].add_edge(nodes[10])
      nodes[10].add_edge(nodes[0])
    nodes[0].add_edge(nodes[1])
    nodes[0].add_edge(nodes[9])
    nodes[1].add_edge(nodes[2])
    nodes[1].add_edge(nodes[10])
    nodes[1].add_edge(nodes[0])
    nodes[2].add_edge(nodes[3])
    nodes[2].add_edge(nodes[11])
    nodes[2].add_edge(nodes[1])
    nodes[3].add_edge(nodes[4])
    nodes[3].add_edge(nodes[12])
    nodes[3].add_edge(nodes[2])
    nodes[4].add_edge(nodes[5])
    nodes[4].add_edge(nodes[3])
    nodes[5].add_edge(nodes[6])
    nodes[5].add_edge(nodes[13])
    nodes[5].add_edge(nodes[12])
    nodes[5].add_edge(nodes[4])
    nodes[6].add_edge(nodes[7])
    nodes[6].add_edge(nodes[5])
    nodes[7].add_edge(nodes[8])
    nodes[7].add_edge(nodes[13])
    nodes[7].add_edge(nodes[6])
    nodes[8].add_edge(nodes[21])
    nodes[8].add_edge(nodes[7])
    nodes[9].add_edge(nodes[0])
    nodes[9].add_edge(nodes[10])
    nodes[9].add_edge(nodes[14])
    nodes[10].add_edge(nodes[1])
    nodes[10].add_edge(nodes[11])
    nodes[10].add_edge(nodes[15])
    nodes[10].add_edge(nodes[9])
    nodes[11].add_edge(nodes[2])
    nodes[11].add_edge(nodes[12])
    nodes[11].add_edge(nodes[16])
    nodes[11].add_edge(nodes[10])
    nodes[12].add_edge(nodes[3])
    nodes[12].add_edge(nodes[5])
    nodes[12].add_edge(nodes[17])
    nodes[12].add_edge(nodes[11])
    nodes[13].add_edge(nodes[5])
    nodes[13].add_edge(nodes[7])
    nodes[13].add_edge(nodes[21])
    nodes[13].add_edge(nodes[19])
    nodes[14].add_edge(nodes[9])
    nodes[14].add_edge(nodes[15])
    nodes[15].add_edge(nodes[10])
    nodes[15].add_edge(nodes[16])
    nodes[15].add_edge(nodes[14])
    nodes[16].add_edge(nodes[11])
    nodes[16].add_edge(nodes[17])
    nodes[16].add_edge(nodes[15])
    nodes[17].add_edge(nodes[12])
    nodes[17].add_edge(nodes[18])
    nodes[17].add_edge(nodes[16])
    nodes[18].add_edge(nodes[19])
    nodes[18].add_edge(nodes[17])
    nodes[19].add_edge(nodes[13])
    nodes[19].add_edge(nodes[20])
    nodes[19].add_edge(nodes[18])
    nodes[20].add_edge(nodes[21])
    nodes[20].add_edge(nodes[19])
    nodes[21].add_edge(nodes[13])
    nodes[21].add_edge(nodes[8])
    nodes[21].add_edge(nodes[20])
  else:
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')

    node_a.add_edge(node_b)
    node_a.add_edge(node_c)

    node_b.add_edge(node_a)
    node_b.add_edge(node_d)

    node_c.add_edge(node_a)
    node_c.add_edge(node_d)

    node_d.add_edge(node_b)
    node_d.add_edge(node_c)
    if use_invalid:
      node_b.add_edge(node_c)
      node_c.add_edge(node_b)
    nodes = [node_a, node_b, node_c, node_d]
  if use_shuffle:
    random.shuffle(nodes)
  print('The 1st node is', nodes[0].name)
  return nodes

def main():
  """
    The worst case time complexity is O(V + E) where V is the number of vertexes and E is the number of edges.
  """
  print('Should print \'Yes\'')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, True, True)) else 'No')

  print('\n')

  print('Should print \'No\'')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, True, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, True, True)) else 'No')

  print('\n')

  print('Should print \'Yes\'')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(False, False, True)) else 'No')

  print('\n')

  print('Should print \'No\'')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, False, True)) else 'No')
  print('Yes' if is_valid_wire_connection_for_pcb(get_input(True, False, True)) else 'No')
if __name__ == '__main__':
  main()
