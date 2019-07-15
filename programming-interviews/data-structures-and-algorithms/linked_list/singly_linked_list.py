"""
  Use python 3.6.8
"""
"""
  What is a linked list?
  A linked list is a data structure in which the objects are arranged in a linear order and
  the order is determined by pointers in each object.

  What is a singly-linked list?
  A singly-linked list is a linked list in which each object has a pointer `next` which points to its successor.

  How to implement a singly-linked list?
  You can consider make a singly-linked list support methods as follows by different cases:
  (assume `n` is the length of the linked list)
  * case (a) If the singly-linked list has `head`; each node has `data` and `nxt`:
    1. `search` with O(n) time complexity and it means "search by key".
    2. `insert` with O(1) time complexity and it means "insert a given node before head".
    3. `delete` with O(n) time complexity and it means "delete the given node".
    4. `insert_after` with O(1) time complexity and it means "insert a given node after another given node".
    5. `delete_after` with O(1) time complexity and it means "delete a given node after another given node".
    6. `insert_by_data` with O(1) time complexity and it means "insert a node from a given data"
    7. `delete_by_key` with O(n) time complexity and it means "delete the 1st node whose data is equal to key."
  * case (b) Based on (a), if the singly-linked list has additional `length`, then
    we can implement the above 1 ~ 7 plus the following 8, 9, 10:
    8. `search_by_idx` with O(n) time complexity.
    9. `insert_by_idx` with O(n) time complexity.
    10.`delete_by_idx` with O(n) time complexity.
  * case (c) Based on (a), if the singly-linked list has additional `tail`, then
    we can implement the above 1 ~ 7 plus the following 11:
    11. `append` with O(1) time complexity and it means "add a new node after tail".

  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).
  3. Adnan Aziz et al., "Elements of Programming Interviews in Python - The Insiders' Guide" (2018).

  There are some details for the following implement code:
    If we only need `head` and don't need `tail` and `length` and only want to use functions as operations
    then we can choose that we don't wrap `head` in an instance of `LinkedList` (like in `use_funcs_1`)
    and the `head` node itself represents the whole linked list
    because the code would be cleaner for more most interview questions.
    (If you prefer to wrap it, it is OK to do so.)
    However if we also need `tail` and `length`, then we usually wrap `head`, `tail` and `length`
    into an instance of `LinkedList` to keep updating status consistently.

    To focus on the code logic and make the code shorter in the interview,
    we assume when users use my API, they would always
    input valid arguments (ex: if the valid input is a string, they would not input an integer.)
    so we don't do much error handling and we just focus on edge case.
    
    If the interviewer want you to consider more error handling, you can consider
    1. Do input type checking by using `isinstance`, ex: `isinstance(3, int)` => check if 3 is an `int`
    2. Wrap your original code by `try ... except` as follows:
    ```
      def my_func(arg):
        try:
          your_original_code
        except Exception as e:
          print(e)
          do_more_error_handling_here
    ```

    If you need to use `tail` attribute to make some method/function like `append`
    more efficiently, please feel free to declare a wrapper class `LinkedList` like:
    ```
      class LinkedList(object):
        class Node(object):
          def __init__(self, data=None, nxt=None):
            self.data = data
            self.nxt = nxt
        def __init__(self, head=None, tail=None):
          self.head = head # head is a LinkedList.Node instance
          self.tail = tail # tail is a LinkedList.Node instance
    ```
    It is impossible to implement every scenario, in this file we just list 
    some common scenarios in classical text book, and if you are familiar with these scenarios,
    other challenges or vairiants would not beat you down.

    Note that under many different scenarios, the operation with the same name could have different
    meaning between you and the interviewer. Under this situation, the time complexity is not the same.
    Take `insert` as an example, if `insert` means "insert by index" in the interviewer's mind,
    then the time complexity is O(n) where n is the length of the linked list.
    (
      let's say, insert the given data into the 4th node (index 3) of the linked list, then it is
      obviously you should do while loop from head node (index 0) to the node with index 2, then
      create a new node with the given data and then point the new node's next to the index 2 node's next,
      finally point the index 2 node's next to the new node.
    )
    So, when interviewers want you to compare `insert` time complexity between an array and a linked list,
    you just clarify the context and then do the dicussion, everything would be OK.
"""
# Utils for test - start
def get_str_from_head_node(h, length=None):
  res = []
  node = h
  if isinstance(length, int):
    while length > 0:
      res.append(str(node.data))
      node = node.nxt
      length -= 1
  else:
    while node:
      res.append(str(node.data))
      node = node.nxt
  return get_str_from_list(res)

def get_str_from_list(src):
  return '[' + ' => '.join(map(lambda x: str(x), src)) + ']'

def get_data(nodes):
  return map(lambda x: x.data, nodes)

# Utils for test - end

def use_class_1():
  """
    Implement a singly-linked list by a class with a `head` attribute.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    @staticmethod
    def insert_after(node, new_node):
      new_node.nxt = node.nxt
      node.nxt = new_node

    @staticmethod
    def delete_after(node):
      if node.nxt:
        node.nxt = node.nxt.nxt

    def __init__(self):
      self.head = None

    def search(self, key):
      x = self.head
      while x and (x.data != key):
        x = x.nxt
      return x # if x is None, it means 'find nothing'

    def insert(self, x):
      x.nxt = self.head
      self.head = x

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do some edge case handling:
        1. the linked list is empty, that is `self.head` is `None`
        2. the node we want to delete is just the `self.head`
        3. the node we want to delete does not belong to our linked list.
      """
      if not self.head:
        return False # return False means 'delete failed.'
      if self.head == x:
        self.head = x.nxt
        return True # return True means 'delete successful.'
      node = self.head
      while node.nxt and node.nxt != x:
        node = node.nxt
      if node.nxt:
        node.nxt = x.nxt
        return True # the node we want to delete belongs to our linked list.
      return False # the node we want to delete does not belong to our linked list.

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
  slt = LinkedList() # slt is 'singly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  
  slt.insert(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  
  res = slt.search(0)
  assert res == node_0
  
  res = slt.search(1)
  assert res == None
  
  slt.delete(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  
  for node in reversed(nodes):
    slt.insert(node)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data(nodes))
  
  res = slt.search(2)
  assert res == node_2

  res = slt.search(3)
  assert res == node_3

  LinkedList.delete_after(node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1]))

  LinkedList.insert_after(node_1, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
    
  LinkedList.insert_after(node_1, node_2)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))

  slt.delete(node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))

  slt.delete(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))

  slt.insert_by_data(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_1, node_2, node_3]))

  slt.insert_by_data(0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))

  slt.delete_by_key(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))

  slt.delete_by_key(0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))

  print('use_class_1 success')
  # Test end

def use_funcs_1():
  """
    Implement a singly-linked list by a node with `data` and `nxt` attributes and other functions.
  """
  # Implement start
  class Node(object):
    def __init__(self, data=None, nxt=None):
      self.data = data
      self.nxt = nxt

  def insert_after(node, new_node):
    new_node.nxt = node.nxt
    node.nxt = new_node

  def delete_after(node):
    if node.nxt:
      node.nxt = node.nxt.nxt

  def search(head, key):
    x = head
    while x and (x.data != key):
      x = x.nxt
    return x

  def insert(head, x): # should return the new head
    x.nxt = head
    return x # x is the new head

  def delete(head, x): # should return the new head, and the successful/failed status
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though uses input valid arguments,
      we still need to do some edge case handling:
      1. the linked list is empty, that is `head` is `None`
      2. the node we want to delete is just the `head`
      3. the node we want to delete does not belong to our linked list.
    """
    if not head: return None, False
    if head == x:
      return x.nxt, True # x.nxt is the new head.
    node = head
    while node.nxt and node.nxt != x:
      node = node.nxt
    if node.nxt:
      node.nxt = x.nxt
      return head, True # the node we want to delete belongs to our linked list.
    return head, False # the node we want to delete does not belong to our linked list.

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
  slt = None # slt is 'singly-linked list', now it is just the head node.
  node_0 = Node(0)
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(slt) == get_str_from_list([])
  
  slt = insert(slt, node_0)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0]))

  res = search(slt, 0)
  assert res == node_0
  
  res = search(slt, 1)
  assert res == None
  
  slt, status = delete(slt, node_0)
  assert get_str_from_head_node(slt) == get_str_from_list([])
  
  for node in reversed(nodes):
    slt = insert(slt, node)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data(nodes))
  
  res = search(slt, 2)
  assert res == node_2

  res = search(slt, 3)
  assert res == node_3

  delete_after(node_1)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1, node_3]))

  delete_after(node_3)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1, node_3]))

  delete_after(node_1)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1]))

  insert_after(node_1, node_3)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1, node_3]))
    
  insert_after(node_1, node_2)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))

  slt, status = delete(slt, node_1)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_2, node_3]))

  slt, status = delete(slt, node_0)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_2, node_3]))

  slt = insert_by_data(slt, 1)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_1, node_2, node_3]))

  slt = insert_by_data(slt, 0)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))

  slt, status = delete_by_key(slt, 1)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_0, node_2, node_3]))

  slt, status = delete_by_key(slt, 0)
  assert get_str_from_head_node(slt) == get_str_from_list(get_data([node_2, node_3])) 

  print('use_funcs_1 success')
  # Test end

def use_class_2():
  """
    Implement a singly-linked list by a class with `head`, `tail` and `length` attributes.
    In this implement I combine case (b) + (c) as described on the top of this file.
    It is easy to decouple it into case (b) and case (c) separately. Just try by yourself.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    @staticmethod
    def insert_after(linked_list, node, new_node):
      """
        We expect the input `node` and `new_node` belong to `linked_list`
      """
      new_node.nxt = node.nxt
      node.nxt = new_node
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
        if not node.nxt: # node now becomes a tail
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
      if self.head is None: # before x is added, the linked list is empty.
        self.tail = x
      self.head = x
      self.inc_len()

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do some edge case handling:
        1. the linked list is empty, that is `self.head` is `None`
        2. the node we want to delete is just the `self.head`
        3. the node we want to delete does not belong to our linked list.
      """
      if not self.head:
        return False
      elif self.head == x: # it is possible that self.head == self.tail in this block
        self.head = x.nxt
        if self.head is None:
          # In this block means, before deletion, self.head = self.tail and self.length = 1
          self.tail = self.head
        self.dec_len()
      else:
        # In this block means
        # 1. we have at least 1 node in the linked list.
        # 2. the node x we want to delete is not head.
        node = self.head
        while node.nxt and node.nxt != x:
          node = node.nxt
        if node.nxt:
          node.nxt = x.nxt
          if node.nxt is None:
            self.tail = node
          self.dec_len()
          return True # the node we want to delete belongs to our linked list.
        return False # the node we want to delete does not belong to our linked list.

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
  slt = LinkedList() # slt is 'singly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  assert slt.head is None
  assert slt.tail is None
  assert slt.get_len() == 0
 
  slt.insert(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == slt.tail
  assert slt.get_len() == 1
  
  res = slt.search(0)
  assert res == node_0
  
  res = slt.search(1)
  assert res == None
  
  slt.delete(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  assert slt.head is None
  assert slt.tail is None
  assert slt.get_len() == 0
  
  for node in reversed(nodes):
    slt.insert(node)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data(nodes))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 4
  
  res = slt.search(2)
  assert res == node_2

  res = slt.search(3)
  assert res == node_3

  LinkedList.delete_after(slt, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 3

  LinkedList.delete_after(slt, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 3

  LinkedList.delete_after(slt, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1]))
  assert slt.head == node_0
  assert slt.tail == node_1
  assert slt.get_len() == 2

  LinkedList.insert_after(slt, node_1, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 3
    
  LinkedList.insert_after(slt, node_1, node_2)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 4

  slt.delete(node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 3

  slt.delete(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))
  assert slt.head == node_2
  assert slt.tail == node_3
  assert slt.get_len() == 2

  slt.insert_by_data(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_1, node_2, node_3]))
  assert slt.head.data == node_1.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert slt.get_len() == 3

  slt.insert_by_data(0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))
  assert slt.head.data == node_0.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert slt.get_len() == 4

  slt.delete_by_key(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head.data == node_0.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert slt.get_len() == 3

  slt.delete_by_key(0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))
  assert slt.head == node_2
  assert slt.tail == node_3
  assert slt.get_len() == 2

  slt.insert(node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 3

  res = slt.search_by_idx(0)
  assert res == node_0

  res = slt.search_by_idx(1)
  assert res == node_2

  res = slt.search_by_idx(2)
  assert res == node_3

  slt.delete_by_idx(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 2

  slt.delete_by_idx(1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == node_0
  assert slt.tail == node_0
  assert slt.get_len() == 1

  slt.delete_by_idx(0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([]))
  assert slt.head == None
  assert slt.tail == None
  assert slt.get_len() == 0

  slt.insert_by_idx(0, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == node_0
  assert slt.tail == node_0
  assert slt.get_len() == 1

  slt.insert_by_idx(1, node_2)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2]))
  assert slt.head == node_0
  assert slt.tail == node_2
  assert slt.get_len() == 2

  slt.insert_by_idx(1, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2]))
  assert slt.head == node_0
  assert slt.tail == node_2
  assert slt.get_len() == 3

  slt.append(node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data(nodes))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert slt.get_len() == 4

  print('use_class_2 success')
  # Test end

def use_funcs_2():
  """
    Implement a singly-linked list by linked list data with `head`, `tail` and `length` attributes and other functions.
    In this implement I combine case (b) + (c) as described on the top of this file.
    It is easy to decouple it into case (b) and case (c) separately. Just try by yourself.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

  def insert_after(linked_list, node, new_node):
    """
      We expect the input `node` and `new_node` belong to `linked_list`
    """
    new_node.nxt = node.nxt
    node.nxt = new_node
    if node == linked_list.tail:
      linked_list.tail = new_node
    inc_len(linked_list)

  def delete_after(linked_list, node):
    """
      We expect the input `node` belongs to `linked_list`
    """
    if node.nxt:
      node.nxt = node.nxt.nxt
      if not node.nxt: # node now becomes a tail
        linked_list.tail = node
      dec_len(linked_list)

  def search(linked_list, key):
    x = linked_list.head
    while x and (x.data != key):
      x = x.nxt
    return x # if x is None, it means 'find nothing'

  def insert(linked_list, x):
    x.nxt = linked_list.head
    if linked_list.head is None: # before x is added, the linked list is empty.
      linked_list.tail = x
    linked_list.head = x
    inc_len(linked_list)

  def delete(linked_list, x):
    """
      In our notes on the top of this file, we assume users don't input invalid arguments.
      However, for `delete`, even though users input valid arguments,
      we still need to do some edge case handling:
      1. the linked list is empty, that is `linked_list.head` is `None`
      2. the node we want to delete is just the `linked_list.head`
      3. the node we want to delete does not belong to our linked list.
    """
    if not linked_list.head:
      return False
    elif linked_list.head == x: # it is possible that linked_list.head == linked_list.tail in this block
      linked_list.head = x.nxt
      if linked_list.head is None:
        # In this block means, before deletion, linked_list.head = linked_list.tail and linked_list.length = 1
        linked_list.tail = linked_list.head
      dec_len(linked_list)
    else:
      # In this block means
      # 1. we have at least 1 node in the linked list.
      # 2. the node x we want to delete is not head.
      node = linked_list.head
      while node.nxt and node.nxt != x:
        node = node.nxt
      if node.nxt:
        node.nxt = x.nxt
        if node.nxt is None:
          linked_list.tail = node
        dec_len(linked_list)
        return True # the node we want to delete belongs to our linked list.
      return False # the node we want to delete does not belong to our linked list.

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
  slt = LinkedList() # slt is 'singly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  assert slt.head is None
  assert slt.tail is None
  assert get_len(slt) == 0
 
  insert(slt, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == slt.tail
  assert get_len(slt) == 1
  
  res = search(slt, 0)
  assert res == node_0
  
  res = search(slt, 1)
  assert res == None
  
  delete(slt, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list([])
  assert slt.head is None
  assert slt.tail is None
  assert get_len(slt) == 0
  
  for node in reversed(nodes):
    insert(slt, node)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data(nodes))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 4
  
  res = search(slt, 2)
  assert res == node_2

  res = search(slt, 3)
  assert res == node_3

  delete_after(slt, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 3

  delete_after(slt, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 3

  delete_after(slt, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1]))
  assert slt.head == node_0
  assert slt.tail == node_1
  assert get_len(slt) == 2

  insert_after(slt, node_1, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 3
    
  insert_after(slt, node_1, node_2)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 4

  delete(slt, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 3

  delete(slt, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))
  assert slt.head == node_2
  assert slt.tail == node_3
  assert get_len(slt) == 2

  insert_by_data(slt, 1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_1, node_2, node_3]))
  assert slt.head.data == node_1.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert get_len(slt) == 3

  insert_by_data(slt, 0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))
  assert slt.head.data == node_0.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert get_len(slt) == 4

  delete_by_key(slt, 1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head.data == node_0.data # slt.head is another Node instance
  assert slt.tail == node_3
  assert get_len(slt) == 3

  delete_by_key(slt, 0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_2, node_3]))
  assert slt.head == node_2
  assert slt.tail == node_3
  assert get_len(slt) == 2

  insert(slt, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 3

  res = search_by_idx(slt, 0)
  assert res == node_0

  res = search_by_idx(slt, 1)
  assert res == node_2

  res = search_by_idx(slt, 2)
  assert res == node_3

  delete_by_idx(slt, 1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_3]))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 2

  delete_by_idx(slt, 1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == node_0
  assert slt.tail == node_0
  assert get_len(slt) == 1

  delete_by_idx(slt, 0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([]))
  assert slt.head == None
  assert slt.tail == None
  assert get_len(slt) == 0

  insert_by_idx(slt, 0, node_0)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0]))
  assert slt.head == node_0
  assert slt.tail == node_0
  assert get_len(slt) == 1

  insert_by_idx(slt, 1, node_2)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_2]))
  assert slt.head == node_0
  assert slt.tail == node_2
  assert get_len(slt) == 2

  insert_by_idx(slt, 1, node_1)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data([node_0, node_1, node_2]))
  assert slt.head == node_0
  assert slt.tail == node_2
  assert get_len(slt) == 3

  append(slt, node_3)
  assert get_str_from_head_node(slt.head) == get_str_from_list(get_data(nodes))
  assert slt.head == node_0
  assert slt.tail == node_3
  assert get_len(slt) == 4

  print('use_funcs_2 success')
  # Test end

def main():
  use_class_1()
  use_funcs_1()
  use_class_2()
  use_funcs_2()

if __name__ == '__main__':
  main()
