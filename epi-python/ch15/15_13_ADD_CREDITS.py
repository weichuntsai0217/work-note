from __future__ import print_function
import bst

class Item(list):
  def __eq__(self, other):
    if other == None:
      return False
    return self[0] == other[0]
  def __ne__(self, other):
    return not self.__eq__(other)
  def __lt__(self, other):
    if other == None:
      return False
    return self[0] < other[0]
  def __le__(self, other):
    if other == None:
      return False
    return self.__lt__(other) or self.__eq__(other)
  def __gt__(self, other):
    if other == None:
      return False
    return not self.__le__(other)
  def __ge__(self, other):
    if other == None:
      return False
    return self.__gt__(other) or self.__eq__(other)

class Service(object):
  def __init__(self):
    self.table = {}
    self.root = None
    self.add_all_amount = 0

  def real_credit(self, credit):
    return credit + self.add_all_amount

  def insert(self, idx, credit):
    self.remove(idx)
    data = Item([credit, idx])
    if self.root:
      self.table[idx] = credit
      bst.Bst.insert(self.root, bst.BinaryTreeNode(Item([credit, idx])), append_when_same_key=True)
    self.root = bst.BinaryTreeNode(Item([credit, set([idx])]))
    return True

  def remove(self, idx):
    if idx in self.table:
      credit = self.table[idx]
      del self.table[idx]
      node = bst.Bst.search(self.root, Item([credit, idx]))
      node.data[1].remove(idx)
      if not node.data[1]:
        status, root = bst.Bst.delete(self.root, Item([credit, idx]))
        self.root = root
        return status
    return False

  def lookup(self, idx):
    if idx in self.table:
      return self.real_credit(self.table[idx])
    return None

  def add_to_all(self, amount):
    self.add_all_amount += amount

  def max_client(self):
    if self.root:
      return bst.Bst.last(self.root).data[1]
    return None

def main():
  srv = Service()
  srv.insert('e', 10)
  srv.insert('c', 20)
  srv.insert('g', 5)
  srv.insert('a', 2)
  srv.insert('b', 1)
  srv.insert('d', 70)
  print(srv.root.left)
  srv.insert('d', 66)
  print(srv.root)
  print(srv.lookup('b'))
  srv.add_to_all(30)
  print(srv.lookup('b'))
  print(srv.max_client())
  print(srv.root)

if __name__ == '__main__':
  main()





