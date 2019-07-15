"""
  Use python 3.6.8
"""
"""
  What is a linked list?
  A linked list is a data structure in which the objects are arranged in a linear order and
  the order is determined by pointers in each object.

  What is a doubly-linked list?
  A doubly-linked list is a linked list in which each object has two pointers `next` and `prev` which points to its successor and predecessor, repectively.

  How to implement a doubly-linked list?
  You can consider make a doubly-linked list support methods as follows by different cases:
  (assume `n` is the length of the linked list)
  * case (a) If the doubly-linked list has `head`; each node has `data` and `nxt`:
    1. `search` with O(n) time complexity and it means "search by key".
    2. `insert` with O(1) time complexity and it means "insert a given node before head".
    3. `delete` with O(1) time complexity and it means "delete the given node".
    4. `insert_after` with O(1) time complexity and it means "insert a given node after another given node".
    5. `delete_after` with O(1) time complexity and it means "delete a given node after another given node".
    6. `insert_by_data` with O(1) time complexity and it means "insert a node from a given data"
    7. `delete_by_key` with O(n) time complexity and it means "delete the 1st node whose data is equal to key."
  * case (b) Based on (a), if the doubly-linked list has additional `length`, then
    we can implement the above 1 ~ 7 plus the following 8, 9, 10:
    8. `search_by_idx` with O(n) time complexity.
    9. `insert_by_idx` with O(n) time complexity.
    10.`delete_by_idx` with O(n) time complexity.
  * case (c) Based on (a), if the doubly-linked list has additional `tail`, then
    we can implement the above 1 ~ 7 plus the following 11:
    11. `append` with O(1) time complexity and it means "add a new node after tail".

  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).

  There are some details for the following implement code:
    For people who are not familiar with douly-linked list, the most important in implementation is
    "Don't forget to update the `prv` pointer."

    If we only need `head` and don't need `tail` and `length` and only want to use functions as operations
    then we can choose that we don't wrap `head` in an instance of `LinkedList` (like in `use_funcs_1`)
    and the `head` node itself represents the whole linked list
    because the code would be cleaner for more most interview questions.
    (If you prefer to wrap it, it is OK to do so.)
    However if we also need `tail` and `length`, then we usually wrap `head`, `tail` and `length`
    into an instance of `LinkedList` to keep updating status consistently.

    It is impossible to implement every scenario, in this file we just list 
    some common scenarios in classical text book, and if you are familiar with these scenarios,
    other challenges or vairiants would not beat you down.

    For more information, please refer to comments in the top of "singly_linked_list.py".
"""

# Utils for test - start
def get_str_from_head_node(head, tail=None):
  node = head
  from_p_to_c = ' => '
  from_c_to_p = ' <= '
  res_p_to_c = []
  res_c_to_p = []
  if tail:
    while node:
      res_p_to_c.append(str(node.data))
      node = node.nxt
  else:
    while node:
      tail = node
      res_p_to_c.append(str(node.data))
      node = node.nxt
  node = tail
  while node:
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
    Implement a doubly-linked list by a class with a `head` attribute.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    @staticmethod
    def insert_after(node, new_node):
      new_node.nxt = node.nxt
      if node.nxt:
        node.nxt.prv = new_node
      node.nxt = new_node
      new_node.prv = node

    @staticmethod
    def delete_after(node):
      if node.nxt:
        node.nxt = node.nxt.nxt
        if node.nxt: # the updated node.nxt could be None, we must use `if` to check.
          node.nxt.prv = node

    def __init__(self):
      self.head = None

    def search(self, key):
      x = self.head
      while x and (x.data != key):
        x = x.nxt
      return x # if x is None, it means 'find nothing'

    def insert(self, x):
      x.nxt = self.head
      if self.head:
        self.head.prv = x
      self.head = x
      x.prv = None

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do some edge case handling:
        1. the linked list is empty, that is `self.head` is `None`
        2. the node we want to delete is just the `self.head`
      """
      if not self.head:
        return False # return False means 'delete failed.'
      if x.prv is None: # x is head
        self.head = x.nxt
      else:
        x.prv.nxt = x.nxt
      if x.nxt:
        x.nxt.prv = x.prv
      return True

    def insert_by_data(self, data):
      new_node = LinkedList.Node(data)
      self.insert(new_node)

    def delete_by_key(self, key):
      x = self.search(key)
      if x:
        return self.delete(x)
      return False
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is 'doubly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(dlt.head) == get_strs([])
  
  dlt.insert(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  
  res = dlt.search(0)
  assert res == node_0
  
  res = dlt.search(1)
  assert res == None
  
  dlt.delete(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs([])
  
  for node in reversed(nodes):
    dlt.insert(node)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data(nodes))
  
  res = dlt.search(2)
  assert res == node_2

  res = dlt.search(3)
  assert res == node_3

  LinkedList.delete_after(node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1]))

  LinkedList.insert_after(node_1, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
    
  LinkedList.insert_after(node_1, node_2)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt.delete(node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))

  dlt.delete(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))

  dlt.insert_by_data(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_1, node_2, node_3]))

  dlt.insert_by_data(0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt.delete_by_key(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))

  dlt.delete_by_key(0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))

  print('use_class_1 success')
  # Test end

def use_funcs_1():
  """
    Implement a doubly-linked list by a `head` node and other functions.
  """
  # Implement start
  class Node(object):
    def __init__(self, data=None, nxt=None, prv=None):
      self.data = data
      self.nxt = nxt
      self.prv = prv

  def insert_after(node, new_node):
    new_node.nxt = node.nxt
    if node.nxt:
      node.nxt.prv = new_node
    node.nxt = new_node
    new_node.prv = node

  def delete_after(node):
    if node.nxt:
      node.nxt = node.nxt.nxt
      if node.nxt: # the updated node.nxt could be None, we must use `if` to check.
        node.nxt.prv = node

  def search(head, key):
    x = head
    while x and (x.data != key):
      x = x.nxt
    return x # if x is None, it means 'find nothing'

  def insert(head, x):
    x.nxt = head
    if head:
      head.prv = x
    head = x
    x.prv = None
    return head

  def delete(head, x):
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though users input valid arguments,
      we still need to do some edge case handling:
      1. the linked list is empty, that is `head` is `None`
      2. the node we want to delete is just the `head`
    """
    if not head:
      return head, False # return False means 'delete failed.'
    if x.prv is None: # x is head
      head = x.nxt
    else:
      x.prv.nxt = x.nxt
    if x.nxt:
      x.nxt.prv = x.prv
    return head, True

  def insert_by_data(head, data):
    new_node = Node(data)
    return insert(head, new_node)

  def delete_by_key(head, key):
    x = search(head, key)
    if x:
      return delete(head, x)
    return head, False
  # Implement end

  # Test start
  dlt = None # dlt is 'doubly-linked list', in this demo it is just a head node.
  node_0 = Node(0)
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(dlt) == get_strs([])
  
  dlt = insert(dlt, node_0)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0]))
  
  res = search(dlt, 0)
  assert res == node_0
  
  res = search(dlt, 1)
  assert res == None
  
  dlt, status = delete(dlt, node_0)
  assert get_str_from_head_node(dlt) == get_strs([])
 
  for node in reversed(nodes):
    dlt = insert(dlt, node)
  assert get_str_from_head_node(dlt) == get_strs(get_data(nodes))
  
  res = search(dlt, 2)
  assert res == node_2

  res = search(dlt, 3)
  assert res == node_3

  delete_after(node_1)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))

  delete_after(node_3)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))

  delete_after(node_1)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1]))

  insert_after(node_1, node_3)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1, node_3]))
    
  insert_after(node_1, node_2)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt, status = delete(dlt, node_1)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_2, node_3]))

  dlt, status = delete(dlt, node_0)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_2, node_3]))

  dlt = insert_by_data(dlt, 1)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_1, node_2, node_3]))

  dlt = insert_by_data(dlt, 0)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_1, node_2, node_3]))

  dlt, status = delete_by_key(dlt, 1)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_0, node_2, node_3]))

  dlt, status =delete_by_key(dlt, 0)
  assert get_str_from_head_node(dlt) == get_strs(get_data([node_2, node_3]))

  print('use_funcs_1 success')
  # Test end

def use_class_2():
  """
    Implement a doubly-linked list by a class with `head`, `tail` and `length` attributes.
    In this implement I combine case (b) + (c) as described on the top of this file.
    It is easy to decouple it into case (b) and case (c) separately. Just try by yourself.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    @staticmethod
    def insert_after(linked_list, node, new_node):
      """
        We expect the input `node` and `new_node` belong to `linked_list`
      """
      new_node.nxt = node.nxt
      if node.nxt:
        node.nxt.prv = new_node
      node.nxt = new_node
      new_node.prv = node
      if node == linked_list.tail:
        linked_list.tail = new_node
      linked_list.inc_len()

    @staticmethod
    def delete_after(linked_list, node):
      """
        We expect the input `node` belongs to `linked_list`
      """
      if node.nxt:
        node.nxt = node.nxt.nxt
        if node.nxt:
          node.nxt.prv = node
        else: # node now becomes a tail
          linked_list.tail = node
        linked_list.dec_len()

    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

    def search(self, key):
      x = self.head
      while x and (x.data != key):
        x = x.nxt
      return x # if x is None, it means 'find nothing'

    def insert(self, x):
      x.nxt = self.head
      if self.head:
        self.head.prv = x
      else:
        self.tail = x
      self.head = x
      x.prv = None
      self.inc_len()

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do some edge case handling:
        1. the linked list is empty, that is `self.head` is `None`
        2. the node we want to delete is just the `self.head`
      """
      if self.head is None:
        return False
      if x.prv is None: # x is head
        self.head = x.nxt
        if self.head is None:
          # In this block means, before deletion, self.head = self.tail and self.length = 1
          self.tail = self.head
      else:
        x.prv.nxt = x.nxt
      if x.nxt:
        x.nxt.prv = x.prv
      self.dec_len()
      return True

    def insert_by_data(self, data):
      new_node = LinkedList.Node(data)
      self.insert(new_node)

    def delete_by_key(self, key):
      x = self.search(key)
      if x:
        return self.delete(x)
      return False

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
      x = self.head
      while i < idx:
        x = x.nxt
        i += 1
      return x

    def append(self, x):
      """
        For demo/interview, we expect x.nxt is None and don't do further check.
      """
      if self.tail:
        # linked list with at least one node
        self.tail.nxt = x
        x.prv = self.tail
        self.tail = x
        self.tail.nxt = None
        self.inc_len()
      else:
        # empty linked list
        self.insert(x)

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
        self.delete(self.head)
      else:
        prv = self.search_by_idx(idx - 1)
        LinkedList.delete_after(self, prv)
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is 'doubly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(dlt.head) == get_strs([])
  assert dlt.head is None
  assert dlt.tail is None
  assert dlt.get_len() == 0
 
  dlt.insert(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == dlt.tail
  assert dlt.get_len() == 1
  
  res = dlt.search(0)
  assert res == node_0
  
  res = dlt.search(1)
  assert res == None
  
  dlt.delete(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs([])
  assert dlt.head is None
  assert dlt.tail is None
  assert dlt.get_len() == 0
  
  for node in reversed(nodes):
    dlt.insert(node)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data(nodes))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 4
  
  res = dlt.search(2)
  assert res == node_2

  res = dlt.search(3)
  assert res == node_3

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  LinkedList.delete_after(dlt, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  LinkedList.delete_after(dlt, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1]))
  assert dlt.head == node_0
  assert dlt.tail == node_1
  assert dlt.get_len() == 2

  LinkedList.insert_after(dlt, node_1, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 3
    
  LinkedList.insert_after(dlt, node_1, node_2)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 4

  dlt.delete(node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  dlt.delete(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))
  assert dlt.head == node_2
  assert dlt.tail == node_3
  assert dlt.get_len() == 2

  dlt.insert_by_data(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_1, node_2, node_3]))
  assert dlt.head.data == node_1.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  dlt.insert_by_data(0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.head.data == node_0.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert dlt.get_len() == 4

  dlt.delete_by_key(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head.data == node_0.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  dlt.delete_by_key(0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))
  assert dlt.head == node_2
  assert dlt.tail == node_3
  assert dlt.get_len() == 2

  dlt.insert(node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 3

  res = dlt.search_by_idx(0)
  assert res == node_0

  res = dlt.search_by_idx(1)
  assert res == node_2

  res = dlt.search_by_idx(2)
  assert res == node_3

  dlt.delete_by_idx(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 2

  dlt.delete_by_idx(1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == node_0
  assert dlt.tail == node_0
  assert dlt.get_len() == 1

  dlt.delete_by_idx(0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([]))
  assert dlt.head == None
  assert dlt.tail == None
  assert dlt.get_len() == 0

  dlt.insert_by_idx(0, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == node_0
  assert dlt.tail == node_0
  assert dlt.get_len() == 1

  dlt.insert_by_idx(1, node_2)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2]))
  assert dlt.head == node_0
  assert dlt.tail == node_2
  assert dlt.get_len() == 2

  dlt.insert_by_idx(1, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2]))
  assert dlt.head == node_0
  assert dlt.tail == node_2
  assert dlt.get_len() == 3

  dlt.append(node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data(nodes))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert dlt.get_len() == 4

  print('use_class_2 success')
  # Test end

def use_funcs_2():
  """
    Implement a doubly-linked list by a class with `head`, `tail` and `length` attributes, and other functions.
    In this implement I combine case (b) + (c) as described on the top of this file.
    It is easy to decouple it into case (b) and case (c) separately. Just try by yourself.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None, prv=None):
        self.data = data
        self.nxt = nxt
        self.prv = prv

    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

  def insert_after(linked_list, node, new_node):
    """
      We expect the input `node` and `new_node` belong to `linked_list`
    """
    new_node.nxt = node.nxt
    if node.nxt:
      node.nxt.prv = new_node
    node.nxt = new_node
    new_node.prv = node
    if node == linked_list.tail:
      linked_list.tail = new_node
    inc_len(linked_list)

  def delete_after(linked_list, node):
    """
      We expect the input `node` belongs to `linked_list`
    """
    if node.nxt:
      node.nxt = node.nxt.nxt
      if node.nxt:
        node.nxt.prv = node
      else: # node now becomes a tail
        linked_list.tail = node
      dec_len(linked_list)

  def search(linked_list, key):
    x = linked_list.head
    while x and (x.data != key):
      x = x.nxt
    return x # if x is None, it means 'find nothing'

  def insert(linked_list, x):
    x.nxt = linked_list.head
    if linked_list.head:
      linked_list.head.prv = x
    else:
      linked_list.tail = x
    linked_list.head = x
    x.prv = None
    inc_len(linked_list)

  def delete(linked_list, x):
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though users input valid arguments,
      we still need to do some edge case handling:
      1. the linked list is empty, that is `linked_list.head` is `None`
      2. the node we want to delete is just the `linked_list.head`
    """
    if linked_list.head is None:
      return False
    if x.prv is None: # x is head
      linked_list.head = x.nxt
      if linked_list.head is None:
        # In this block means, before deletion, linked_list.head = linked_list.tail and linked_list.length = 1
        linked_list.tail = linked_list.head
    else:
      x.prv.nxt = x.nxt
    if x.nxt:
      x.nxt.prv = x.prv
    dec_len(linked_list)
    return True

  def insert_by_data(linked_list, data):
    new_node = LinkedList.Node(data)
    insert(linked_list, new_node)

  def delete_by_key(linked_list, key):
    x = search(linked_list, key)
    if x:
      return delete(linked_list, x)
    return False

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
    x = linked_list.head
    while i < idx:
      x = x.nxt
      i += 1
    return x

  def append(linked_list, x):
    """
      For demo/interview, we expect x.nxt is None and don't do further check.
    """
    if linked_list.tail:
      # linked list with at least one node
      linked_list.tail.nxt = x
      x.prv = linked_list.tail
      linked_list.tail = x
      linked_list.tail.nxt = None
      inc_len(linked_list)
    else:
      # empty linked list
      insert(linked_list, x)

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
      delete(linked_list, linked_list.head)
    else:
      prv = search_by_idx(linked_list, idx - 1)
      delete_after(linked_list, prv)
  # Implement end

  # Test start
  dlt = LinkedList() # dlt is 'doubly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(dlt.head) == get_strs([])
  assert dlt.head is None
  assert dlt.tail is None
  assert get_len(dlt) == 0
 
  insert(dlt, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == dlt.tail
  assert get_len(dlt) == 1
  
  res = search(dlt, 0)
  assert res == node_0
  
  res = search(dlt, 1)
  assert res == None
  
  delete(dlt, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs([])
  assert dlt.head is None
  assert dlt.tail is None
  assert get_len(dlt) == 0
  
  for node in reversed(nodes):
    insert(dlt, node)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data(nodes))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 4
  
  res = search(dlt, 2)
  assert res == node_2

  res = search(dlt, 3)
  assert res == node_3

  delete_after(dlt, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  delete_after(dlt, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  delete_after(dlt, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1]))
  assert dlt.head == node_0
  assert dlt.tail == node_1
  assert get_len(dlt) == 2

  insert_after(dlt, node_1, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 3
    
  insert_after(dlt, node_1, node_2)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 4

  delete(dlt, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  delete(dlt, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))
  assert dlt.head == node_2
  assert dlt.tail == node_3
  assert get_len(dlt) == 2

  insert_by_data(dlt, 1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_1, node_2, node_3]))
  assert dlt.head.data == node_1.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  insert_by_data(dlt, 0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2, node_3]))
  assert dlt.head.data == node_0.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert get_len(dlt) == 4

  delete_by_key(dlt, 1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head.data == node_0.data # dlt.head is another Node instance
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  delete_by_key(dlt, 0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_2, node_3]))
  assert dlt.head == node_2
  assert dlt.tail == node_3
  assert get_len(dlt) == 2

  insert(dlt, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 3

  res = search_by_idx(dlt, 0)
  assert res == node_0

  res = search_by_idx(dlt, 1)
  assert res == node_2

  res = search_by_idx(dlt, 2)
  assert res == node_3

  delete_by_idx(dlt, 1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_3]))
  assert dlt.head == node_0
  assert dlt.tail == node_3
  assert get_len(dlt) == 2

  delete_by_idx(dlt, 1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == node_0
  assert dlt.tail == node_0
  assert get_len(dlt) == 1

  delete_by_idx(dlt, 0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([]))
  assert dlt.head == None
  assert dlt.tail == None
  assert get_len(dlt) == 0

  insert_by_idx(dlt, 0, node_0)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0]))
  assert dlt.head == node_0
  assert dlt.tail == node_0
  assert get_len(dlt) == 1

  insert_by_idx(dlt, 1, node_2)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_2]))
  assert dlt.head == node_0
  assert dlt.tail == node_2
  assert get_len(dlt) == 2

  insert_by_idx(dlt, 1, node_1)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data([node_0, node_1, node_2]))
  assert dlt.head == node_0
  assert dlt.tail == node_2
  assert get_len(dlt) == 3

  append(dlt, node_3)
  assert get_str_from_head_node(dlt.head) == get_strs(get_data(nodes))
  assert dlt.head == node_0
  assert dlt.tail == node_3
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
