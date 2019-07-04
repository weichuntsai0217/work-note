
"""
  Use python 3.6.8
"""
"""
  # Question: What is the difference between an iterable and iterator?
  An iterable object is an object which implements __iter__ or __getitem__
  An iterator object is an object which implements __iter__ and __next__

  # Question: How for loop statement works in python?
  Behind the scenes, the for loop statement calls iter() on the container object (ex: list, tuple, dict, str).
  The iter function would use the container's __iter__ or __getitem__ method and then returns an iterator object
  that defines the method __next__() which accesses elements in the container one at a time.

  # Question: Why does python need to distinguish iterable and iterator?
  With iterable design, we can keep the initial state of data in iterable object,
  and re-generate iterator at any time we want.
  For example,
  we know that the built-in range functin would return an iterable:
  ```
    numbers = range(3)
    print(tuple(numbers)) # (0, 1, 2)
    print(tuple(numbers)) # (0, 1, 2)
  ```
  However, if range returns an iterator, then
  ```
  numbers = iter(range(3))
  print(tuple(numbers)) # (0, 1, 2), after this line, numbers runs out
  print(tuple(numbers)) # ()
  ```
"""

class MyrangeIterator(object):
  def __init__(self, n: int): # n must be >= 0
    self.i = 0
    self.n = n

  def __iter__(self):
    return self

  def __next__(self):
    if self.i < self.n:
      res = self.i
      self.i += 1
      return res
    raise StopIteration()

class MyrangeIterable(object):
  def __init__(self, n: int): # n must be >= 0
    self.n = n

  def __iter__(self):
    return MyrangeIterator(self.n)

def main():
  n = 5
  myrange_iterable = MyrangeIterable(n)
  myrange_iterator = iter(myrange_iterable)

  while True:
    try:
      print('next(myrange_iterator) =', next(myrange_iterator))
    except StopIteration:
      print('Done')
      break

  """
    With iterable design, we can keep the initial state of data in iterable object,
    and re-generate iterator at any time we want.
  """
  myrange_iterator = iter(myrange_iterable)
  while True:
    try:
      print('next(myrange_iterator) =', next(myrange_iterator))
    except StopIteration:
      print('Done')
      break

if __name__ == '__main__':
  main()
