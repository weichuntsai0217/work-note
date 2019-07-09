"""
  Use python 3.6.8
"""
"""
  # Question: What is the difference between an iterator and a generator?

  The answer is, a generator is an easy way to create a iterator.
  
  Generators are written like regular functions but use the yield statement
  whenever they want to return data. Each time next() is called on it,
  the generator resumes where it left off
  (it remembers all the data values and which statement was last executed).

  When a generator is executed, it would return an object in which
  the __iter__() and __next__() methods are created automatically.
  That's why we say "a generator is an easy way to create a iterator.".
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

def myrange_generator(n: int): # n must be >= 0
  i = 0
  while True:
    if i < n:
      res = i
      i += 1
      yield res
    else:
      break

def main():
  n = 5
  myrange_iterator = MyrangeIterator(n)
  myrange_iterator_from_generator = myrange_generator(n)

  for i in myrange_iterator:
    print('In for loop, i =', i)
  print('For loop done')

  myrange_iterator = MyrangeIterator(n)
  while True:
    try:
      print('next(myrange_iterator) =', next(myrange_iterator))
    except StopIteration:
      print('Done')
      break

  while True:
    try:
      print('next(myrange_iterator_from_generator) =', next(myrange_iterator_from_generator))
    except StopIteration:
      print('Done')
      break

if __name__ == '__main__':
  main()
