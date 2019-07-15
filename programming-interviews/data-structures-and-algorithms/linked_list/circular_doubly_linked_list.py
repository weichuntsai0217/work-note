"""
  Use python 3.6.8
"""
"""
  # What is a linked list?
  A linked list is a data structure in which the objects are arranged in a linear order and
  the order is determined by pointers in each object.

  # What is a cicular doubly-linked list?
  A circular doubly-linked list is a doubly-linked list in which the tail node is connected to the head node.
  This design can simplify the edge case handling when we do insertion and deletion.

  # How to implement a cicular doubly-linked list?
  You can consider make a circular doubly-linked list support methods as follows by different cases:
  (assume `n` is the length of the linked list)
  * case (a) If the circular doubly-linked list has `snt`; each node has `data`, `nxt`, and `prv`:
    1. `search` with O(n) time complexity and it means "search by key".
    2. `insert` with O(1) time complexity and it means "insert a given node before head".
    3. `delete` with O(1) time complexity and it means "delete the given node".
    4. `insert_after` with O(1) time complexity and it means "insert a given node after another given node".
    5. `delete_after` with O(1) time complexity and it means "delete a given node after another given node".
    6. `insert_by_data` with O(1) time complexity and it means "insert a node from a given data"
    7. `delete_by_key` with O(n) time complexity and it means "delete the 1st node whose data is equal to key."
    8. `append` with O(1) time complexity and it means "add a new node after tail".
  * case (b) Based on (a), if the circular doubly-linked list has additional `length`, then
    we can implement the above 1 ~ 8 plus the following 9, 10, 11:
    9. `search_by_idx` with O(n) time complexity.
    10. `insert_by_idx` with O(n) time complexity.
    11.`delete_by_idx` with O(n) time complexity.

  # References
  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).

  # Notes
  There are some details for the following implement code:
  * For people who are not familiar with douly-linked list, the most important in implementation is
  "Don't forget to update the `prv` pointer."

  * If we only need `snt` and don't need `length` and only want to use functions as operations
  then we can choose that we don't wrap `head` in an instance of `LinkedList` (like in `use_funcs_1`)
  and the `head` node itself represents the whole linked list
  because the code would be cleaner for more most interview questions.
  (If you prefer to wrap it, it is OK to do so.)
  However if we also need `length`, then we usually wrap `snt` and `length`
  into an instance of `LinkedList` to keep updating status consistently.

  * It is impossible to implement every scenario, in this file we just list 
  some common scenarios in classical text book, and if you are familiar with these scenarios,
  other challenges or vairiants would not beat you down.

  * For more information, please refer to comments in the top of "singly_linked_list.py".
"""

# Utils for test - start
def get_str_from_snt_node(snt):
  node = snt.nxt
  from_p_to_c = ' => '
  from_c_to_p = ' <= '
  res_p_to_c = []
  res_c_to_p = []
  while node != snt:
    res_p_to_c.append(str(node.data))
    node = node.nxt
  node = snt.prv
  while node != snt:
    res_c_to_p.insert(0, str(node.data))
    node = node.prv
  return (get_str_from_list(res_p_to_c, from_p_to_c), get_str_from_list(res_c_to_p, from_c_to_p))

def get_str_from_list(src, token):
  return '[' + token.join(map(lambda x: str(x), src)) + ']'

def get_data(nodes):
  return list(map(lambda x: x.data, nodes))

def get_strs(src, token_0=' => ', token_1=' <= '):
  return (get_str_from_list(src, token_0), get_str_from_list(src, token_1))
# Utils for test - end

def use_class_1():
  """
    Implement a circular doubly-linked list by a class with a `snt` attribute.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    @staticmethod
    def init_new_snt():
      snt = LinkedList.Node() # snt is sentinel node.
      snt.nxt = snt # snt.nxt is head. The default value is snt itself.
      snt.prv = snt # snt.prv is tail. The default value is snt itself.
      return snt

    @staticmethod
    def insert_after(node, new_node):
      new_node.nxt = node.nxt
      node.nxt.prv = new_node
      node.nxt = new_node
      new_node.prv = node

    @staticmethod
    def delete_after(linked_list, node):
      """
        `delete_after` still need to check if the node is tail.
        If node is `tail`, then you would delete `snt` node.
        So when tail is detected, we do nothing.
      """
      if node != linked_list.snt.prv:
        node.nxt = node.nxt.nxt
        node.nxt.prv = node

    def __init__(self):
      self.snt = LinkedList.init_new_snt()

    def search(self, key):
      x = self.snt.nxt
      while (x != self.snt) and (x.data != key):
        x = x.nxt
      return x if x != self.snt else None # None means 'find nothing'

    def insert(self, x):
      x.nxt = self.snt.nxt
      self.snt.nxt.prv = x
      self.snt.nxt = x
      x.prv = self.snt

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do the following edge case handling:
        1. the linked list is empty, that is `self.snt.nxt` is itself.
        2. the node we want to delete is `self.snt`, this is not allowed.
        We expect users don't input x from another linked list.
      """
      if self.snt.nxt != self.snt and x != self.snt:
        x.prv.nxt = x.nxt
        x.nxt.prv = x.prv
        return True # delete successful.
      return False # delete failed.

    def insert_by_data(self, data):
      new_node = LinkedList.Node(data)
      self.insert(new_node)

    def delete_by_key(self, key):
      x = self.search(key)
      if x:
        return self.delete(x)
      return False

    def append(self, x):
      self.snt.prv.nxt = x
      x.prv = self.snt.prv
      x.nxt = self.snt
      self.snt.prv = x
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is a 'circular doubly-linked list'.
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  
  dlt.insert(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  
  res = dlt.search(0)
  assert res == node_0
  
  res = dlt.search(1)
  assert res == None
  
  dlt.delete(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  
  for node in reversed(nodes):
    dlt.insert(node)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data(nodes))
  
  res = dlt.search(2)
  assert res == node_2

  res = dlt.search(3)
  assert res == node_3

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(dlt, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1]))

  LinkedList.insert_after(node_1, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
    
  LinkedList.insert_after(node_1, node_2)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt.delete(node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))

  dlt.delete(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))

  dlt.insert_by_data(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_1, node_2, node_3]))

  dlt.insert_by_data(0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt.delete_by_key(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))

  dlt.delete_by_key(0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))

  dlt.append(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3, node_0]))
  assert dlt.snt.nxt == node_2
  assert dlt.snt.prv == node_0

  print('use_class_1 success')
  # Test end

def use_funcs_1():
  """
    Implement a doubly-linked list by a `snt` node and other functions.
  """
  # Implement start
  class Node(object):
    def __init__(self, data=None, nxt=None, prv=None):
      self.data = data
      self.nxt = nxt
      self.prv = prv

  def insert_after(node, new_node):
    new_node.nxt = node.nxt
    node.nxt.prv = new_node
    node.nxt = new_node
    new_node.prv = node

  def delete_after(snt, node):
    """
      `delete_after` still need to check if the node is tail.
      If node is `tail`, then you would delete `snt` node.
      So when tail is detected, we do nothing.
    """
    if node != snt.prv:
      node.nxt = node.nxt.nxt
      node.nxt.prv = node

  def init_new_snt():
    snt = Node() # snt is sentinel node.
    snt.nxt = snt # snt.nxt is head. The default value is snt itself.
    snt.prv = snt # snt.prv is tail. The default value is snt itself.
    return snt

  def search(snt, key):
    x = snt.nxt
    while (x != snt) and (x.data != key):
      x = x.nxt
    return x if x != snt else None # None means 'find nothing'

  def insert(snt, x):
    x.nxt = snt.nxt
    snt.nxt.prv = x
    snt.nxt = x
    x.prv = snt

  def delete(snt, x):
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though users input valid arguments,
      we still need to do the following edge case handling:
      1. the linked list is empty, that is `snt.nxt` is itself.
      2. the node we want to delete is `snt`, this is not allowed.
      We expect users don't input x from another linked list.
    """
    if snt.nxt != snt and x != snt:
      x.prv.nxt = x.nxt
      x.nxt.prv = x.prv
      return True # delete successful.
    return False # delete failed.
    

  def insert_by_data(snt, data):
    new_node = Node(data)
    insert(snt, new_node)

  def delete_by_key(snt, key):
    x = search(snt, key)
    if x:
      return delete(snt, x)
    return False

  def append(snt, x):
    snt.prv.nxt = x
    x.prv = snt.prv
    x.nxt = snt
    snt.prv = x
  # Implement end

  # Test start
  dlt = init_new_snt() # dlt is a 'circular doubly-linked list'., now represented by a `snt` node
  node_0 = Node(0)
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_snt_node(dlt) == get_strs([])
  
  insert(dlt, node_0)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0]))
  
  res = search(dlt, 0)
  assert res == node_0
  
  res = search(dlt, 1)
  assert res == None
  
  delete(dlt, node_0)
  assert get_str_from_snt_node(dlt) == get_strs([])
  
  for node in reversed(nodes):
    insert(dlt, node)
  assert get_str_from_snt_node(dlt) == get_strs(get_data(nodes))
  
  res = search(dlt, 2)
  assert res == node_2

  res = search(dlt, 3)
  assert res == node_3

  delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))

  delete_after(dlt, node_3)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))

  delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1]))

  insert_after(node_1, node_3)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))
    
  insert_after(node_1, node_2)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  delete(dlt, node_1)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_2, node_3]))

  delete(dlt, node_0)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_2, node_3]))

  insert_by_data(dlt, 1)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_1, node_2, node_3]))

  insert_by_data(dlt, 0)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  delete_by_key(dlt, 1)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_0, node_2, node_3]))

  delete_by_key(dlt, 0)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_2, node_3]))

  append(dlt, node_0)
  assert get_str_from_snt_node(dlt) == get_strs(get_data([node_2, node_3, node_0]))
  assert dlt.nxt == node_2
  assert dlt.prv == node_0

  print('use_funcs_1 success')
  # Test end

def use_class_2():
  """
    Implement a doubly-linked list by a class with `head`, `tail` and `length` attributes.
    This implement is case (b).
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    @staticmethod
    def init_new_snt():
      snt = LinkedList.Node() # snt is sentinel node.
      snt.nxt = snt # snt.nxt is head. The default value is snt itself.
      snt.prv = snt # snt.prv is tail. The default value is snt itself.
      return snt

    @staticmethod
    def insert_after(linked_list, node, new_node):
      new_node.nxt = node.nxt
      node.nxt.prv = new_node
      node.nxt = new_node
      new_node.prv = node
      linked_list.inc_len()

    @staticmethod
    def delete_after(linked_list, node):
      """
        `delete_after` still need to check if the node is tail.
        If node is `tail`, then you would delete `snt` node.
        So when tail is detected, we do nothing.
      """
      if node != linked_list.snt.prv:
        node.nxt = node.nxt.nxt
        node.nxt.prv = node
        linked_list.dec_len()

    def __init__(self):
      self.snt = LinkedList.init_new_snt()
      self.length = 0

    def search(self, key):
      x = self.snt.nxt
      while (x != self.snt) and (x.data != key):
        x = x.nxt
      return x if x != self.snt else None # None means 'find nothing'

    def insert(self, x):
      x.nxt = self.snt.nxt
      self.snt.nxt.prv = x
      self.snt.nxt = x
      x.prv = self.snt
      self.inc_len()

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do the following edge case handling:
        1. the linked list is empty, that is `self.snt.nxt` is itself.
        2. the node we want to delete is `self.snt`, this is not allowed.
        We expect users don't input x from another linked list.
      """
      if self.snt.nxt != self.snt and x != self.snt:
        x.prv.nxt = x.nxt
        x.nxt.prv = x.prv
        self.dec_len()
        return True # delete successful.
      return False # delete failed.

    def insert_by_data(self, data):
      new_node = LinkedList.Node(data)
      self.insert(new_node)

    def delete_by_key(self, key):
      x = self.search(key)
      if x:
        return self.delete(x)
      return False

    def append(self, x):
      self.snt.prv.nxt = x
      x.prv = self.snt.prv
      x.nxt = self.snt
      self.snt.prv = x
      self.inc_len()

    def get_len(self):
      return self.length

    def inc_len(self):
      self.length += 1

    def dec_len(self):
      self.length -= 1

    def search_by_idx(self, idx):
      """
        We use array index tradition, that is index 0 means the 1st element.
      """
      if idx >= self.get_len() or idx < 0:
        raise IndexError(
          'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
          .format(self.get_len() - 1, idx)
        )
      i = 0
      x = self.snt.nxt
      while i < idx:
        x = x.nxt
        i += 1
      return x

    def insert_by_idx(self, idx, x):
      """
        When self.get_len() = 0 and idx = 0, this means prepend a node to the empty linked list.
        When self.get_len() = 3 and idx = 3, this means append a node to the linked list.
        So max idx could be self.get_len() instead of self.get_len() - 1.
      """
      if idx > self.get_len() or idx < 0:
        raise IndexError(
          'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
          .format(self.get_len(), idx)
        )
      if idx == 0:
        self.insert(x)
      else:
        prv = self.search_by_idx(idx - 1)
        LinkedList.insert_after(self, prv, x)       

    def delete_by_idx(self, idx):
      if idx >= self.get_len() or idx < 0:
        raise IndexError(
          'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
          .format(self.get_len() - 1, idx)
        )
      if idx == 0:
        self.delete(self.snt.nxt)
      else:
        prv = self.search_by_idx(idx - 1)
        LinkedList.delete_after(self, prv)
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is a 'circular doubly-linked list'.
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert dlt.get_len() == 0
 
  dlt.insert(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == dlt.snt.prv
  assert dlt.get_len() == 1
  
  res = dlt.search(0)
  assert res == node_0
  
  res = dlt.search(1)
  assert res == None
  
  dlt.delete(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert dlt.get_len() == 0
  
  for node in reversed(nodes):
    dlt.insert(node)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data(nodes))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 4
  
  res = dlt.search(2)
  assert res == node_2

  res = dlt.search(3)
  assert res == node_3

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  LinkedList.delete_after(dlt, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_1
  assert dlt.get_len() == 2

  LinkedList.insert_after(dlt, node_1, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3
    
  LinkedList.insert_after(dlt, node_1, node_2)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 4

  dlt.delete(node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  dlt.delete(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))
  assert dlt.snt.nxt == node_2
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 2

  dlt.insert_by_data(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_1, node_2, node_3]))
  assert dlt.snt.nxt.data == node_1.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  dlt.insert_by_data(0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.snt.nxt.data == node_0.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 4

  dlt.delete_by_key(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt.data == node_0.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  dlt.delete_by_key(0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))
  assert dlt.snt.nxt == node_2
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 2

  dlt.insert(node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 3

  res = dlt.search_by_idx(0)
  assert res == node_0

  res = dlt.search_by_idx(1)
  assert res == node_2

  res = dlt.search_by_idx(2)
  assert res == node_3

  dlt.delete_by_idx(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 2

  dlt.delete_by_idx(1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_0
  assert dlt.get_len() == 1

  dlt.delete_by_idx(0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([]))
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert dlt.get_len() == 0

  dlt.insert_by_idx(0, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_0
  assert dlt.get_len() == 1

  dlt.insert_by_idx(1, node_2)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_2
  assert dlt.get_len() == 2

  dlt.insert_by_idx(1, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_2
  assert dlt.get_len() == 3

  dlt.append(node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data(nodes))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert dlt.get_len() == 4

  print('use_class_2 success')
  # Test end

def use_funcs_2():
  """
    Implement a doubly-linked list by a class with `head`, `tail` and `length` attributes, and other functions.
    This implement is case (b).
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    @staticmethod
    def init_new_snt():
      snt = LinkedList.Node() # snt is sentinel node.
      snt.nxt = snt # snt.nxt is head. The default value is snt itself.
      snt.prv = snt # snt.prv is tail. The default value is snt itself.
      return snt

    def __init__(self):
      self.snt = LinkedList.init_new_snt()
      self.length = 0

  def insert_after(linked_list, node, new_node):
    new_node.nxt = node.nxt
    node.nxt.prv = new_node
    node.nxt = new_node
    new_node.prv = node
    inc_len(linked_list)

  def delete_after(linked_list, node):
    """
      `delete_after` still need to check if the node is tail.
      If node is `tail`, then you would delete `snt` node.
      So when tail is detected, we do nothing.
    """
    if node != linked_list.snt.prv:
      node.nxt = node.nxt.nxt
      node.nxt.prv = node
      dec_len(linked_list)

  def search(linked_list, key):
    x = linked_list.snt.nxt
    while (x != linked_list.snt) and (x.data != key):
      x = x.nxt
    return x if x != linked_list.snt else None # None means 'find nothing'

  def insert(linked_list, x):
    x.nxt = linked_list.snt.nxt
    linked_list.snt.nxt.prv = x
    linked_list.snt.nxt = x
    x.prv = linked_list.snt
    inc_len(linked_list)

  def delete(linked_list, x):
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though users input valid arguments,
      we still need to do the following edge case handling:
      1. the linked list is empty, that is `linked_list.snt.nxt` is itself.
      2. the node we want to delete is `linked_list.snt`, this is not allowed.
      We expect users don't input x from another linked list.
    """
    if linked_list.snt.nxt != linked_list.snt and x != linked_list.snt:
      x.prv.nxt = x.nxt
      x.nxt.prv = x.prv
      dec_len(linked_list)
      return True # delete successful.
    return False # delete failed.

  def insert_by_data(linked_list, data):
    new_node = LinkedList.Node(data)
    insert(linked_list, new_node)

  def delete_by_key(linked_list, key):
    x = search(linked_list, key)
    if x:
      return delete(linked_list, x)
    return False

  def append(linked_list, x):
    linked_list.snt.prv.nxt = x
    x.prv = linked_list.snt.prv
    x.nxt = linked_list.snt
    linked_list.snt.prv = x
    inc_len(linked_list)

  def get_len(linked_list):
    return linked_list.length

  def inc_len(linked_list):
    linked_list.length += 1

  def dec_len(linked_list):
    linked_list.length -= 1

  def search_by_idx(linked_list, idx):
    """
      We use array index tradition, that is index 0 means the 1st element.
    """
    if idx >= get_len(linked_list) or idx < 0:
      raise IndexError(
        'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
        .format(get_len(linked_list) - 1, idx)
      )
    i = 0
    x = linked_list.snt.nxt
    while i < idx:
      x = x.nxt
      i += 1
    return x

  def insert_by_idx(linked_list, idx, x):
    """
      When get_len(linked_list) = 0 and idx = 0, this means prepend a node to the empty linked list.
      When get_len(linked_list) = 3 and idx = 3, this means append a node to the linked list.
      So max idx could be get_len(linked_list) instead of get_len(linked_list) - 1.
    """
    if idx > get_len(linked_list) or idx < 0:
      raise IndexError(
        'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
        .format(get_len(linked_list), idx)
      )
    if idx == 0:
      insert(linked_list, x)
    else:
      prv = search_by_idx(linked_list, idx - 1)
      insert_after(linked_list, prv, x)       

  def delete_by_idx(linked_list, idx):
    if idx >= get_len(linked_list) or idx < 0:
      raise IndexError(
        'The idx is out of range. The max idx is {} and the min idx is 0, but your input is {}'
        .format(get_len(linked_list) - 1, idx)
      )
    if idx == 0:
      delete(linked_list, linked_list.snt.nxt)
    else:
      prv = search_by_idx(linked_list, idx - 1)
      delete_after(linked_list, prv)
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is a 'circular doubly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert get_len(dlt) == 0
 
  insert(dlt, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == dlt.snt.prv
  assert get_len(dlt) == 1
  
  res = search(dlt, 0)
  assert res == node_0
  
  res = search(dlt, 1)
  assert res == None
  
  delete(dlt, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs([])
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert get_len(dlt) == 0
  
  for node in reversed(nodes):
    insert(dlt, node)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data(nodes))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 4
  
  res = search(dlt, 2)
  assert res == node_2

  res = search(dlt, 3)
  assert res == node_3

  delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  delete_after(dlt, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  delete_after(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_1
  assert get_len(dlt) == 2

  insert_after(dlt, node_1, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3
    
  insert_after(dlt, node_1, node_2)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 4

  delete(dlt, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  delete(dlt, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))
  assert dlt.snt.nxt == node_2
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 2

  insert_by_data(dlt, 1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_1, node_2, node_3]))
  assert dlt.snt.nxt.data == node_1.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  insert_by_data(dlt, 0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.snt.nxt.data == node_0.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 4

  delete_by_key(dlt, 1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt.data == node_0.data # check data here because dlt.snt is another Node instance
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  delete_by_key(dlt, 0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_2, node_3]))
  assert dlt.snt.nxt == node_2
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 2

  insert(dlt, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 3

  res = search_by_idx(dlt, 0)
  assert res == node_0

  res = search_by_idx(dlt, 1)
  assert res == node_2

  res = search_by_idx(dlt, 2)
  assert res == node_3

  delete_by_idx(dlt, 1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_3]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 2

  delete_by_idx(dlt, 1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_0
  assert get_len(dlt) == 1

  delete_by_idx(dlt, 0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([]))
  assert dlt.snt.nxt == dlt.snt
  assert dlt.snt.prv == dlt.snt
  assert get_len(dlt) == 0

  insert_by_idx(dlt, 0, node_0)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_0
  assert get_len(dlt) == 1

  insert_by_idx(dlt, 1, node_2)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_2]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_2
  assert get_len(dlt) == 2

  insert_by_idx(dlt, 1, node_1)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data([node_0, node_1, node_2]))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_2
  assert get_len(dlt) == 3

  append(dlt, node_3)
  assert get_str_from_snt_node(dlt.snt) == get_strs(get_data(nodes))
  assert dlt.snt.nxt == node_0
  assert dlt.snt.prv == node_3
  assert get_len(dlt) == 4

  print('use_funcs_2 success')
  # Test end

def main():
  use_class_1()
  use_funcs_1()
  use_class_2()
  use_funcs_2()

if __name__ == '__main__':
  main()

