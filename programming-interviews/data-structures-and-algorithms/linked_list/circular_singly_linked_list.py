"""
  Use python 3.6.8
"""
"""
  # What is a linked list?
  A linked list is a data structure in which the objects are arranged in a linear order and
  the order is determined by pointers in each object.

  # What is a circular singly-linked list?
  A circular singly-linked list is a circular singly-linked list in which the tail node is connected to the head node.

  # How to implement a circular singly-linked list?
  You can consider make a circular singly-linked list support methods as follows by different cases:
  (assume `n` is the length of the linked list)
  * case (a) If the circular singly-linked list has `tail` (`tail.nxt` points to `head`); each node has `data` and `nxt`:
    1. `search` with O(n) time complexity and it means "search by key".
    2. `insert` with O(1) time complexity and it means "insert a given node before head".
    3. `delete` with O(n) time complexity and it means "delete the given node".
    4. `insert_after` with O(1) time complexity and it means "insert a given node after another given node".
    5. `delete_after` with O(1) time complexity and it means "delete a given node after another given node".
    6. `insert_by_data` with O(1) time complexity and it means "insert a node from a given data"
    7. `delete_by_key` with O(n) time complexity and it means "delete the 1st node whose data is equal to key."
    8. `append` with O(1) time complexity and it means "add a new node after tail".
  * case (b) Based on (a), if the circular singly-linked list has additional `length`, then
    we can implement the above 1 ~ 8 plus the following 9, 10, 11:
    9. `search_by_idx` with O(n) time complexity.
    10. `insert_by_idx` with O(n) time complexity.
    11.`delete_by_idx` with O(n) time complexity.

  # References
  The implements here are a summry of
  1. Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
  2. Frank M. Carrano, "Data Abstraction & Problem Solving with C++ - WALLS & MIRRORS, 5th" (2007).

  # Notes
  * The implement uses a `tail` not a `head`. This refers to page 217 of ref. 2 (Frank M. Carrano's book).
  * In this file, I don't implement case (b), since there is not so much discussion about circular singly-linked lists
  in traditional textbook (ref. 1 & 2). Feel free to try case (b) by yourself.
"""
# Utils for test - start
def get_str_from_tail_node(tail, length=None):
  res = []
  if tail:
    node = tail.nxt
    if isinstance(length, int):
      while length > 0:
        res.append(str(node.data))
        node = node.nxt
        length -= 1
    else:
      res.append(str(node.data))
      node = node.nxt
      while node != tail.nxt:
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
    Implement a circular singly-linked list by a class with a `tail` attribute.
  """
  # Implement start
  class LinkedList(object):
    class Node(object):
      def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    @staticmethod
    def insert_after(linked_list, node, new_node):
      new_node.nxt = node.nxt
      node.nxt = new_node
      if linked_list.tail == node:
        linked_list.tail = new_node

    @staticmethod
    def delete_after(linked_list, node):
      if linked_list.tail:
        if node.nxt == linked_list.tail:
          linked_list.tail = node
        node.nxt = node.nxt.nxt

    def __init__(self):
      self.tail = None
      # If self.tail is a node, then self.tail.nxt is head.

    def search(self, key):
      if self.tail:
        x = self.tail.nxt
        if x.data == key:
          return x
        else:
          x = x.nxt
          while (x != self.tail.nxt) and (x.data != key):
            x = x.nxt
          return x if x != self.tail.nxt else None  # None means 'find nothing'
      return None

    def insert(self, x):
      if self.tail:
        x.nxt = self.tail.nxt
        self.tail.nxt = x
      else:
        self.tail = x
        self.tail.nxt = self.tail

    def delete(self, x):
      """
        In our notes on the top of this file, we assume users don't input invalid arguments.
        However, for `delete`, even though users input valid arguments,
        we still need to do some edge case handling:
        1. the linked list is empty, that is `self.tail` is `None`
        2. the node we want to delete is just the `self.tail`
        3. the node we want to delete does not belong to our linked list.
      """
      if not self.tail:
        return False # return False means 'delete failed.'
      if self.tail.nxt == self.tail:
        # the list has only one node
        if self.tail == x:
          self.tail = None
          return True # return True means 'delete successful.'
        return False
      # the list has at least 2 nodes.
      if self.tail.nxt == x:
        # the node to delete is head
        self.tail.nxt = self.tail.nxt.nxt
        return True
      else:
        # the node to delete is not head
        node = self.tail.nxt
        while node.nxt != self.tail.nxt and node.nxt != x:
          node = node.nxt
        if node.nxt != self.tail.nxt:
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

    def append(self, x):
      if self.tail:
        LinkedList.insert_after(self, self.tail, x)
      else:
        self.insert(x)

    
  # Implement end

  # Test start
  slt = LinkedList() # slt is 'circular singly-linked list'
  node_0 = LinkedList.Node(0)
  node_1 = LinkedList.Node(1)
  node_2 = LinkedList.Node(2)
  node_3 = LinkedList.Node(3)
  nodes = [node_0, node_1, node_2, node_3]
  assert get_str_from_tail_node(slt.tail) == get_str_from_list([])
  
  slt.insert(node_0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_0]))
  
  res = slt.search(0)
  assert res == node_0
  
  res = slt.search(1)
  assert res == None
  
  slt.delete(node_0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list([])
  
  for node in reversed(nodes):
    slt.insert(node)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data(nodes))
  
  res = slt.search(2)
  assert res == node_2

  res = slt.search(3)
  assert res == node_3

  LinkedList.delete_after(slt, node_1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_0, node_1, node_3]))

  LinkedList.delete_after(slt, node_3)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1, node_3]))

  LinkedList.delete_after(slt, node_1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1]))

  LinkedList.insert_after(slt, node_1, node_3)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1, node_3]))
    
  LinkedList.insert_after(slt, node_1, node_2)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1, node_2, node_3]))

  slt.delete(node_1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_2, node_3]))

  slt.delete(node_0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_2, node_3]))

  slt.insert_by_data(1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1, node_2, node_3]))

  slt.insert_by_data(0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_0, node_1, node_2, node_3]))

  slt.delete_by_key(1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_0, node_2, node_3]))

  slt.delete_by_key(0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_2, node_3]))

  slt.append(node_0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_2, node_3, node_0]))

  slt.delete(node_3)
  slt.delete(node_2)
  slt.delete(node_0)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([]))

  slt.append(node_1)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1]))
  
  slt.append(node_2)
  assert get_str_from_tail_node(slt.tail) == get_str_from_list(get_data([node_1, node_2]))

  print('use_class_1 success')
  # Test end

def main():
  use_class_1()

if __name__ == '__main__':
  main()
