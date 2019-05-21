from __future__ import print_function

class LruItem(object):
  def __init__(self, key=None, data=None, prv=None, nxt=None):
    self.key = key
    self.data = data
    self.prv = prv
    self.nxt = nxt

class IsbnCache(object):
  """
    The time complexity for lookup, insert, evict, and remove is O(1)
  """
  def __init__(self, lru_limit=3):
    self.cache = {}
    self.lru_head = None
    self.lru_tail = None
    self.lru_len = 0
    self.lru_limit = lru_limit

  def lookup(self, key):
    if key in self.cache:
      self.insert(key)
      return self.cache[key].data
    return None

  def insert(self, key, price=None):
    if key in self.cache:
      new_lru_head = self.remove(key)
      new_lru_head.nxt = self.lru_head
      self.lru_head = new_lru_head
    else:
      new_lru_head = LruItem(key, price, None, self.lru_head)
      self.cache[key] = new_lru_head
      self.lru_head = new_lru_head
      self.lru_len += 1
      if self.lru_len == 1:
        self.lru_tail = self.lru_head
      else:
        self.lru_head.nxt.prv = self.lru_head
      if self.lru_len > self.lru_limit:
        self.evict()

  def evict(self):
    del self.cache[self.lru_tail.key]
    self.lru_tail = self.lru_tail.prv
    if self.lru_tail:
      self.lru_tail.nxt.prv = None
      self.lru_tail.nxt = None
    else: # no node in the linked list
      self.lru_head = None
    self.lru_len -= 1


  def remove(self, key):
    if key in self.cache:
      target = self.cache[key]
      del self.cache[key]
      if target == self.lru_head:
        self.lru_head = self.lru_head.nxt
        if self.lru_head:
          self.lru_head.prv.nxt = None
          self.lru_head.prv = None
        else: # no node in the linked list
          self.lru_tail = None
      elif target == self.lru_tail:
        self.lru_tail = self.lru_tail.prv
        if self.lru_tail:
          self.lru_tail.nxt = None
        else: # no node in the linked list
          self.lru_head = None
      else:
        target.prv.nxt = target.nxt
        target.nxt.prv = target.prv
        target.prv = None
        target.nxt = None
      self.lru_len -= 1
      return target

def show_double_linked_list(head, tail):
  node = head
  from_p_to_c = ' => '
  from_c_to_p = ' <= '
  res_p_to_c = []
  res_c_to_p = []
  while node:
    res_p_to_c.append(str(node.data))
    node = node.nxt
  node = tail
  while node:
    res_c_to_p.insert(0, str(node.data))
    node = node.prv
  print(from_p_to_c.join(res_p_to_c))
  print(from_c_to_p.join(res_c_to_p))

def show_cache(cache):
  res = {}
  for key in cache:
    res[key] = cache[key].data
  print(res)

def main():
  isbn_cache = IsbnCache(3)
  isbn_cache.insert(1, 100)
  isbn_cache.insert(2, 200)
  isbn_cache.insert(3, 300)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(4, 400)
  isbn_cache.insert(5, 500)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(6, 600)
  isbn_cache.insert(7, 700)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  print('='*20)

  isbn_cache = IsbnCache(1)
  isbn_cache.insert(1, 100)
  isbn_cache.insert(2, 200)
  isbn_cache.insert(3, 300)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(4, 400)
  isbn_cache.insert(5, 500)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(6, 600)
  isbn_cache.insert(7, 700)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  print('='*20)

  isbn_cache = IsbnCache(0)
  isbn_cache.insert(1, 100)
  isbn_cache.insert(2, 200)
  isbn_cache.insert(3, 300)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(4, 400)
  isbn_cache.insert(5, 500)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  isbn_cache.insert(6, 600)
  isbn_cache.insert(7, 700)
  show_cache(isbn_cache.cache)
  show_double_linked_list(isbn_cache.lru_head, isbn_cache.lru_tail)
  print('='*20)

if __name__ == '__main__':
  main()


