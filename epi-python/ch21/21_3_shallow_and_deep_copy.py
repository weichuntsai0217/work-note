"""
  Use python 3.6.8
"""
"""
  # Question: Describe the differences between a shallow copy and a deep copy. When is each appropriate,
  and when is neither appropriate? How is deep copy implemented?

  The difference is that, a shallow copy constructs a new compound object and then only inserts references
  into it to the objects found in the original. However a deep copy constructs a new compound object and
  then recursively inserts copies of the objects found in the original into the new created object.
  Please see the following code examples.

  Deep copy is more challenging to implement since recursive objects, if they contains references to themselves,
  could result in infinite recursion in a naive implementation of deep copy
"""

def main():
  import copy
  a = [[1,2,3], [4,5,6]]
  b = copy.copy(a)
  c = copy.deepcopy(a)

  print('=== before b changes its element')
  print('a =', a, ', a is the data source.')
  print('b =', b, ', b is a shallow copy of a.')
  print('c =', c, ', c is a deep copy of a.')
  b[0][0] = -5
  print('=== after b changes its element')
  print('a =', a) # a is also changed because b is a shallow copy of a
  print('b =', b)
  print('c =', c) # c is still unchanged because c is a deep copy of a


if __name__ == '__main__':
  main()
